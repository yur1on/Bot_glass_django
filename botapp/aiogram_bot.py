import asyncio
import json
import os
import re

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, RetryAfter, UserDeactivated

from django.conf import settings

from .services import (
    is_user_blocked,
    get_user_info,
    get_all_chat_ids,
    save_message,
    save_size_search,
    AD_TEXT,
    BELARUSIAN_CITIES,
)

# импорт данных как у тебя
from baza import (
    glass_data, glass_data2, glass_data3, glass_data4,
    glass_data5, glass_data6, glass_data7
)
from baza2 import glass_data9

def add_src(url: str, src: str) -> str:
    return f"{url}&src={src}" if "?" in url else f"{url}?src={src}"

# --- BOT/DP ---
if not settings.BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is empty. Set BOT_TOKEN in env.")

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# ----------------- Меню -----------------
async def create_menu_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    start_button = types.KeyboardButton('🚀 start')
    registration_button = types.KeyboardButton('🗂registration')
    help_button = types.KeyboardButton('ℹ️ Info')

    size_button = types.KeyboardButton(
        '🔎подбор стекла по размеру',
        web_app=types.WebAppInfo(url=add_src(settings.WEBAPP_URL, "menu"))
    )
    markup.add(start_button, registration_button, help_button)
    markup.add(size_button)
    return markup

# ----------------- Регистрация -----------------
class UserRegistration(StatesGroup):
    name = State()
    city = State()
    phone_number = State()

# Django ORM import тут, чтобы не грузить до настройки Django
from .models import User, BlockedUser

@dp.message_handler(commands=['block'], user_id=settings.ADMIN_ID)
async def block_user(message: types.Message):
    try:
        user_id_to_block = int(message.text.split()[1])
        BlockedUser.objects.get_or_create(user_id=user_id_to_block)
        await message.reply(f"Пользователь с ID {user_id_to_block} заблокирован.")
    except (IndexError, ValueError):
        await message.reply("Используйте команду в формате: /block <user_id>")

@dp.message_handler(commands=['unblock'], user_id=settings.ADMIN_ID)
async def unblock_user_command(message: types.Message):
    try:
        user_id_to_unblock = int(message.text.split()[1])
        BlockedUser.objects.filter(user_id=user_id_to_unblock).delete()
        await message.reply(f"Пользователь с ID {user_id_to_unblock} разблокирован.")
    except (IndexError, ValueError):
        await message.reply("Используйте команду в формате: /unblock <user_id>")

# ✅ рассылка всем
async def send_to_all_users(bot_instance, message_text: str):
    chat_ids = get_all_chat_ids()
    ok = 0
    fail = 0

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
            except Exception:
                fail += 1
        except (BotBlocked, ChatNotFound, UserDeactivated):
            fail += 1
        except Exception:
            fail += 1

    return ok, fail

@dp.message_handler(commands=['send1'])
async def send1_command(message: types.Message):
    if message.from_user.id != settings.ADMIN_ID:
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

@dp.message_handler(commands=['delete_registration'])
async def delete_registration(message: types.Message):
    chat_id = message.chat.id
    User.objects.filter(chat_id=chat_id).delete()
    await bot.send_message(chat_id, "Ваши регистрационные данные успешно удалены. Для повторной регистрации используйте команду /registration")

@dp.message_handler(commands=['size'])
async def size_cmd(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(
        types.KeyboardButton(
            "🔎подбор стекла по размеру",
            web_app=types.WebAppInfo(url=add_src(settings.WEBAPP_URL, "cmd"))
        )
    )
    kb.add(types.KeyboardButton("↩️ В меню"))

    await message.answer(
        "🔎 <b>Подбор стекла по размерам</b>\n\n"
        "Нажмите кнопку 👇 «🔎подбор стекла по размеру».\n\n"
        "Если передумали — нажмите «↩️ В меню».",
        parse_mode="html",
        reply_markup=kb
    )

@dp.message_handler(lambda m: m.text == "↩️ В меню")
async def back_to_menu(message: types.Message):
    await message.answer("Меню:", reply_markup=await create_menu_button())

@dp.message_handler(state=UserRegistration.name)
async def register_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await UserRegistration.city.set()
    await bot.send_message(message.chat.id, "Введите Ваш город:", reply_markup=await create_menu_button())

@dp.message_handler(lambda message: message.text.isdigit(), state=UserRegistration.city)
async def register_invalid_city(message: types.Message):
    await bot.send_message(message.chat.id, "Некорректно введен город!")

@dp.message_handler(state=UserRegistration.city)
async def register_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await UserRegistration.phone_number.set()
    await bot.send_message(message.chat.id, "Введите Ваш номер телефона:")

@dp.message_handler(lambda message: not message.text.isdigit(), state=UserRegistration.phone_number)
async def register_invalid_phone(message: types.Message):
    await bot.send_message(message.chat.id, "Номер телефона должен содержать только цифры. Пожалуйста, введите корректный номер телефона.")

@dp.message_handler(lambda message: message.text.isdigit(), state=UserRegistration.phone_number)
async def register_phone_number(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_data = await state.get_data()
    name = user_data.get("name")
    city = user_data.get("city")
    phone_number = message.text

    User.objects.update_or_create(
        chat_id=chat_id,
        defaults={"name": name, "city": city, "phone_number": phone_number},
    )

    await state.finish()
    await bot.send_message(
        chat_id,
        "Регистрация успешно завершена!\n\nВведите модель стекла телефона или планшета, которое вы ищите.\n\n Изучите информацию и откройте доп. кнопки 👉 /info"
    )

@dp.message_handler(commands=['registration'])
async def registration_cmd(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    info = get_user_info(chat_id)
    if info:
        user_name, user_city, user_phone = info
        await bot.send_message(
            chat_id,
            f"Вы зарегистрированы! \nВаше имя: {user_name}\nВаш город: {user_city}\nВаш № тел.: {user_phone}\n\nДля удаления регистрационных данных введите команду /delete_registration"
        )
    else:
        await bot.send_message(chat_id, "Здравствуйте!\nВведите свое имя для регистрации:")
        await UserRegistration.name.set()

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    chat_id = message.chat.id
    await save_message(chat_id, message.text)

    info = get_user_info(chat_id)
    if info:
        await bot.send_message(
            chat_id,
            f"Привет👋, @{message.from_user.username}!\n Введите модель стекла телефона или планшета, которое вы ищете.\n Изучите информацию и откройте доп. кнопки 👉 /info\n\nmobirazbor.by",
            parse_mode="html",
        )
    else:
        await bot.send_message(
            chat_id,
            "Это бот для поиска взаимозаменяемых стекол для переклейки.\nДля пользования ботом, пожалуйста, зарегистрируйтесь! Используйте команду /registration\n\nmobirazbor.by",
            parse_mode="html",
            reply_markup=await create_menu_button()
        )

@dp.message_handler(commands=['info'])
async def handle_info(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "🤖 Я бот для поиска взаимозаменяемых моделей стекол телефонов и планшетов.\n\n"
        "✔️Для поиска взаимозаменяемых стекол отправьте сообщение нужной модели\n\n"
        "✔️Для подбора стекла по размерам: кнопка «🔎подбор стекла по размеру» или команда /size\n\n"
        "✔️/registration - команда для регистрации\n\n"
        "✔️/delete_registration - команда для удаления своих регистрационных данных из базы\n\n"
        "✔️Если нашли ошибку или знаете взаимозаменяемую модель стекла, напишите пожалуйста @expert_glass_lcd \n",
        reply_markup=await create_menu_button()
    )

@dp.message_handler(lambda message: message.text == 'ℹ️ Info')
async def info_button_handler(message: types.Message):
    save_message(message.chat.id, message.text)
    await handle_info(message)

@dp.message_handler(lambda message: message.text == '🚀 start')
async def start_button_handler(message: types.Message):
    save_message(message.chat.id, message.text)
    info = get_user_info(message.chat.id)
    if info:
        await bot.send_message(
            message.chat.id,
            f"Привет👋, @{message.from_user.username}\n Введите модель стекла телефона или планшета, которое вы ищете.\n Изучите информацию и откройте доп. кнопки 👉 /info"
        )
    else:
        await bot.send_message(
            message.chat.id,
            "Это бот для поиска взаимозаменяемых стекол для переклейки.\nДля пользования ботом, пожалуйста, зарегистрируйтесь! Используйте команду /registration"
        )

@dp.message_handler(lambda message: message.text == '🗂registration')
async def registration_button_handler(message: types.Message, state: FSMContext):
    save_message(message.chat.id, message.text)
    await registration_cmd(message, state)

# ----------------- WebApp size -----------------
def perform_size_search(height, width):
    found = []
    for glass9 in glass_data9:
        try:
            if float(glass9.get("height")) == float(height) and float(glass9.get("width")) == float(width):
                found.append({"model": glass9.get("model"), "photo_path": glass9.get("photo_path")})
        except Exception:
            continue
    return found

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def handle_size_webapp(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    info = get_user_info(chat_id)
    if not info:
        await bot.send_message(
            chat_id,
            "Для пользования ботом пожалуйста зарегистрируйтесь! \nИспользуйте команду 👉  /registration",
            reply_markup=await create_menu_button()
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
            reply_markup=await create_menu_button()
        )
        return

    found = perform_size_search(height, width)
    save_size_search(chat_id, height, width, len(found), source)

    if found:
        await bot.send_message(chat_id, f"<em><u>Стекла по размерам {height}x{width} найдено:</u></em>", parse_mode="HTML")
        for item in found:
            model = item.get("model")
            photo_path = item.get("photo_path")
            if photo_path and os.path.exists(photo_path):
                with open(photo_path, "rb") as photo:
                    await bot.send_photo(chat_id, photo, caption=f"<b>Модель:</b> {model}", parse_mode="HTML")
            else:
                await bot.send_message(chat_id, f"<b>Модель:</b> {model}", parse_mode="HTML")
    else:
        await bot.send_message(
            chat_id,
            "🔘По указанным размерам ничего не найдено!\n"
            "🔘Попробуйте увеличить или уменьшить размер в запросе на 0,5мм"
        )

    await bot.send_message(chat_id, "Меню:", reply_markup=await create_menu_button())

# ----------------- Основной текстовый обработчик -----------------
@dp.message_handler()
async def handle_text(message: types.Message, state: FSMContext):
    user_message = message.text
    if not user_message:
        return

    chat_id = message.chat.id
    user_message_lower = user_message.lower()

    save_message(chat_id, user_message_lower)

    user_id = message.from_user.id
    if is_user_blocked(user_id):
        await message.reply("Вы заблокированы и не можете использовать этого бота.")
        return

    if 'galaxy' in user_message_lower:
        await bot.send_message(chat_id, "Повторите пожалуйста запрос не используя слово <b>galaxy</b>.", parse_mode='html')
        return
    if 'realmi' in user_message_lower:
        await bot.send_message(chat_id, "❗️Исправте в запросе слово <u>realmi</u> на правильное написание <b>realme</b>.", parse_mode='html')
        return
    if 'techno' in user_message_lower:
        await bot.send_message(chat_id, "❗️Исправте в запросе слово <u>techno</u> на правильное написание <b>tecno</b>.", parse_mode='html')
        return
    if 'tehno' in user_message_lower:
        await bot.send_message(chat_id, "❗️Исправте в запросе слово <u>tehno</u> на правильное написание <b>tecno</b>.", parse_mode='html')
        return
    if '+' in user_message_lower:
        await bot.send_message(chat_id, "❗️Исправте в запросе знак <u>+</u> на слово <b>plus</b>.", parse_mode='html')
        return

    if re.search(r"[а-яё]", user_message_lower):
        await bot.send_message(chat_id, "Пожалуйста, пишите модель на <b>английском</b> языке.", parse_mode="html")
        return

    if not get_user_info(chat_id):
        await bot.send_message(chat_id, "Для пользования ботом пожалуйста зарегистрируйтесь! \nИспользуйте команду 👉  /registration ")
        return

    found_glasses = []
    found_glasses2 = []
    found_glasses3 = []
    found_glasses4 = []
    found_glasses5 = []
    found_glasses6 = []
    found_glasses7 = []

    for model, glasses in glass_data:
        if user_message_lower == model.lower():
            found_glasses = glasses
            break
    for model, glasses in glass_data2:
        if user_message_lower == model.lower():
            found_glasses2 = glasses
            break
    for model, glasses in glass_data3:
        if user_message_lower == model.lower():
            found_glasses3 = glasses
            break
    for model, glasses in glass_data4:
        if user_message_lower == model.lower():
            found_glasses4 = glasses
            break
    for model, glasses in glass_data5:
        if user_message_lower == model.lower():
            found_glasses5 = glasses
            break
    for model, glasses in glass_data6:
        if user_message_lower == model.lower():
            found_glasses6 = glasses
            break
    for model, glasses in glass_data7:
        if user_message_lower == model.lower():
            found_glasses7 = glasses
            break

    if found_glasses5:
        response = f"<em>Я знаю многое о продукции<b> {user_message}</b>. Укажите конкретную модель!</em>\n"
        response += "\n".join(found_glasses5)
        await bot.send_message(chat_id, response, parse_mode='html')
        return

    if found_glasses7:
        response = f"<em>Уточните, какая именно модель<b> {user_message}</b> Вас интересует?</em>\n"
        response += "\n".join(found_glasses7)
        await bot.send_message(chat_id, response, parse_mode='html')
        return

    def build_found_block(found_list):
        keyboard = types.InlineKeyboardMarkup()
        response = f"<em><u>Взаимозаменяемые стекла по поиску 🔍<b>'{user_message}'</b> найдено:</u></em>\n"
        for index, glass in enumerate(found_list):
            if isinstance(glass, str) and glass.lower().endswith(".png") and index == len(found_list) - 1:
                photo_name = glass
                keyboard.add(types.InlineKeyboardButton("Посмотреть фото стекла", callback_data=f"photo:{photo_name}"))
            else:
                response += f"{glass}\n"
        return response, keyboard

    sent_any = False

    for lst in (found_glasses, found_glasses2, found_glasses3, found_glasses4, found_glasses6):
        if lst:
            resp, kb = build_found_block(lst)
            await bot.send_message(chat_id, resp, reply_markup=kb, parse_mode='html')
            sent_any = True

    if sent_any:
        await bot.send_message(chat_id, "\n" + AD_TEXT, parse_mode="html", disable_web_page_preview=True)
        return

    await bot.send_message(
        chat_id,
        "<em><b>По Вашему запросу ничего не найдено!</b>\n\n"
        "1️⃣ Проверьте ошибки при написании модели.\n"
        "2️⃣ Попробуйте ввести полное название модели.\n\n"
        "🔎 <b>Вы можете подобрать стекло по размерам</b>\n"
        "👇 <b>нажмите кнопку внизу меню</b>\n"
        "«🔎подбор стекла по размеру»\n"
        "или команда /size</em>",
        parse_mode="html",
        reply_markup=await create_menu_button()
    )

@dp.callback_query_handler(lambda query: query.data and query.data.startswith('photo:'))
async def process_photo_callback(callback_query: types.CallbackQuery):
    photo_name = callback_query.data.split(':', 1)[1]
    possible_paths = [f"photos1/{photo_name}", f"photos/{photo_name}", photo_name]
    photo_path = next((p for p in possible_paths if os.path.exists(p)), None)

    query_text = callback_query.message.text or ""

    if photo_path:
        lines = [ln.strip() for ln in query_text.splitlines()]
        found_lines = [ln for ln in lines[1:] if ln]
        photo_caption = "<b>Фото стекла:</b>\n" + "\n".join(found_lines) if found_lines else "<b>Фото стекла</b>"

        await bot.send_photo(
            callback_query.from_user.id,
            open(photo_path, 'rb'),
            caption=photo_caption,
            parse_mode='html'
        )
    else:
        await bot.send_message(callback_query.from_user.id, "Фото не найдено.")