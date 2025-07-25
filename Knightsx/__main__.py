import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Knightsx import LOGGER, app, userbot
from Knightsx.core.call import KnightsX
from Knightsx.plugins import ALL_MODULES
from Knightsx.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("knightsx").error(
            "You need to add at least one Pyrogram STRING_SESSION!"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("knightsx").warning(
            "Spotify Client ID and Secret not provided. Spotify functionality may not work."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER("knightsx").warning(f"Failed to fetch banned users: {e}")

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("knightsx.plugins." + all_module)
    LOGGER("knightsx.plugins").info(
        "All modules imported successfully."
    )
    await userbot.start()
    await KnightsX.start()
    await KnightsX.decorators()
    LOGGER("knightsx").info("KnightsX Music Bot Started Successfully")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("knightsx").info("Stopping KnightsX Music Bot...")
