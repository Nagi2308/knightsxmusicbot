import random
import re
import string

import lyricsgenius as lg
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS, lyrical
from strings import get_command
from Knightsx import app  # ✅ Changed from KnightsxX to Knightsx
from Knightsx.utils.decorators.language import language  # ✅ Updated path

# Command
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

# Genius API Setup
api_key = "JVv8pud-25QRBYyRwcH34AlAygySsSAU3owRNGBw6hXO96x0JiTMn-3R4PvsjcTf"
genius = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
genius.verbose = False


@app.on_message(filters.command(LYRICS_COMMAND) & ~filters.edited & ~BANNED_USERS)
@language
async def lrsearch(_, message: Message, _lang):
    if len(message.command) < 2:
        return await message.reply_text(_lang["lyrics_1"])
    
    title = message.text.split(None, 1)[1]
    response = await message.reply_text(_lang["lyrics_2"])
    
    song = genius.search_song(title, get_full_info=False)
    if song is None:
        return await response.edit(_lang["lyrics_3"].format(title))
    
    ran_hash = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    lyrics_text = song.lyrics

    if "Embed" in lyrics_text:
        lyrics_text = re.sub(r"\d*Embed", "", lyrics_text)

    lyrical[ran_hash] = lyrics_text

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_lang["L_B_1"],
                    url=f"https://t.me/{app.username}?start=lyrics_{ran_hash}",
                )
            ]
        ]
    )

    await response.edit(_lang["lyrics_4"], reply_markup=markup)
