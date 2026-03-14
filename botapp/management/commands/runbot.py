# botapp/management/commands/runbot.py
import asyncio
import json
import os
import re
from datetime import timedelta
from typing import Optional, Tuple, List

from django.core.management.base import BaseCommand
from django.db import close_old_connections
from django.utils import timezone

from asgiref.sync import sync_to_async

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import LabeledPrice
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, RetryAfter, UserDeactivated

import config
from botapp.models import User, Message, BlockedUser, SizeSearch, PaymentEvent

# импорт данных (как у тебя)
from baza import (
    glass_data, glass_data2, glass_data3, glass_data4,
    glass_data5, glass_data6, glass_data7
)
from baza2 import glass_data9


# ================== ПОДПИСКА / STARS ==================
SUB_CURRENCY = "XTR"         # Telegram Stars
SUB_PROVIDER_TOKEN = ""      # для Stars пустой

PLAN_MONTH_PRICE = 150
PLAN_MONTH_DAYS = 30

PLAN_YEAR_PRICE = 500
PLAN_YEAR_DAYS = 365

SUB_TITLE_MONTH = "Подписка на месяц"
SUB_DESC_MONTH = "Полный доступ ко всем результатам бота на 1 месяц."

SUB_TITLE_YEAR = "Подписка на год"
SUB_DESC_YEAR = "Полный доступ ко всем результатам бота на 1 год."


class UserRegistration(StatesGroup):
    name = State()
    city = State()
    phone_number = State()


belarusian_cities = [
    "minsk", "минск",
    "grodno", "гродно",
    "brest", "брест",
    "vitebsk", "витебск",
    "mogilev", "могилев",
    "gomel", "гомель",
    "baranovichi", "барановичи",
    "bobruisk", "бобруйск",
    "borisov", "борисов",
    "pinsk", "пинск",
    "orsha", "орша",
    "mozyr", "мозырь",
    "soligorsk", "солигорск",
    "lida", "лида",
    "novopolotsk", "новополоцк",
    "polotsk", "полоцк",
]
BEL_CITIES_SET = set([c.lower() for c in belarusian_cities])

AD_TEXT = (
    '<b>Для жителей РБ 🇧🇾</b>\n'
    'Сервис для разборщиков мобильной техники.\n'
    'Канал: <a href="https://t.me/MobiraRazbor">@MobiraRazbor</a>\n'
    'Чат: <a href="https://t.me/mobirazbor_chat">@mobirazbor_chat</a>\n'
    'Сайт: <a href="https://mobirazbor.by">mobirazbor.by</a>'
)

# ✅ не логируем эти сообщения/команды
SKIP_LOG_TEXTS = {
    "/start",
    "/info",
    # кнопки:
    "🚀 start",
    "ℹ️ Info",
}

# Тексты кнопок
BTN_START = "🚀 start"
BTN_REG = "🗂registration"
BTN_INFO = "ℹ️ Info"
BTN_SIZE = "🔎подбор стекла по размеру"
BTN_SUB = "⭐ Подписка"
BTN_STATUS = "📅 Статус"
BTN_MENU = "↩️ В меню"


def add_src(url: str, src: str) -> str:
    return f"{url}&src={src}" if "?" in url else f"{url}?src={src}"


# ----------------- Django ORM wrappers for async -----------------

@sync_to_async(thread_sensitive=True)
def db_is_user_blocked(user_id: int) -> bool:
    return BlockedUser.objects.filter(user_id=user_id).exists()


@sync_to_async(thread_sensitive=True)
def db_get_user_info(chat_id: int):
    u = User.objects.filter(chat_id=chat_id).first()
    if not u:
        return None
    return (u.name, u.city, u.phone_number)


@sync_to_async(thread_sensitive=True)
def db_ensure_user_exists(chat_id: int):
    User.objects.get_or_create(chat_id=chat_id)


@sync_to_async(thread_sensitive=True)
def db_get_subscribed_until(chat_id: int):
    u = User.objects.filter(chat_id=chat_id).only("subscribed_until").first()
    if not u:
        return None
    return u.subscribed_until


@sync_to_async(thread_sensitive=True)
def db_is_subscribed(chat_id: int) -> bool:
    u = User.objects.filter(chat_id=chat_id).only("subscribed_until").first()
    if not u or not u.subscribed_until:
        return False
    return u.subscribed_until > timezone.now()


@sync_to_async(thread_sensitive=True)
def db_grant_subscription(
    chat_id: int,
    days: int,
    charge_id: Optional[str],
    total_amount: Optional[int],
    currency: Optional[str],
):
    u, _ = User.objects.get_or_create(chat_id=chat_id)

    now = timezone.now()
    base = u.subscribed_until if (getattr(u, "subscribed_until", None) and u.subscribed_until > now) else now
    u.subscribed_until = base + timedelta(days=days)

    update_fields = ["subscribed_until"]

    if hasattr(u, "last_stars_charge_id"):
        u.last_stars_charge_id = charge_id
        update_fields.append("last_stars_charge_id")
    if hasattr(u, "last_payment_total_amount"):
        u.last_payment_total_amount = total_amount
        update_fields.append("last_payment_total_amount")
    if hasattr(u, "last_payment_currency"):
        u.last_payment_currency = currency
        update_fields.append("last_payment_currency")
    if hasattr(u, "last_payment_at"):
        u.last_payment_at = now
        update_fields.append("last_payment_at")

    u.save(update_fields=update_fields)


@sync_to_async(thread_sensitive=True)
def db_save_message(chat_id: int, text: str):
    if not text:
        return
    t = text.strip()
    if t in SKIP_LOG_TEXTS:
        return
    Message.objects.create(chat_id=chat_id, message_text=text)


@sync_to_async(thread_sensitive=True)
def db_save_size_search(chat_id, height, width, found_count, source="unknown"):
    SizeSearch.objects.create(
        chat_id=int(chat_id),
        height=float(height),
        width=float(width),
        found_count=int(found_count),
        source=str(source),
    )


@sync_to_async(thread_sensitive=True)
def db_user_upsert(chat_id: int, name: str, city: str, phone_number: str):
    User.objects.update_or_create(
        chat_id=chat_id,
        defaults={"name": name, "city": city, "phone_number": phone_number},
    )


@sync_to_async(thread_sensitive=True)
def db_user_delete(chat_id: int):
    User.objects.filter(chat_id=chat_id).delete()


@sync_to_async(thread_sensitive=True)
def db_block_add(user_id: int):
    BlockedUser.objects.get_or_create(user_id=user_id)


@sync_to_async(thread_sensitive=True)
def db_block_remove(user_id: int):
    BlockedUser.objects.filter(user_id=user_id).delete()


@sync_to_async(thread_sensitive=True)
def db_get_all_chat_ids():
    return list(User.objects.values_list("chat_id", flat=True))


@sync_to_async(thread_sensitive=True)
def db_get_belarusian_chat_ids():
    rows = list(User.objects.values_list("chat_id", "city"))
    out = []
    for chat_id, city in rows:
        if city and city.lower() in BEL_CITIES_SET:
            out.append(chat_id)
    return out


@sync_to_async(thread_sensitive=True)
def db_log_payment_event(chat_id: int, event_type: str, amount=None, currency=None, charge_id=None, payload=None):
    PaymentEvent.objects.create(
        chat_id=chat_id,
        event_type=event_type,
        amount=amount,
        currency=currency,
        charge_id=charge_id,
        payload=payload,
    )


# ----------------- bot helpers -----------------

async def create_menu_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.row(types.KeyboardButton(BTN_START), types.KeyboardButton(BTN_INFO))
    markup.row(types.KeyboardButton(BTN_REG), types.KeyboardButton(BTN_STATUS))
    markup.row(
        types.KeyboardButton(BTN_SIZE, web_app=types.WebAppInfo(url=add_src(config.WEBAPP_URL, "menu"))),
        types.KeyboardButton(BTN_SUB),
    )
    return markup


async def send_message_with_ad(bot: Bot, chat_id, text, reply_markup=None, parse_mode="html"):
    ad_text = "\n\nmobirazbor.by"
    await bot.send_message(chat_id, text + ad_text, reply_markup=reply_markup, parse_mode=parse_mode)


def perform_size_search(height, width):
    found = []
    for glass9 in glass_data9:
        try:
            if float(glass9.get("height")) == float(height) and float(glass9.get("width")) == float(width):
                found.append({
                    "model": glass9.get("model"),
                    "photo_path": glass9.get("photo_path", None),
                })
        except Exception:
            continue
    return found


def limit_results(found_list, subscribed: bool, limit: int = 1):
    if subscribed:
        return found_list, 0
    if not found_list:
        return [], 0
    if len(found_list) <= limit:
        return found_list, 0
    return found_list[:limit], len(found_list) - limit


def mask_line(style: str = "lottery") -> str:
    if style == "dots":
        body = "•" * 18
    elif style == "stars":
        body = "✶" * 18
    elif style == "scratch":
        body = ("▓▒" * 9)[:18]
    else:
        body = "▓" * 18
    return f"<code>{body}</code>"


def build_masked_list(hidden_count: int, style: str = "lottery") -> str:
    if hidden_count <= 0:
        return ""
    return "\n".join(mask_line(style=style) for _ in range(hidden_count))


def find_model_in_dataset(query_lower: str, dataset) -> Optional[Tuple[str, list]]:
    for model, glasses in dataset:
        if query_lower == str(model).lower():
            return model, glasses
    return None


def fmt_dt(dt):
    if not dt:
        return None
    try:
        local_dt = timezone.localtime(dt)
    except Exception:
        local_dt = dt
    return local_dt.strftime("%d.%m.%Y %H:%M")


def alpha_label(n: int) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[n] if n < len(letters) else ""


def pretty_item_prefix() -> str:
    return "•"


def is_service_line(item) -> bool:
    """
    НЕ стекло (служебные строки):
    - display / дисплей
    - фото / .png
    - пустые строки
    """
    if not isinstance(item, str):
        return False
    s = item.strip().lower()
    if not s:
        return True
    if s.endswith(".png"):
        return True
    if "фото" in s or "photo" in s:
        return True
    if "display" in s or "диспле" in s:
        return True
    return False


def count_hidden_glasses(found_list: list, visible_count: int = 1) -> int:
    """
    Считаем, сколько СТЁКОЛ скрыто (игнорируя display/фото/.png).
    """
    hidden_part = found_list[visible_count:]
    only_glasses = [x for x in hidden_part if not is_service_line(x)]
    return len(only_glasses)


def extract_glasses_for_photo_caption(message_text: str) -> List[str]:
    """
    В подпись к фото: перечень стёкол из сообщения, где нажали кнопку "Фото".
    Игнорируем заголовки, лотерейку, строки про фото/дисплей/скрыто/подписку.
    """
    if not message_text:
        return []

    plain = re.sub(r"<[^>]+>", "", message_text)
    lines = [ln.strip() for ln in plain.splitlines() if ln.strip()]

    out: List[str] = []
    for ln in lines:
        low = ln.lower()

        if "взаимозаменяемые" in low:
            continue
        if "по запросу" in low:
            continue
        if ("результаты" in low) and ("размер" in low):
            continue
        if low.startswith("🔒") or low.startswith("⭐"):
            continue
        if "скрыто" in low:
            continue
        if "кнопка ниже" in low:
            continue
        if "▓" in ln or "▒" in ln:
            continue

        if ln.startswith("•"):
            if "фото" in low or "photo" in low:
                continue
            if "display" in low or "диспле" in low:
                continue
            out.append(ln)

    return out


async def send_updates_to_all_users_rb(bot_instance, message_text):
    chat_ids = await db_get_belarusian_chat_ids()
    for chat_id in chat_ids:
        try:
            await bot_instance.send_message(chat_id, message_text)
        except Exception as e:
            print(f"Ошибка при отправке {chat_id}: {e}")


async def send_to_all_users(bot_instance, message_text: str):
    chat_ids = await db_get_all_chat_ids()
    ok, fail = 0, 0
    for chat_id in chat_ids:
        try:
            await bot_instance.send_message(chat_id, message_text)
            ok += 1
            await asyncio.sleep(0.05)
        except RetryAfter as e:
            await asyncio.sleep(e.timeout)
            try:
                await bot_instance.send_message(chat_id, message_text)
                ok += 1
            except Exception as e2:
                print(f"❌ send fail after RetryAfter to {chat_id}: {e2}")
                fail += 1
        except (BotBlocked, ChatNotFound, UserDeactivated) as e:
            print(f"⚠️ unreachable {chat_id}: {e}")
            fail += 1
        except Exception as e:
            print(f"❌ send error to {chat_id}: {e}")
            fail += 1
    return ok, fail


def build_bot():
    tok = getattr(config, "tok", None) or os.getenv("BOT_TOKEN")
    if not tok:
        raise SystemExit("❌ BOT token not found. Set config.tok or env BOT_TOKEN.")

    bot = Bot(tok)
    dp = Dispatcher(bot, storage=MemoryStorage())
    ADMIN_ID = config.ADMIN_ID

    # ================== SUBSCRIBE / STATUS ==================

    async def show_status(chat_id: int):
        until = await db_get_subscribed_until(chat_id)
        now = timezone.now()
        if until and until > now:
            await bot.send_message(
                chat_id,
                f"✅ <b>Подписка активна</b>\n"
                f"Действует до: <b>{fmt_dt(until)}</b>\n\n"
                "Спасибо за поддержку 🙌",
                parse_mode="html",
                reply_markup=await create_menu_button(),
            )
        else:
            await bot.send_message(
                chat_id,
                "🔒 <b>Подписка не активна</b>\n\n"
                "⭐ <b>Тарифы:</b>\n"
                f"• <b>1 месяц</b>: {PLAN_MONTH_PRICE}⭐ ({PLAN_MONTH_DAYS} дней)\n"
                f"• <b>1 год</b>: {PLAN_YEAR_PRICE}⭐ ({PLAN_YEAR_DAYS} дней)\n\n"
                "Оформить: /subscribe или кнопка «⭐ Подписка».",
                parse_mode="html",
                reply_markup=await create_menu_button(),
            )

    @dp.message_handler(commands=["status"])
    async def status_cmd(message: types.Message):
        chat_id = message.chat.id
        await db_ensure_user_exists(chat_id)
        await db_save_message(chat_id, "/status")
        await show_status(chat_id)

    @dp.message_handler(lambda m: m.text == BTN_STATUS)
    async def status_button(message: types.Message):
        chat_id = message.chat.id
        await db_ensure_user_exists(chat_id)
        await db_save_message(chat_id, BTN_STATUS)
        await show_status(chat_id)

    async def send_invoice_for_plan(chat_id: int, plan: str):
        if plan == "month":
            title = SUB_TITLE_MONTH
            desc = SUB_DESC_MONTH
            days = PLAN_MONTH_DAYS
            price = PLAN_MONTH_PRICE
        else:
            title = SUB_TITLE_YEAR
            desc = SUB_DESC_YEAR
            days = PLAN_YEAR_DAYS
            price = PLAN_YEAR_PRICE

        prices = [LabeledPrice(label=f"Подписка ({days} дней)", amount=price)]
        payload = f"sub:{plan}:{chat_id}"

        await bot.send_invoice(
            chat_id=chat_id,
            title=title,
            description=desc,
            payload=payload,
            provider_token=SUB_PROVIDER_TOKEN,
            currency=SUB_CURRENCY,
            prices=prices,
        )

    @dp.message_handler(commands=["subscribe"])
    async def subscribe_cmd(message: types.Message):
        chat_id = message.chat.id
        await db_ensure_user_exists(chat_id)

        username = getattr(message.from_user, "username", None)
        await db_log_payment_event(
            chat_id,
            "subscribe_click",
            payload=f"username=@{username}" if username else "username=None"
        )

        await db_save_message(chat_id, "/subscribe")

        if await db_is_subscribed(chat_id):
            return await message.answer(
                "✅ У вас уже активна подписка.\n"
                "Нажмите «📅 Статус» чтобы посмотреть дату окончания.",
                reply_markup=await create_menu_button()
            )

        kb = types.InlineKeyboardMarkup(row_width=1)
        kb.add(
            types.InlineKeyboardButton(
                f"⭐ 1 месяц — {PLAN_MONTH_PRICE}⭐ ({PLAN_MONTH_DAYS} дней)",
                callback_data="buy:month"
            ),
            types.InlineKeyboardButton(
                f"⭐ 1 год — {PLAN_YEAR_PRICE}⭐ ({PLAN_YEAR_DAYS} дней)",
                callback_data="buy:year"
            ),
        )

        await message.answer(
            "⭐ <b>Выберите подписку</b>\n\n"
            f"• <b>1 месяц</b>: {PLAN_MONTH_PRICE}⭐ ({PLAN_MONTH_DAYS} дней)\n"
            f"• <b>1 год</b>: {PLAN_YEAR_PRICE}⭐ ({PLAN_YEAR_DAYS} дней)\n\n"
            "Нажмите кнопку ниже — откроется инвойс 👇",
            parse_mode="html",
            reply_markup=kb
        )

    @dp.message_handler(lambda m: m.text == BTN_SUB)
    async def subscribe_button(message: types.Message):
        await db_save_message(message.chat.id, BTN_SUB)
        await subscribe_cmd(message)

    @dp.callback_query_handler(lambda q: q.data and q.data.startswith("buy:"))
    async def buy_plan_callback(callback_query: types.CallbackQuery):
        chat_id = callback_query.from_user.id
        plan = callback_query.data.split(":", 1)[1].strip()

        if plan not in ("month", "year"):
            try:
                await callback_query.answer("Неверный тариф", show_alert=True)
            except Exception:
                pass
            return

        await db_log_payment_event(chat_id, "subscribe_plan_select", payload=f"plan={plan}")
        await send_invoice_for_plan(chat_id, plan)

        try:
            await callback_query.answer()
        except Exception:
            pass

    @dp.pre_checkout_query_handler(lambda q: True)
    async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
    async def successful_payment(message: types.Message):
        sp = message.successful_payment
        chat_id = message.chat.id

        charge_id = getattr(sp, "telegram_payment_charge_id", None) or getattr(sp, "provider_payment_charge_id", None)
        total_amount = getattr(sp, "total_amount", None)
        currency = getattr(sp, "currency", None)
        inv_payload = getattr(sp, "invoice_payload", None) or ""

        # payload: sub:<plan>:<chat_id>
        plan = "year"
        parts = inv_payload.split(":")
        if len(parts) >= 2 and parts[0] == "sub":
            plan = parts[1]

        days = PLAN_MONTH_DAYS if plan == "month" else PLAN_YEAR_DAYS

        await db_log_payment_event(
            chat_id,
            "successful_payment",
            amount=total_amount,
            currency=currency,
            charge_id=charge_id,
            payload=f"invoice_payload={inv_payload}",
        )

        await db_grant_subscription(chat_id, days, charge_id, total_amount, currency)
        until = await db_get_subscribed_until(chat_id)

        await message.answer(
            "✅ <b>Оплата успешна!</b>\n"
            f"⭐ Подписка активирована до: <b>{fmt_dt(until)}</b>\n\n"
            "Теперь доступ открыт полностью.",
            parse_mode="html",
            reply_markup=await create_menu_button()
        )

    # ================== ADMIN ==================

    @dp.message_handler(commands=["block"], user_id=ADMIN_ID)
    async def block_user(message: types.Message):
        try:
            user_id_to_block = int(message.text.split()[1])
            await db_block_add(user_id_to_block)
            await message.reply(f"Пользователь с ID {user_id_to_block} заблокирован.")
        except (IndexError, ValueError):
            await message.reply("Используйте команду в формате: /block <user_id>")

    @dp.message_handler(commands=["unblock"], user_id=ADMIN_ID)
    async def unblock_user_command(message: types.Message):
        try:
            user_id_to_unblock = int(message.text.split()[1])
            await db_block_remove(user_id_to_unblock)
            await message.reply(f"Пользователь с ID {user_id_to_unblock} разблокирован.")
        except (IndexError, ValueError):
            await message.reply("Используйте команду в формате: /unblock <user_id>")

    @dp.message_handler(commands=["send"])
    async def send_updates_command(message: types.Message):
        if message.from_user.id == ADMIN_ID:
            message_text = (
                "Друзья! Представляем новый проект — mobirazbor.by :\n"
                "платформа для разборщиков мобильной техники,\n"
                "удобный сервис для учёта и поиска запчастей мобильной техники.\n"
                "🔹Личный склад\n🔹Умный поиск по всей базе\n🔹Поддержка фото, описаний, отзывов и связи между пользователями\n"
            )
            await send_updates_to_all_users_rb(bot, message_text)
            await message.answer("Сообщение отправлено пользователям из РБ (по городам).")
        else:
            await message.answer("У вас нет прав для отправки сообщений.")

    @dp.message_handler(commands=["send1"])
    async def send1_command(message: types.Message):
        if message.from_user.id != ADMIN_ID:
            return await message.answer("У вас нет прав для отправки сообщений.")

        text = (
            "🔔 У нас появился новый проект\n\n"
            "🤖 Бот для поиска взаимозаменяемых защитных стёкол:\n"
            "https://t.me/safety_display_bot\n\n"
            "База активно наполняется и дорабатывается.\n\n"
            "📢 Канал с обновлениями:\n"
            "https://t.me/+ze8-aO_YZ-Q0ZGEy\n\n"
            "💬 Чат для обсуждений и предложений:\n"
            "https://t.me/+yJDx_G2b0hNjNTBi\n\n"
            "Если вы готовы поучаствовать в развитии проекта "
            "(делиться таблицами, наработками, информацией) — "
            "для вас будут сняты ограничения и открыт полный доступ.\n\n"
            "Спасибо за поддержку 🙌"
        )

        ok, fail = await send_to_all_users(bot, text)
        await message.answer(f"✅ Рассылка завершена.\nОтправлено: {ok}\nОшибок: {fail}")

    @dp.message_handler(commands=["send_to_user"])
    async def send_to_user_command(message: types.Message):
        if message.from_user.id == ADMIN_ID:
            try:
                user_id = int(message.text.split()[1])
                message_text = " ".join(message.text.split()[2:])
                await bot.send_message(user_id, message_text)
                await message.answer("Сообщение отправлено пользователю с ID: " + str(user_id))
            except (IndexError, ValueError):
                await message.answer("Формат: /send_to_user <ID> <текст>")
        else:
            await message.answer("У вас нет прав для отправки сообщений.")

    # ================== registration ==================

    @dp.message_handler(commands=["delete_registration"])
    async def delete_registration(message: types.Message):
        chat_id = message.chat.id
        await db_user_delete(chat_id)
        await bot.send_message(chat_id, "Ваши регистрационные данные успешно удалены. Для повторной регистрации используйте /registration")

    @dp.message_handler(state=UserRegistration.name)
    async def register_name(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        name = message.text
        await state.update_data(name=name)
        await UserRegistration.city.set()
        await bot.send_message(chat_id, "Введите Ваш город:", reply_markup=await create_menu_button())

    @dp.message_handler(lambda message: message.text.isdigit(), state=UserRegistration.city)
    async def register_invalid_city(message: types.Message):
        await bot.send_message(message.chat.id, "Некорректно введен город!")

    @dp.message_handler(state=UserRegistration.city)
    async def register_city(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        city = message.text
        await state.update_data(city=city)
        await UserRegistration.phone_number.set()
        await bot.send_message(chat_id, "Введите Ваш номер телефона:")

    @dp.message_handler(lambda message: not message.text.isdigit(), state=UserRegistration.phone_number)
    async def register_invalid_phone(message: types.Message):
        await bot.send_message(message.chat.id, "Номер телефона должен содержать только цифры. Введите корректный номер телефона.")

    @dp.message_handler(lambda message: message.text.isdigit(), state=UserRegistration.phone_number)
    async def register_phone_number(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        phone_number = message.text
        user_data = await state.get_data()
        name = user_data.get("name")
        city = user_data.get("city")

        await db_user_upsert(chat_id, name, city, phone_number)

        await state.finish()
        await bot.send_message(
            chat_id,
            "✅ Регистрация успешно завершена!\n\n"
            "Введите модель стекла (EN) или откройте меню.\n\n"
            f"⭐ Подписка: /subscribe или кнопка «{BTN_SUB}»",
            reply_markup=await create_menu_button()
        )

    @dp.message_handler(commands=["registration"])
    async def registration_cmd(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        info = await db_get_user_info(chat_id)
        if info:
            user_name, user_city, user_phone = info
            await bot.send_message(
                chat_id,
                f"✅ Вы зарегистрированы!\n"
                f"Имя: {user_name}\n"
                f"Город: {user_city}\n"
                f"Телефон: {user_phone}\n\n"
                f"Удалить данные: /delete_registration\n"
                f"Подписка: /subscribe\n"
                f"Статус: /status",
                reply_markup=await create_menu_button()
            )
        else:
            await bot.send_message(chat_id, "Здравствуйте!\nВведите свое имя для регистрации:")
            await UserRegistration.name.set()

    @dp.message_handler(lambda message: message.text == BTN_REG)
    async def registration_button_handler(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        await db_save_message(chat_id, message.text)

        info = await db_get_user_info(chat_id)
        if info:
            user_name, user_city, user_phone = info
            await bot.send_message(
                chat_id,
                f"✅ Вы зарегистрированы!\n"
                f"Имя: {user_name}\n"
                f"Город: {user_city}\n"
                f"Телефон: {user_phone}\n\n"
                f"Удалить данные: /delete_registration\n"
                f"Подписка: /subscribe\n"
                f"Статус: /status",
                reply_markup=await create_menu_button()
            )
        else:
            await bot.send_message(chat_id, "Здравствуйте!\nВведите свое имя для регистрации:")
            await UserRegistration.name.set()

    # ================== start/info ==================

    @dp.message_handler(commands=["start"])
    async def start_cmd(message: types.Message):
        chat_id = message.chat.id
        await db_save_message(chat_id, message.text)
        await db_ensure_user_exists(chat_id)

        info = await db_get_user_info(chat_id)
        if info:
            await send_message_with_ad(
                bot,
                chat_id,
                f"Привет👋, @{message.from_user.username}!\n"
                "Введите модель стекла (EN) или используйте меню.\n\n"
                f"⭐ Подписка: /subscribe • 📅 Статус: /status",
                reply_markup=await create_menu_button()
            )
        else:
            await send_message_with_ad(
                bot,
                chat_id,
                "Это бот для поиска взаимозаменяемых стекол.\n"
                "Для пользования ботом зарегистрируйтесь: /registration\n\n"
                f"⭐ Подписка: /subscribe • 📅 Статус: /status",
                reply_markup=await create_menu_button()
            )

    @dp.message_handler(lambda message: message.text == BTN_START)
    async def start_button_handler(message: types.Message):
        chat_id = message.chat.id
        await db_save_message(chat_id, message.text)

        info = await db_get_user_info(chat_id)
        if info:
            await bot.send_message(
                chat_id,
                f"Привет👋, @{message.from_user.username}\n"
                "Введите модель стекла (EN) или используйте меню.\n\n"
                f"⭐ Подписка: /subscribe • 📅 Статус: /status",
                reply_markup=await create_menu_button()
            )
        else:
            await bot.send_message(
                chat_id,
                "Это бот для поиска взаимозаменяемых стекол.\n"
                "Для пользования ботом зарегистрируйтесь: /registration\n\n"
                f"⭐ Подписка: /subscribe • 📅 Статус: /status",
                reply_markup=await create_menu_button()
            )

    @dp.message_handler(commands=["info"])
    async def handle_info(message: types.Message):
        await db_save_message(message.chat.id, message.text)

        info_text = (
            "🤖 <b>О боте</b>\n"
            "Этот бот помогает быстро находить взаимозаменяемые стёкла для переклейки.\n\n"
            "💳 <b>Почему бот стал платным?</b>\n"
            "База постоянно пополняется, хранение/хостинг и поддержка требуют затрат.\n"
            "Чтобы проект развивался, введена подписка ⭐.\n\n"
            "⭐ <b>Тарифы:</b>\n"
            f"• <b>1 месяц</b>: {PLAN_MONTH_PRICE}⭐ ({PLAN_MONTH_DAYS} дней)\n"
            f"• <b>1 год</b>: {PLAN_YEAR_PRICE}⭐ ({PLAN_YEAR_DAYS} дней)\n\n"
            "📌 <b>Команды</b>\n"
            "• /registration — <code>регистрация</code>\n"
            "• /delete_registration — <code>удалить свои данные</code>\n"
            "• /size — <code>подбор стекла по размерам</code>\n"
            "• /subscribe — <code>оформить подписку ⭐</code>\n"
            "• /status — <code>статус подписки</code>\n"
            "• /info — <code>справка</code>\n\n"
            "🛠 Если нашли ошибку — @expert_glass_lcd\n"
        )

        await bot.send_message(
            message.chat.id,
            info_text,
            parse_mode="html",
            reply_markup=await create_menu_button(),
            disable_web_page_preview=True,
        )

    @dp.message_handler(lambda message: message.text == BTN_INFO)
    async def info_button_handler(message: types.Message):
        await db_save_message(message.chat.id, message.text)
        await handle_info(message)

    # ================== /size ==================

    @dp.message_handler(commands=["size"])
    async def size_cmd(message: types.Message):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.row(types.KeyboardButton(BTN_SIZE, web_app=types.WebAppInfo(url=add_src(config.WEBAPP_URL, "cmd"))))
        kb.row(types.KeyboardButton(BTN_MENU))
        await message.answer(
            "🔎 <b>Подбор стекла по размерам</b>\n\n"
            f"Нажмите кнопку 👇 «{BTN_SIZE}».\n\n"
            f"Если передумали — нажмите «{BTN_MENU}».",
            parse_mode="html",
            reply_markup=kb
        )

    @dp.message_handler(lambda m: m.text == BTN_MENU)
    async def back_to_menu(message: types.Message):
        await message.answer("Меню:", reply_markup=await create_menu_button())

    @dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
    async def handle_size_webapp(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        info = await db_get_user_info(chat_id)
        if not info:
            await bot.send_message(
                chat_id,
                "Для пользования ботом зарегистрируйтесь: /registration",
                reply_markup=await create_menu_button(),
            )
            return

        try:
            data = json.loads(message.web_app_data.data)
            height = float(str(data.get("height", "")).replace(",", "."))
            width = float(str(data.get("width", "")).replace(",", "."))
            source = str(data.get("src", "unknown"))
        except Exception:
            await bot.send_message(
                chat_id,
                "Некорректный формат. Введите длину и ширину числами (можно с запятой).",
                reply_markup=await create_menu_button(),
            )
            return

        found = perform_size_search(height, width)
        await db_save_size_search(chat_id, height, width, len(found), source)

        if not found:
            await bot.send_message(
                chat_id,
                "🔘По указанным размерам ничего не найдено!\n"
                "🔘Попробуйте увеличить или уменьшить размер на 0,5мм"
            )
            await bot.send_message(chat_id, "Меню:", reply_markup=await create_menu_button())
            return

        subscribed = await db_is_subscribed(chat_id)

        await bot.send_message(
            chat_id,
            f"<em><u>Результаты для размеров {height}x{width}</u></em>",
            parse_mode="HTML"
        )

        dot = pretty_item_prefix()

        if subscribed:
            for g in found:
                model = g.get("model")
                photo_path = g.get("photo_path")
                caption = f"{dot} <b>Модель:</b> {model}"
                if photo_path and os.path.exists(photo_path):
                    with open(photo_path, "rb") as photo:
                        await bot.send_photo(chat_id, photo, caption=caption, parse_mode="HTML")
                else:
                    await bot.send_message(chat_id, caption, parse_mode="HTML")
        else:
            visible, _ = limit_results(found, subscribed, limit=1)
            if visible:
                g = visible[0]
                model = g.get("model")
                photo_path = g.get("photo_path")
                caption = f"{dot} <b>Модель:</b> {model}"
                if photo_path and os.path.exists(photo_path):
                    with open(photo_path, "rb") as photo:
                        await bot.send_photo(chat_id, photo, caption=caption, parse_mode="HTML")
                else:
                    await bot.send_message(chat_id, caption, parse_mode="HTML")

            hidden_count = max(len(found) - 1, 0)
            if hidden_count > 0:
                await bot.send_message(
                    chat_id,
                    build_masked_list(hidden_count, style="lottery") +
                    f"\n🔒 <b>Скрыто стекол:</b> {hidden_count}\n"
                    f"⭐ Откройте всё: /subscribe или кнопка «{BTN_SUB}»",
                    parse_mode="html"
                )

        await bot.send_message(chat_id, "Меню:", reply_markup=await create_menu_button())

    # ================== main text ==================

    @dp.message_handler()
    async def handle_text(message: types.Message, state: FSMContext):
        user_message = message.text
        if not user_message:
            return

        chat_id = message.chat.id
        user_message_lower = user_message.lower()

        await db_save_message(chat_id, user_message_lower)

        user_id = message.from_user.id
        if await db_is_user_blocked(user_id):
            await message.reply("Вы заблокированы и не можете использовать этого бота.")
            return

        if "galaxy" in user_message_lower:
            await bot.send_message(chat_id, "Повторите запрос не используя слово <b>galaxy</b>.", parse_mode="html")
            return
        if "realmi" in user_message_lower:
            await bot.send_message(chat_id, "❗️Исправте <u>realmi</u> на <b>realme</b>.", parse_mode="html")
            return
        if "techno" in user_message_lower:
            await bot.send_message(chat_id, "❗️Исправте <u>techno</u> на <b>tecno</b>.", parse_mode="html")
            return
        if "tehno" in user_message_lower:
            await bot.send_message(chat_id, "❗️Исправте <u>tehno</u> на <b>tecno</b>.", parse_mode="html")
            return
        if "+" in user_message_lower:
            await bot.send_message(chat_id, "❗️Знак <u>+</u> замените на слово <b>plus</b>.", parse_mode="html")
            return

        if re.search(r"[а-яё]", user_message_lower):
            await bot.send_message(chat_id, "Пожалуйста, пишите модель на <b>английском</b> языке.", parse_mode="html")
            return

        if not await db_get_user_info(chat_id):
            await bot.send_message(chat_id, "Для пользования ботом зарегистрируйтесь: /registration")
            return

        subscribed = await db_is_subscribed(chat_id)

        m1 = find_model_in_dataset(user_message_lower, glass_data)
        m2 = find_model_in_dataset(user_message_lower, glass_data2)
        m3 = find_model_in_dataset(user_message_lower, glass_data3)
        m4 = find_model_in_dataset(user_message_lower, glass_data4)
        m5 = find_model_in_dataset(user_message_lower, glass_data5)
        m6 = find_model_in_dataset(user_message_lower, glass_data6)
        m7 = find_model_in_dataset(user_message_lower, glass_data7)

        dot = pretty_item_prefix()

        # уточняющие списки (5 и 7)
        if m5:
            _, found_list = m5
            response = f"<em>Я знаю многое о продукции<b> {user_message}</b>. Укажите конкретную модель!</em>\n"
            if subscribed:
                kb = types.InlineKeyboardMarkup()
                photo_btn_idx = 0
                for item in found_list:
                    if isinstance(item, str) and item.lower().endswith(".png"):
                        lbl = alpha_label(photo_btn_idx)
                        title = "📷 Фото стекла" if not lbl else f"📷 Фото {lbl}"
                        photo_btn_idx += 1
                        kb.add(types.InlineKeyboardButton(title, callback_data=f"photo:{item}"))
                        response += f"\n{dot} <i>Фото стекла — кнопка ниже</i>"
                    else:
                        response += f"\n{dot} {item}"
                await bot.send_message(chat_id, response, parse_mode="html", reply_markup=kb)
                return

            visible, _ = limit_results(found_list, subscribed, limit=1)
            kb = types.InlineKeyboardMarkup()
            if visible:
                first = visible[0]
                if isinstance(first, str) and first.lower().endswith(".png"):
                    kb.add(types.InlineKeyboardButton("📷 Фото стекла", callback_data=f"photo:{first}"))
                    await bot.send_message(chat_id, response + f"\n{dot} <i>Фото стекла — кнопка ниже</i>", parse_mode="html", reply_markup=kb)
                else:
                    await bot.send_message(chat_id, response + f"\n{dot} {first}", parse_mode="html")

            hidden_glasses = count_hidden_glasses(found_list, visible_count=1)
            if hidden_glasses > 0:
                await bot.send_message(
                    chat_id,
                    build_masked_list(hidden_glasses, style="lottery") +
                    f"\n🔒 <b>Скрыто стекол:</b> {hidden_glasses}\n"
                    f"⭐ Откройте всё: /subscribe или кнопка «{BTN_SUB}»",
                    parse_mode="html"
                )
            return

        if m7:
            _, found_list = m7
            response = f"<em>Уточните, какая именно модель<b> {user_message}</b> Вас интересует?</em>\n"
            if subscribed:
                kb = types.InlineKeyboardMarkup()
                photo_btn_idx = 0
                for item in found_list:
                    if isinstance(item, str) and item.lower().endswith(".png"):
                        lbl = alpha_label(photo_btn_idx)
                        title = "📷 Фото стекла" if not lbl else f"📷 Фото {lbl}"
                        photo_btn_idx += 1
                        kb.add(types.InlineKeyboardButton(title, callback_data=f"photo:{item}"))
                        response += f"\n{dot} <i>Фото стекла — кнопка ниже</i>"
                    else:
                        response += f"\n{dot} {item}"
                await bot.send_message(chat_id, response, parse_mode="html", reply_markup=kb)
                return

            visible, _ = limit_results(found_list, subscribed, limit=1)
            kb = types.InlineKeyboardMarkup()
            if visible:
                first = visible[0]
                if isinstance(first, str) and first.lower().endswith(".png"):
                    kb.add(types.InlineKeyboardButton("📷 Фото стекла", callback_data=f"photo:{first}"))
                    await bot.send_message(chat_id, response + f"\n{dot} <i>Фото стекла — кнопка ниже</i>", parse_mode="html", reply_markup=kb)
                else:
                    await bot.send_message(chat_id, response + f"\n{dot} {first}", parse_mode="html")

            hidden_glasses = count_hidden_glasses(found_list, visible_count=1)
            if hidden_glasses > 0:
                await bot.send_message(
                    chat_id,
                    build_masked_list(hidden_glasses, style="lottery") +
                    f"\n🔒 <b>Скрыто стекол:</b> {hidden_glasses}\n"
                    f"⭐ Откройте всё: /subscribe или кнопка «{BTN_SUB}»",
                    parse_mode="html"
                )
            return

        def build_found_block(found_list: list):
            keyboard = types.InlineKeyboardMarkup()
            response = f"<em><u>Взаимозаменяемые стекла по запросу 🔍<b>'{user_message}'</b></u></em>\n"

            if subscribed:
                photo_btn_idx = 0
                for glass in found_list:
                    if isinstance(glass, str) and glass.lower().endswith(".png"):
                        lbl = alpha_label(photo_btn_idx)
                        title = "📷 Фото стекла" if not lbl else f"📷 Фото {lbl}"
                        photo_btn_idx += 1
                        keyboard.add(types.InlineKeyboardButton(title, callback_data=f"photo:{glass}"))
                        response += f"\n{dot} <i>Фото стекла — кнопка ниже</i>"
                    else:
                        response += f"\n{dot} {glass}"
                return response, keyboard

            visible, _ = limit_results(found_list, subscribed, limit=1)
            if visible:
                first = visible[0]
                if isinstance(first, str) and first.lower().endswith(".png"):
                    keyboard.add(types.InlineKeyboardButton("📷 Фото стекла", callback_data=f"photo:{first}"))
                    response += f"\n{dot} <i>Фото стекла — кнопка ниже</i>"
                else:
                    response += f"\n{dot} {first}"

            hidden_glasses = count_hidden_glasses(found_list, visible_count=1)
            if hidden_glasses > 0:
                response += "\n" + build_masked_list(hidden_glasses, style="lottery")
                response += (
                    f"\n🔒 <b>Скрыто стекол:</b> {hidden_glasses}\n"
                    f"⭐ Откройте всё: /subscribe или кнопка «{BTN_SUB}»"
                )

            return response, keyboard

        sent_any_results = False
        for m in (m1, m2, m3, m4, m6):
            if m:
                _, lst = m
                resp, kb = build_found_block(lst)
                await bot.send_message(chat_id, resp, reply_markup=kb, parse_mode="html")
                sent_any_results = True

        if sent_any_results:
            await bot.send_message(chat_id, "\n" + AD_TEXT, parse_mode="html", disable_web_page_preview=True)
            return

        await bot.send_message(
            chat_id,
            "<em><b>По Вашему запросу ничего не найдено!</b>\n\n"
            "1️⃣ Проверьте ошибки.\n"
            "2️⃣ Попробуйте полное название.\n\n"
            "🔎 <b>Можно подобрать по размерам</b>\n"
            f"«{BTN_SIZE}» или /size</em>\n\n"
            f"⭐ Подписка: /subscribe • 📅 Статус: /status",
            parse_mode="html",
            reply_markup=await create_menu_button(),
        )

    # ================== PHOTO CALLBACK ==================
    @dp.callback_query_handler(lambda query: query.data and query.data.startswith("photo:"))
    async def process_photo_callback(callback_query: types.CallbackQuery):
        photo_name = callback_query.data.split(":", 1)[1]
        possible_paths = [f"photos1/{photo_name}", f"photos/{photo_name}", photo_name]
        photo_path = next((p for p in possible_paths if os.path.exists(p)), None)

        src_text = ""
        try:
            src_text = callback_query.message.text or ""
        except Exception:
            src_text = ""

        glass_lines = extract_glasses_for_photo_caption(src_text)

        if glass_lines:
            caption = "<b>Фото стекла:</b>\n" + "\n".join(glass_lines)
        else:
            caption = "<b>Фото стекла</b>"

        if photo_path:
            with open(photo_path, "rb") as f:
                await bot.send_photo(
                    callback_query.from_user.id,
                    f,
                    caption=caption,
                    parse_mode="html",
                )
        else:
            await bot.send_message(callback_query.from_user.id, "Фото не найдено.")

        try:
            await callback_query.answer()
        except Exception:
            pass

    return bot, dp


class Command(BaseCommand):
    help = "Run Telegram bot (aiogram) inside Django"

    def handle(self, *args, **options):
        close_old_connections()
        bot, dp = build_bot()
        self.stdout.write(self.style.SUCCESS("🚀 Bot starting (Django + aiogram)..."))
        executor.start_polling(dp, skip_updates=False)