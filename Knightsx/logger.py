import logging

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("knightsx_log.txt"),
        logging.StreamHandler(),
    ],
)

# Suppress overly verbose logs from dependencies
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

# Return a named logger (for compatibility)
def getLogger(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Alias for legacy code
LOGGER = getLogger