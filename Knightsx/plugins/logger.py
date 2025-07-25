from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from Knightsx import app
from Knightsx.misc import SUDOERS
from Knightsx.utils.database import add_off, add_on
from Knightsx.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(_, message: Message, lang):
    usage = lang["log_1"]

    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.command[1].lower()

    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(lang["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(lang["log_3"])
    else:
        await message.reply_text(usage)
