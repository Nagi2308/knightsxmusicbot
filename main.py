import asyncio
from Knightsx import KnightsXBot  # Make sure this import path is correct

bot = KnightsXBot()

async def main():
    await bot.start()
    await asyncio.Event().wait()  # Keeps bot running

if __name__ == "__main__":
    asyncio.run(main())
