from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from Knightsx import app  # updated import
from Knightsx.misc import SUDOERS
from Knightsx.utils import help_pannel
from Knightsx.utils.database import get_lang, is_commanddelete_on
from Knightsx.utils.decorators.language import LanguageStart, languageCB
from Knightsx.utils.inline.help import help_back_markup, private_help_panel

# Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND) & filters.private & ~filters.edited & ~BANNED_USERS
)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(_["help_1"], reply_markup=keyboard)
        else:
            await update.edit_message_text(_["help_1"], reply_markup=keyboard)
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(chat_id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["help_1"],
            reply_markup=keyboard,
        )


@app.on_message(
    filters.command(HELP_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["help_2"],
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)

    if cb == "hb9":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "Bsdk Tuje kisne sudo banaya, Bkk ja sale", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_9, reply_markup=keyboard
            )
            return await CallbackQuery.answer()

    try:
        await CallbackQuery.answer()
    except:
        pass

    help_sections = {
        "hb1": helpers.HELP_1,
        "hb2": helpers.HELP_2,
        "hb3": helpers.HELP_3,
        "hb4": helpers.HELP_4,
        "hb5": helpers.HELP_5,
        "hb6": helpers.HELP_6,
        "hb7": helpers.HELP_7,
        "hb8": helpers.HELP_8,
        "hb10": helpers.HELP_10,
        "hb11": helpers.HELP_11,
        "hb12": helpers.HELP_12,
        "hb13": helpers.HELP_13,
    }

    if cb in help_sections:
        await CallbackQuery.edit_message_text(
            help_sections[cb], reply_markup=keyboard
        )
