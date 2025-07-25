import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types

import config
from config import adminlist, chatstats, clean, userstats
from strings import get_command
from Knightsx import app, userbot
from Knightsx.misc import SUDOERS
from Knightsx.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_particular_top,
    get_served_chats,
    get_served_users,
    get_user_top,
    is_cleanmode_on,
    set_queries,
    update_particular_top,
    update_user_top
)
from Knightsx.utils.decorators.language import language
from Knightsx.utils.formatters import alpha_to_int

# Command
BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")

# Config
AUTO_DELETE = config.CLEANMODE_DELETE_MINS
AUTO_SLEEP = 5
IS_BROADCASTING = False
cleanmode_group = 15


@app.on_raw_update(group=cleanmode_group)
async def clean_mode(client, update, users, chats):
    global IS_BROADCASTING
    if IS_BROADCASTING:
        return
    if not isinstance(update, types.UpdateReadChannelOutbox):
        return
    if users or chats:
        return
    message_id = update.max_id
    chat_id = int(f"-100{update.channel_id}")
    if not await is_cleanmode_on(chat_id):
        return
    if chat_id not in clean:
        clean[chat_id] = []
    time_now = datetime.now()
    clean[chat_id].append({
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=AUTO_DELETE),
    })
    await set_queries(1)


@app.on_message(filters.command(BROADCAST_COMMAND) & SUDOERS)
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING

    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_5"])
        query = message.text.split(None, 1)[1]
        for opt in ["-pin", "-pinloud", "-nobot", "-assistant", "-user"]:
            query = query.replace(opt, "")
        if query.strip() == "":
            return await message.reply_text(_["broad_6"])

    IS_BROADCASTING = True

    # 1. Broadcast to Groups
    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = [int(c["chat_id"]) for c in await get_served_chats()]
        for chat_id in chats:
            try:
                msg = await (
                    app.forward_messages(chat_id, y, x)
                    if message.reply_to_message
                    else app.send_message(chat_id, text=query)
                )
                if "-pin" in message.text:
                    await msg.pin(disable_notification=True)
                    pin += 1
                elif "-pinloud" in message.text:
                    await msg.pin(disable_notification=False)
                    pin += 1
                sent += 1
            except FloodWait as e:
                await asyncio.sleep(min(e.x, 200))
            except:
                continue
        try:
            await message.reply_text(_["broad_1"].format(sent, pin))
        except:
            pass

    # 2. Broadcast to Users
    if "-user" in message.text:
        susr = 0
        users = [int(u["user_id"]) for u in await get_served_users()]
        for user_id in users:
            try:
                if message.reply_to_message:
                    await app.forward_messages(user_id, y, x)
                else:
                    await app.send_message(user_id, text=query)
                susr += 1
            except FloodWait as e:
                await asyncio.sleep(min(e.x, 200))
            except:
                continue
        try:
            await message.reply_text(_["broad_7"].format(susr))
        except:
            pass

    # 3. Assistant Broadcast
    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_2"])
        text = _["broad_3"]
        from Knightsx.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.iter_dialogs():
                try:
                    if message.reply_to_message:
                        await client.forward_messages(dialog.chat.id, y, x)
                    else:
                        await client.send_message(dialog.chat.id, text=query)
                    sent += 1
                except FloodWait as e:
                    await asyncio.sleep(min(e.x, 200))
                except:
                    continue
            text += _["broad_4"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass

    IS_BROADCASTING = False


# Background Auto-Clean Task
async def auto_clean():
    while not await asyncio.sleep(AUTO_SLEEP):
        try:
            # Chat stats
            for chat_id in chatstats:
                while chatstats[chat_id]:
                    dic = chatstats[chat_id].pop(0)
                    vidid = dic["vidid"]
                    title = dic["title"]
                    spot_data = await get_particular_top(chat_id, vidid)
                    new_spot = {
                        "spot": spot_data["spot"] + 1 if spot_data else 1,
                        "title": title,
                    }
                    await update_particular_top(chat_id, vidid, new_spot)

            # User stats
            for user_id in userstats:
                while userstats[user_id]:
                    dic = userstats[user_id].pop(0)
                    vidid = dic["vidid"]
                    title = dic["title"]
                    spot_data = await get_user_top(user_id, vidid)
                    new_spot = {
                        "spot": spot_data["spot"] + 1 if spot_data else 1,
                        "title": title,
                    }
                    await update_user_top(user_id, vidid, new_spot)

            # Clean mode messages
            for chat_id in clean:
                if chat_id == config.LOG_GROUP_ID:
                    continue
                for x in clean[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue

            # Update admin list
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for member in app.get_chat_members(chat_id, filter="administrators"):
                        if member.can_manage_voice_chats:
                            adminlist[chat_id].append(member.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for username in authusers:
                        user_id = await alpha_to_int(username)
                        adminlist[chat_id].append(user_id)

        except:
            continue


# Start background cleaner
asyncio.create_task(auto_clean())
