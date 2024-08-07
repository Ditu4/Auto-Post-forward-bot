import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "21288218")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7189281451:AAG87oKZ5UFtRAkb3NvnO0zmNze7MQ63ObE")  # ⚠️ Required
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "K_AutoPostBot")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb://localhost:27017")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e30efcd2b42b81749996c.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6065594762').split()]  # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Kdramaland') # ⚠️ Required without [@]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002023195189"))  # ⚠️ Required

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
➥ Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Ditu ❄️</a> 
➥ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Lᴀɴᴅ</a>
➥ Lɪʙʀᴀʀy : <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Pyʀᴏɢʀᴀᴍ</a>
➥ Lᴀɴɢᴜᴀɢᴇ: <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Pyᴛʜᴏɴ 3</a>
➥ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Mᴏɴɢᴏ DB</a>
➥ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Heroku</a>
➥ ᴠᴇʀsɪᴏɴ : v1.0.0
"""

    HELP_TXT = """
Tʜɪs Bᴏᴛ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ Tᴏ Sᴇɴᴅ Pᴏsᴛs Tᴏ Yᴏᴜʀ Mᴜʟᴛɪᴘʟᴇ Cʜᴀɴɴᴇʟs

❗ Dᴇᴠᴇʟᴏᴘᴇʀ :- <a href=https://t.me/+7Ft-A0Nl0QE5OTFl>Ditu ❄️</a>
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


class temp(object):

    POST_ID = {}
    STORE_DATA = {}
    BOOL_ADDPOST = {}
