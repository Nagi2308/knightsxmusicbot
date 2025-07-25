from pyrogram import filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from Knightsx import app  # Corrected to your bot structure


async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, message: Message):
    if (await app.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        bot_username = (await app.get_me()).username

        new = f"""
**✫** <b><u>#𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ</u></b> **✫**

**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}
**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ :** {username}
**𝐂ʜᴀᴛ 𝐈ᴅ :** `{chat_id}`
**𝐀ᴅᴅᴇᴅ 𝐁ʏ :** {added_by}
**𝐁ᴏᴛ :** @{bot_username}
"""
        await new_message(LOG_GROUP_ID, new)


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        removed_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        bot_username = (await app.get_me()).username

        left = f"""
**✫** <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> **✫**

**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}
**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ :** {username}
**𝐂ʜᴀᴛ 𝐈ᴅ :** `{chat_id}`
**𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ :** {removed_by}
**𝐁ᴏᴛ :** @{bot_username}
"""
        await new_message(LOG_GROUP_ID, left)
