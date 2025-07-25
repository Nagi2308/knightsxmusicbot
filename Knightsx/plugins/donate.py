from pyrogram import Client, filters
from Knightsx import app  # updated to match your project name
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    filters.command("donate") & filters.group & ~filters.edited
)
async def donate(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/hinem5.jpg",
        caption=(
            "🎗️ **Support Knight X Music!**\n\n"
            "If you enjoy using the bot and want to support its development, "
            "consider donating or promoting your group with us.\n\n"
            "➤ [Click here](https://t.me/Nagi2308) to contact the owner.\n"
            "➤ Join our support and updates channels below.\n\n"
            "**Thank you for your love and support! 💖**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💸 Donate / Contact Owner", url="https://t.me/Nagi2308")
                ],
                [
                    InlineKeyboardButton("💬 Support", url="https://t.me/Knightxbotsupport"),
                    InlineKeyboardButton("📢 Updates", url="https://t.me/KnightsXbots")
                ]
            ]
        )
    )
