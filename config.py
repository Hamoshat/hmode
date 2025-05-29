from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 20621590
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "a7e91275d681fefd4b2453b158b254ec"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUHrEmdGhOl2uP1D1ilRYlBIhd4pLHHI0rOhWuIos8tuOZ7ivP9chAL-sCJwuP8lG1pUq_81PYokPdirqhsti6MT_HCmd8V0cJdjSwIBs4LekL_QfmBMpsub3DFs94vU9DO2fNXNFWK8Bfvj28tv_ir9o3LntXS94SLCHd2bwqaKOcS8wZFvDZoe6AWbsgYCvf9r_tYrUSKdEWjGRVfmz3qonEO5fvQCQ2jyF1m_jftHjyq3LaFn1O2cz-CdUn8KRpsiS0XcgsZt1tyWBnJwYu--cqGpfT39hlGG-jtXy82MtmWgVT0ULYNa_LXzOTdf8JEaMFDlJyk-nAx4fFOvXZdg="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()