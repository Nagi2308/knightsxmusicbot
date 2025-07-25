from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from Knightsx import app
from Knightsx.utils.database import get_loop, set_loop
from Knightsx.utils.inline import close_markup
from Knightsx.utils.decorators import AdminRightsCheck
from Knightsx.utils.decorators.language import language


@app.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@language
@AdminRightsCheck
async def loop_command(_, message: Message, lang, chat_id):
    usage = lang["admin_17"]

    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip()

    if state.isnumeric():
        state = int(state)
        current = await get_loop(chat_id)
        if current != 0:
            state = current + state
        if state > 10:
            state = 10
        await set_loop(chat_id, state)
        return await message.reply_text(
            text=lang["admin_18"].format(state, message.from_user.mention),
            reply_markup=close_markup(lang),
        )

    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            text=lang["admin_18"].format(state, message.from_user.mention),
            reply_markup=close_markup(lang),
        )

    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(
            lang["admin_19"].format(message.from_user.mention),
            reply_markup=close_markup(lang),
        )

    else:
        return await message.reply_text(usage)
