import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from Knightsx import app
from Knightsx.utils.formatters import time_to_seconds


def generate_progress_bar(percentage):
    if percentage <= 2:
        return "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    bar_styles = [
        "ﮩ٨ـﮩﮩ٨ـﮩ٨ـ⛨ﮩ٨ـ",
        "ﮩ٨ـﮩﮩ٨ـ⛨ﮩ٨ـﮩﮩ٨ـ",
        "ﮩ٨ـﮩ⛨ﮩ٨ـﮩ٨ـﮩﮩ٨ـ",
        "ﮩ⛨٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    ]
    index = int((percentage % 100) / 25)
    return bar_styles[index]


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bar = generate_progress_bar(percentage)

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="☆", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="★ ᴄʜᴀᴛ ɢʀᴏᴜᴘ ★", url="https://t.me/Knightxbotsupport"),
        ],
        [
            InlineKeyboardButton(text="《 10", callback_data=f"ADMIN 1|{chat_id}"),
            InlineKeyboardButton(text="𓆩✧ ᴄʟᴏsᴇ ✧𓆪", callback_data="close"),
            InlineKeyboardButton(text="10 》", callback_data=f"ADMIN 2|{chat_id}"),
        ]
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bar = generate_progress_bar(percentage)

    return [
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ]
    ]
