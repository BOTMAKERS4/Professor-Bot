# Thanks to MafiaBot
# Re-engineered as ProfessorBot by @harshjais369

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝗣𝗿𝗼𝗳𝗲𝘀𝘀𝗼𝗿 𝗕𝗼𝘁"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
pm_caption = "  __**🔥⚡ 𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 ⚡🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n    **『😈[{DEFAULTUSER}](tg://user?id={mafia})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}`\n"
pm_caption += f"┣•➳➠ `Version:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Creator:` Himanshu\n"
pm_caption += f"┣•➳➠ `Re-engineered by:` Harsh Jaiswal\n"
pm_caption += f"┣•➳➠ `Contact:` [ᴛᴀᴘ ʜᴇʀᴇ 👈🏻](https://t.me/harshjais369)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += "   🔸 [Repository](https://github.com/harshjais369/ProfessorBot) 🔸 [License](https://github.com/harshjais369/ProfessorBot/blob/main/LICENSE) 🔸"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am I alive."
).add()
