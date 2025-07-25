from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from Knightsx.logger import getLogger
import config

LOGGER = getLogger(__name__)

class KnightsXBot(Client):
    def __init__(self):
        LOGGER.info("Initializing KnightsxMusic Bot...")
        super().__init__(
            name="knightsx",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        # Get bot info
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        LOGGER.info("✅ KnightsxMusic Bot is alive and running...")

        # Alive message
        alive_text = (
            "╔═══❰ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ❱═══❍⊱❁۪۪\n"
            "║\n"
            "║┣⪼ 🥀 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🎉\n"
            f"║\n║◈ 𝐍𝐚𝐦𝐞: {config.MUSIC_BOT_NAME}\n"
            f"║┣⪼ 𝐈𝐃: `{self.id}`\n"
            f"║┣⪼ 𝐔𝐬𝐞𝐫: @{self.username}\n"
            "║┣⪼ 💖 𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 😍\n"
            "╚════════════════════❍⊱❁"
        )

        # Send alive message to log group
        try:
            await self.send_message(chat_id=config.LOGGER_ID, text=alive_text)
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER.error(
                "❌ Bot couldn't access the log group/channel. "
                "Make sure the bot is added and promoted."
            )
            raise SystemExit()
        except Exception as ex:
            LOGGER.error(f"❌ Unexpected error while sending log message: {ex}")
            raise SystemExit()

        # Admin check
        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER.error("❌ Bot is not an admin in the log group.")
                raise SystemExit()
        except Exception as ex:
            LOGGER.error(f"❌ Couldn't verify admin status in log group: {ex}")
            raise SystemExit()

        LOGGER.info(f"✅ Bot Started as {self.name} (@{self.username})")

    async def stop(self):
        await super().stop()
        LOGGER.info("🛑 KnightsxMusic Bot stopped successfully.")
