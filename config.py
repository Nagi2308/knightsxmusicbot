import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def get_int_env(var_name, default=None):
    val = getenv(var_name)
    try:
        return int(val.strip()) if val is not None else default
    except (ValueError, AttributeError):
        raise SystemExit(f"[ERROR] - '{var_name}' must be a valid integer.")

# Telegram Credentials
API_ID = get_int_env("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Logger
LOGGER_ID = get_int_env("LOGGER_ID", -1002824817308)

# Bot Identity
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "KnightsXMusic")

# ✅ Alive Message (use in bot reply or logs)


# config.py

BOT_ALIVE_MSG = "✅ KnightsX Music Bot is Alive and Working!"

# Owners
OWNER_ID = list(map(int, getenv("OWNER_ID", "6840435225").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6840435225").split()))

# Usernames
GROUP_USERNAME = getenv("GROUP_USERNAME")
CHANNEL_USERNAME = getenv("CHANNEL_USERNAME")

# Heroku
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Nagi2308/Knightsxbots/blob/main/README.md")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KnightsXbots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Knightxbotsupport")

# Limits
DURATION_LIMIT_MIN = get_int_env("DURATION_LIMIT", 5000)
SONG_DOWNLOAD_DURATION = get_int_env("SONG_DOWNLOAD_DURATION_LIMIT", 1000)
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = get_int_env("ASSISTANT_LEAVE_TIME", 5400)
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = get_int_env("YOUTUBE_EDIT_SLEEP", 5)
TELEGRAM_DOWNLOAD_EDIT_SLEEP = get_int_env("TELEGRAM_EDIT_SLEEP", 3)

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Streaming
VIDEO_STREAM_LIMIT = get_int_env("VIDEO_STREAM_LIMIT", 300)
SERVER_PLAYLIST_LIMIT = get_int_env("SERVER_PLAYLIST_LIMIT", 500)
PLAYLIST_FETCH_LIMIT = get_int_env("PLAYLIST_FETCH_LIMIT", 50)

# Cleanmode
CLEANMODE_DELETE_MINS = get_int_env("CLEANMODE_MINS", 60)

# File Size
TG_AUDIO_FILESIZE_LIMIT = get_int_env("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = get_int_env("TG_VIDEO_FILESIZE_LIMIT", 1073741824)

# String Sessions
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# Internal
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Default Images
DEFAULT_IMG = "https://files.catbox.moe/g1x308.jpg"
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/vvvlte.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", DEFAULT_IMG)
PLAYLIST_IMG_URL = DEFAULT_IMG
GLOBAL_IMG_URL = DEFAULT_IMG
STATS_IMG_URL = DEFAULT_IMG
TELEGRAM_AUDIO_URL = DEFAULT_IMG
TELEGRAM_VIDEO_URL = DEFAULT_IMG
STREAM_IMG_URL = DEFAULT_IMG
SOUNCLOUD_IMG_URL = DEFAULT_IMG
YOUTUBE_IMG_URL = DEFAULT_IMG
SPOTIFY_ARTIST_IMG_URL = DEFAULT_IMG
SPOTIFY_ALBUM_IMG_URL = DEFAULT_IMG
SPOTIFY_PLAYLIST_IMG_URL = DEFAULT_IMG

# Time conversion
def time_to_seconds(time):
    return sum(int(x) * 60**i for i, x in enumerate(reversed(str(time).split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL.strip()):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with http:// or https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT.strip()):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with http:// or https://")


BOT_ALIVE_MSG = (
    "✅ Bot is alive!\n"
    "Thank you for using KnightsxMusic 🎧"
)

