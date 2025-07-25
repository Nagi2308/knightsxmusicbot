from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Knightsx import app

# /owner command - GROUP
@app.on_message(filters.command("owner") & filters.group & ~filters.edited)
async def owner_group(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/hinem5.jpg",
        caption="⚔️ᴄʟɪᴄᴋ🗡️ʙᴇʟᴏᴡ👇ʙᴜᴛᴛᴏɴ🗡️ᴛᴏ❤️ᴅᴍ📞 ᴏᴡɴᴇʀ ⚔️",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("༒︎★•亗『ᴏᴡɴᴇʀ』亗•★", url="https://t.me/Nagi2308")]
            ]
        ),
    )


# /owner command - PRIVATE
@app.on_message(filters.command("owner") & filters.private & ~filters.edited)
async def owner_private(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/hinem5.jpg",
        caption="⚔️ᴄʟɪᴄᴋ🗡️ʙᴇʟᴏᴡ👇ʙᴜᴛᴛᴏɴ🗡️ᴛᴏ❤️ᴅᴍ📞 ᴏᴡɴᴇʀ ⚔️",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("༒︎★•亗『ᴏᴡɴᴇʀ』亗•★", url="https://t.me/Nagi2308")]
            ]
        ),
    )


# /knights command - GROUP ONLY
@app.on_message(filters.command("knights") & filters.group & ~filters.edited)
async def knights_group(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/7d2a56b2e48a1601a1776.jpg",
        caption=(
            "⚔️🛡️•──────────────•🛡️⚔️\n"
            "         𝗗𝗜𝗩𝗜𝗡𝗘 𝗞𝗡𝗜𝗚𝗛𝗧𝗦 ⚔️\n"
            "⚔️🛡️•──────────────•🛡️⚔️\n"
            "┏━━━━━━━ ⚔️ ━━━━━━━┓\n\n"
            "“Feel pain. Accept pain. Know pain.\n"
            "Those who do not understand true pain\n"
            "can never understand true peace.”\n\n"
            "┗━━━━━━━ 🛡️ ━━━━━━━┛"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("JOIN⚔️DIVINE🛡️6KNIGHTS⚔️", url="https://t.me/DIVINE_KNIGHTS")]
            ]
        ),
    )


# /repo and /source command - GROUP
@app.on_message(filters.command(["repo", "source"]) & filters.group & ~filters.edited)
async def repo_group(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/5wd7if.jpg",
        caption="ℂ𝕝𝕚𝕔𝕜⚔️𝔹𝕖𝕝𝕠𝕨🛡️𝔹𝕦𝕥𝕥𝕠𝕟⚔️𝕗𝕠𝕣🛡️𝔾𝕚𝕥𝕙𝕦𝕓",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚔️ƨσʋяcɛ🛡️", url="https://github.com/Nagi2308/Knightsxbots/blob/main/README.md")]
            ]
        ),
    )


# /repo command - PRIVATE
@app.on_message(filters.command("repo") & filters.private & ~filters.edited)
async def repo_private(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/5wd7if.jpg",
        caption="ℂ𝕝𝕚𝕔𝕜⚔️𝔹𝕖𝕝𝕠𝕨🛡️𝔹𝕦𝕥𝕥𝕠𝕟⚔️𝕗𝕠𝕣🛡️𝔾𝕚𝕥𝕙𝕦𝕓",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🛡️ƨσʋяcɛ⚔️", url="https://github.com/Nagi2308/Knightsxbots/blob/main/README.md")]
            ]
        ),
    )
