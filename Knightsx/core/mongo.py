from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logger import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    pymongodb = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = pymongodb["Knightsx"]  # Use your actual database name here
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()
