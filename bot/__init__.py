from swibots import Client, BotCommand
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOGGER = logging.getLogger(__name__)


load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN","")
BOT_USERNAME = os.environ.get("BOT_USERNAME","TelegraphBot")
OWNER_ID = int(os.environ.get("OWNER_ID","3494"))

DATABASE_URL = os.environ.get("DATABASE_URL","")
DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")

try:
    app = Client(
        token=BOT_TOKEN,
        plugins={'root': os.path.join(__package__, 'plugins')}
    ).set_bot_commands(
    [
        BotCommand("start","To start me", True),
        BotCommand("help","help message", True)
    ]
)
    LOGGER.info(f"BOT STARTED at @{app.name}🚀")
except Exception as e:
    LOGGER.warn(f"ERROR creating session with bot: {e}")


if os.path.exists("downloads"):
    pass
else:
    os.mkdir("downloads")
