from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.stream import InputStream
from pytgcalls.types import AudioPiped, VideoPiped

from config import API_ID, API_HASH, SESSION, SESSION2, SESSION3, SESSION4, SESSION5

clients = []

if SESSION:
    KnightsXAss1 = Client(name="KnightsXAss1", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
    clients.append(KnightsXAss1)

if SESSION2:
    KnightsXAss2 = Client(name="KnightsXAss2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
    clients.append(KnightsXAss2)

if SESSION3:
    KnightsXAss3 = Client(name="KnightsXAss3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
    clients.append(KnightsXAss3)

if SESSION4:
    KnightsXAss4 = Client(name="KnightsXAss4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
    clients.append(KnightsXAss4)

if SESSION5:
    KnightsXAss5 = Client(name="KnightsXAss5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
    clients.append(KnightsXAss5)


class Call:
    def __init__(self):
        self.clients = clients
        self.pytgcalls = {client: PyTgCalls(client) for client in clients}
        self.streams = {}
        self.queue = {}

    async def start(self):
        for client in self.clients:
            await client.start()
            await self.pytgcalls[client].start()

    async def stop(self):
        for client in self.clients:
            await self.pytgcalls[client].stop()
            await client.stop()

    async def join_voice_chat(self, chat_id, audio_url, video_url=None, client=None):
        if client is None:
            client = self.clients[0]

        tgcall = self.pytgcalls[client]

        if video_url:
            stream = InputStream(
                AudioPiped(audio_url),
                VideoPiped(video_url)
            )
        else:
            stream = AudioPiped(audio_url)

        await tgcall.join_group_call(chat_id, stream)
        self.streams[chat_id] = (client, stream)

    async def leave_voice_chat(self, chat_id):
        if chat_id in self.streams:
            client, _ = self.streams.pop(chat_id)
            tgcall = self.pytgcalls[client]
            await tgcall.leave_group_call(chat_id)


Knights = Call()
