import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MausamMusic import LOGGER, app, userbot
from MausamMusic.core.call import Mausam
from MausamMusic.misc import sudo
from MausamMusic.plugins import ALL_MODULES
from MausamMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        sys.exit(1)

    await sudo()
    
    try:
        users = await get_gbanned()
        BANNED_USERS.update(users)

        users = await get_banned_users()
        BANNED_USERS.update(users)
    except Exception as e:
        LOGGER("MausamMusic").warning(f"Failed to fetch banned users: {e}")

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module(f"MausamMusic.plugins.{all_module}")

    LOGGER("MausamMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Mausam.start()

    try:
        await Mausam.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("MausamMusic").error("Please turn on the video chat in your log group/channel.\n\nStopping Bot...")
        sys.exit(1)
    except Exception as e:
        LOGGER("MausamMusic").warning(f"Failed to start stream call: {e}")

    await Mausam.decorators()
    
    LOGGER("MausamMusic").info("MausamMusic Started Successfully.\n\nDon't forget to visit @MausamMods")

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("MausamMusic").info("Stopping Mausam Music Bot...")


if __name__ == "__main__":
    asyncio.run(init())