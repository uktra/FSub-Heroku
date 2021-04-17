import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(884031659)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[🔔](https://telegra.ph/file/0f8799ec342c196e2d23c.png) **FORCE SUBSCRIBE :**\n\n𝐹𝑜𝑟𝑐𝑒 𝐺𝑟𝑜𝑢𝑝 𝑀𝑒𝑚𝑏𝑒𝑟𝑠 𝑇𝑜 𝐽𝑜𝑖𝑛 𝐴 𝑆𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 𝐵𝑒𝑓𝑜𝑟𝑒 𝑆𝑒𝑛𝑑𝑖𝑛𝑔 𝑀𝑒𝑠𝑠𝑎𝑔𝑒𝑠 𝑖𝑛 𝑇ℎ𝑒 𝐺𝑟𝑜𝑢𝑝\n𝐼 𝑊𝑖𝑙𝑙 𝑀𝑢𝑡𝑒 𝑀𝑒𝑚𝑏𝑒𝑟𝑠 𝑖𝑓 𝑇ℎ𝑒𝑦 𝑁𝑜𝑡 𝐽𝑜𝑖𝑛𝑒𝑑 𝑌𝑜𝑢𝑟 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 𝐴𝑛𝑑 𝑇𝑒𝑙𝑙 𝑇ℎ𝑒𝑚 𝑇𝑜 𝐽𝑜𝑖𝑛 𝑇ℎ𝑒 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 𝐴𝑛𝑑 𝑈𝑛𝑚𝑢𝑡𝑒 𝑇ℎ𝑒𝑚𝑠𝑒𝑙𝑓 𝐵𝑦 𝑃𝑟𝑒𝑠𝑠𝑖𝑛𝑔 𝐴 𝐵𝑢𝑡𝑡𝑜𝑛.",
        
        "[⚙](https://telegra.ph/file/cbcca74bfdd4dc3308444.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "[⚙](https://i.imgur.com/LnOEiTK.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) **DEVELOPED BY @Goku_kun**"
      ]

      START_MSG = "**Hey! [👋](https://telegra.ph/file/0f8799ec342c196e2d23c.png) [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help"
