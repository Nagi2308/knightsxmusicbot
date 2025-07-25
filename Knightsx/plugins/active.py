from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from Knightsx import app
from Knightsx.misc import SUDOERS
from Knightsx.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("📡 Fetching active voice chats...")
    served_chats = await get_active_chats()
    text = ""
    for i, chat_id in enumerate(served_chats, start=1):
        try:
            chat = await app.get_chat(chat_id)
            title = chat.title or "Private Chat"
            username = chat.username
        except Exception:
            title = "Private Chat"
            username = None

        if username:
            text += f"<b>{i}.</b> [{title}](https://t.me/{username}) [`{chat_id}`]\n"
        else:
            text += f"<b>{i}. {title}</b> [`{chat_id}`]\n"

    if not text:
        await mystic.edit_text("❌ No active voice chats found.")
    else:
        await mystic.edit_text(
            f"🎧 **Active Voice Chats List:**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("📡 Fetching active video chats...")
    served_chats = await get_active_video_chats()
    text = ""
    for i, chat_id in enumerate(served_chats, start=1):
        try:
            chat = await app.get_chat(chat_id)
            title = chat.title or "Private Chat"
            username = chat.username
        except Exception:
            title = "Private Chat"
            username = None

        if username:
            text += f"<b>{i}.</b> [{title}](https://t.me/{username}) [`{chat_id}`]\n"
        else:
            text += f"<b>{i}. {title}</b> [`{chat_id}`]\n"

    if not text:
        await mystic.edit_text("❌ No active video chats found.")
    else:
        await mystic.edit_text(
            f"🎥 **Active Video Chats List:**\n\n{text}",
            disable_web_page_preview=True,
        )
