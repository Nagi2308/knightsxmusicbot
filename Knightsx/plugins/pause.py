from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from Knightsx import app
from Knightsx.core.call import Knights
from Knightsx.utils.database import is_music_playing, music_off
from Knightsx.utils.decorators import AdminRightsCheck
from Knightsx.utils.inline import close_markup


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_music(client, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    
    await music_off(chat_id)
    await Knights.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention),
        reply_markup=close_markup(_)
    )
