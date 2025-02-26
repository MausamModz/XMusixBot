from MausamMusic.core.bot import Mausam
from MausamMusic.core.dir import dirr
from MausamMusic.core.git import git
from MausamMusic.core.userbot import Userbot
from MausamMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Mausam()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
