from asgiref.sync import sync_to_async
from .models import User, Message, BlockedUser, SizeSearch

BELARUSIAN_CITIES = [
    "minsk", "минск", "grodno", "гродно", "brest", "брест", "vitebsk", "витебск",
    "mogilev", "могилев", "gomel", "гомель", "baranovichi", "барановичи",
    "bobruisk", "бобруйск", "borisov", "борисов", "pinsk", "пинск", "orsha", "орша",
    "mozyr", "мозырь", "soligorsk", "солигорск", "lida", "лида", "novopolotsk", "новополоцк",
    "polotsk", "полоцк",
]

AD_TEXT = (
    '<b>Для жителей РБ 🇧🇾</b>\n'
    'Сервис для разборщиков мобильной техники.\n'
    'Канал: <a href="https://t.me/MobiraRazbor">@MobiraRazbor</a>\n'
    'Чат: <a href="https://t.me/mobirazbor_chat">@mobirazbor_chat</a>\n'
    'Сайт: <a href="https://mobirazbor.by">mobirazbor.by</a>'
)

# ---------------- SYNC (если надо в sync контексте) ----------------

def is_user_blocked_sync(user_id: int) -> bool:
    return BlockedUser.objects.filter(user_id=user_id).exists()

def get_user_info_sync(chat_id: int):
    u = User.objects.filter(chat_id=chat_id).first()
    if not u:
        return None
    return (u.name, u.city, u.phone_number)

def get_all_chat_ids_sync():
    return list(User.objects.values_list("chat_id", flat=True))

def get_belarusian_chat_ids_sync():
    ids = []
    for chat_id, city in User.objects.values_list("chat_id", "city"):
        if city and city.lower() in BELARUSIAN_CITIES:
            ids.append(chat_id)
    return ids

def save_message_sync(chat_id: int, text: str):
    Message.objects.create(chat_id=chat_id, message_text=text)

def save_size_search_sync(chat_id: int, height: float, width: float, found_count: int, source: str = "unknown"):
    SizeSearch.objects.create(
        chat_id=int(chat_id),
        height=float(height),
        width=float(width),
        found_count=int(found_count),
        source=str(source)[:64],
    )

# ---------------- ASYNC wrappers (для aiogram) ----------------

is_user_blocked = sync_to_async(is_user_blocked_sync, thread_sensitive=True)
get_user_info = sync_to_async(get_user_info_sync, thread_sensitive=True)
get_all_chat_ids = sync_to_async(get_all_chat_ids_sync, thread_sensitive=True)
get_belarusian_chat_ids = sync_to_async(get_belarusian_chat_ids_sync, thread_sensitive=True)
save_message = sync_to_async(save_message_sync, thread_sensitive=True)
save_size_search = sync_to_async(save_size_search_sync, thread_sensitive=True)