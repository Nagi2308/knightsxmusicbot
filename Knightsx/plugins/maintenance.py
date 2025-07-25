from pyrogram import filters
from pyrogram.types import Message

from strings import get_command, get_string
from Knightsx import app
from Knightsx.misc import SUDOERS
from Knightsx.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on
)
from Knightsx.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip().lower()

    if state == "enable":
        if await is_maintenance():
            return await message.reply_text("ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")
        await maintenance_on()
        return await message.reply_text(_["maint_2"])

    elif state == "disable":
        if not await is_maintenance():
            return await message.reply_text("ɪ ᴅᴏɴ'ᴛ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ᴇɴᴀʙʟᴇᴅ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ.")
        await maintenance_off()
        return await message.reply_text(_["maint_3"])

    else:
        return await message.reply_text(usage)
