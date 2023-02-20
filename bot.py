import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Client, idle
if __name__ == "__main__" :
    # Creating essential directories, if they does not exists
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    if not os.path.isdir(Config.ADMIN_LOCATION):
        os.makedirs(Config.ADMIN_LOCATION)
    if not os.path.isdir(Config.CREDENTIALS_LOCATION):
        os.makedirs(Config.CREDENTIALS_LOCATION)        
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "Mega_Link_Downloader_Bot",
        bot_token=6090268851:AAEJEsvs8nB_YKQc3tKy5hVpeWgu53kwjuI,
        api_id=Config.23977500,
        api_hash=Config.a4bfcc57b242dc49952c02c593b47edb,
        plugins=plugins
    )
    app.run()
    idle()
