import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "user_database.db"

# токен: по-хорошему хранить в env, но пока оставим как есть
# tok = os.getenv("BOT_TOKEN", "6719595706:AAFbFJCJaB10rqwri7x_3WAuwvFSNLUtNDE")
tok = os.getenv("BOT_TOKEN", "6836113072:AAFdU2EZAOyEsCqCSrelFnR1DR9wEpoICAs")

# test
# tok = os.getenv("BOT_TOKEN", "8779197289:AAHUoYDSD_0xASU7Kwi7XjMp_8jHnyPuoCY")

ADMIN_ID = 486747175
WEBAPP_URL = "https://yur1on.github.io/tg-size-webapp/"
# YooMoney
YOOMONEY_WALLET = "4100118591872654"
YOOMONEY_NOTIFICATION_SECRET = "EpywSdxj2mJ96VNfINcQL61t"
# лог для старта
print("🗄 Using DB:", DB_PATH)