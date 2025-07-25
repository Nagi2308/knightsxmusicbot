from pyrogram import filters
from pyrogram.types import Message
from Knightsx import app  # make sure 'app' is your bot Client

from config import BOT_ALIVE_MSG

@app.on_message(filters.command("alive"))
async def alive_handler(_, message: Message):
    await message.reply_text(BOT_ALIVE_MSG)
