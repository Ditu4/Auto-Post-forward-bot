import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "27060846")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "8f39072a61dbb296f38e4ff2b6cbe478")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6947386849:AAHy03YXoWwEW2hDOAQxCoSW-IjDhHso1G0")  # ⚠️ Required
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TzingBot")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb://localhost:27017")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/35175ab374c4a4f309bbb.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6065594762').split()]  # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Kdramaland')  # ⚠️ Required without [@]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001971176803"))  # ⚠️ Required

    
    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hello {} 👋,
━━━━━━━━━━━━━━━━━━━━━
Tʜɪs Bᴏᴛ Cᴀɴ Aᴜᴛᴏ Pᴏsᴛ Tᴏ Aʟʟ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aᴛ Oɴᴄᴇ
━━━━━━━━━━━━━━━━━━━━━
Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Bᴜᴛᴛᴏɴ & Mᴜʟᴛɪᴘʟᴇs Pᴏsᴛs & Mᴜʟᴛɪᴘʟᴇs Cʜᴀɴᴇʟs
"""

    ABOUT_TXT = """<b>
➥ ᴍy ɴᴀᴍᴇ : {}
➥ Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Snowball_Official>ѕησωвαℓℓ ❄️</a> 
➥ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Kdramaland>K-Lᴀɴᴅ</a>
➥ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
➥ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
➥ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
➥ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>
➥ ᴠᴇʀsɪᴏɴ : v1.0.0
"""

    HELP_TXT = """
Tʜɪs Bᴏᴛ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ Tᴏ Sᴇɴᴅ Pᴏsᴛs Tᴏ Yᴏᴜʀ Mᴜʟᴛɪᴘʟᴇ Cʜᴀɴɴᴇʟs

❗ Dᴇᴠᴇʟᴏᴘᴇʀ :- <a href=https://t.me/Snowball_official>ѕησωвαℓℓ ❄️</a>
"""

    STATS_TXT = """
╔════❰ sᴇʀᴠᴇʀ sᴛᴀᴛs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ ᴜᴩᴛɪᴍᴇ: `{0}`
║┣⪼ ᴛᴏᴛᴀʟ ᴅɪsᴋ sᴘᴀᴄᴇ: `{1}`
║┣⪼ ᴜsᴇᴅ: `{2} ({3}%)`
║┣⪼ ꜰʀᴇᴇ: `{4}`
║┣⪼ ᴄᴘᴜ: `{5}%`
║┣⪼ ʀᴀᴍ: `{6}%`
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪        
"""