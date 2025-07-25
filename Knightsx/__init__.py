from Knightsx.core.bot import KnightsXBot
from Knightsx.core.git import git
from Knightsx.core.userbot import Userbot
from Knightsx.misc import dbb, heroku

from .logger import LOGGER

# Initialize directories and services
git()
dbb()
heroku()

# Bot and userbot clients
app = KnightsXBot()
userbot = Userbot()

# Import platform APIs
from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
