from pyrogram import Client, filters
from pyrogram.types import Message

from Knightsx import app  # Updated bot name

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(filters.command(["id", "stickerid", "stkid", "stckrid"]))
async def show_id(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = f"<b>ᴄʜᴀᴛ ɪᴅ</b>: <code>{message.chat.id}</code>\n"
        
        if message.reply_to_message:
            _id += f"<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: <code>{message.reply_to_message.from_user.id}</code>\n"
            file_info = get_id(message.reply_to_message)
        else:
            _id += f"<b>ᴜsᴇʀ ɪᴅ</b>: <code>{message.from_user.id}</code>\n"
            file_info = get_id(message)

        if file_info:
            _id += f"<b>{file_info.message_type}</b>: <code>{file_info.file_id}</code>\n"

        await message.reply_text(_id)
