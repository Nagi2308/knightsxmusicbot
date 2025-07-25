from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from Knightsx import app
from Knightsx.misc import SUDOERS
from Knightsx.utils.database import autoend_off, autoend_on
from Knightsx.utils.decorators.language import language

# Command
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
@language
async def auto_end_stream(client, message: Message, _):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    
    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip().lower()

    if state == "enable":
        await autoend_on()
        return await message.reply_text(
            _["autoend_enabled"]
            if "autoend_enabled" in _
            else "✅ **Auto-End Enabled**\n\nThe assistant will automatically leave the video chat after a short period of inactivity."
        )
    elif state == "disable":
        await autoend_off()
        return await message.reply_text(
            _["autoend_disabled"]
            if "autoend_disabled" in _
            else "❌ **Auto-End Disabled**\n\nThe assistant will remain in the call until manually stopped."
        )
    else:
        return await message.reply_text(usage)
