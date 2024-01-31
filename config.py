#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN ='6872808044:AAGiNiJ5GrCZtQMKfKC38jrU-zf5plbXFYs'

#Your API ID from my.telegram.org
APP_ID =18102551
#Your API Hash from my.telegram.org
API_HASH = '7c51c14ac28592debd5a45a3fdd376eb'

#Your db channel Id
CHANNEL_ID =-1002011777857


#OWNER ID
OWNER_ID = 6669835291
#Port
PORT =8080

#Database 
DB_URI =' mongodb+srv://alienufowala:kishan99@cluster0.wrwmsil.mongodb.net/?retryWrites=true&w=majority'
DB_NAME = "filesharexbot"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = -1002130334868

TG_BOT_WORKERS =4

#start message
START_MSG ="Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link."
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6888539582").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True 

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! bhai direct msg kr admin ko @alien_anonx me bot hu "

ADMINS.append(OWNER_ID)
ADMINS.append(6888539582)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
