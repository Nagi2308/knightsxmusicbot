import socket
import time

import heroku3
from pyrogram import filters, Client
from config import API_HASH, API_ID, BOT_TOKEN
import config
from Knightsx.core.mongo import pymongodb

from .logger import LOGGER

# Initialize the main Pyrogram bot client
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "knightsx.plugins"},
)

SUDOERS = filters.user()
HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/", "@", ".", "com", ":", "git", "heroku", "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD", "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info("Database Initialized.")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = pymongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info("Sudoers Loaded.")


def heroku():
    global HAPP
    if is_heroku():
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info("Heroku App Configured Successfully.")
            except BaseException:
                LOGGER(__name__).warning(
                    "Please check your Heroku API Key and App name configuration."
                )
