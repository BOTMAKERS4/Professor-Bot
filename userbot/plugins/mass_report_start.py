from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp
from asyncio import sleep
from math import ceil
from re import compile
import asyncio
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon import functions
from userbot.cmdhelp import *
from mafiabot.utils import *
from userbot.Config import Config
from . import *
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)

# Super powerful Mass Report tool by ProfessorBot.
# Plugin created by: @harshjais369
# Do not copy without having any permissions!

@bot.on(admin_cmd(pattern=r"mass_report_start$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"mass_report_start$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(9)
    event = await edit_or_reply(event, "Initializing...")
    animation_chars = [
        "**ProfessorBot:** Process exited with `status 0`",
        "**ProfessorBot:** Stopping all processes with SIGTERM",
        "**ProfessorBot:** Starting process with command `python3 -m stdborg`",
        "**ProfessorBot:** State changed from starting to up",
        "**ProfessorBot:** Connecting To [ProfessorBot's server](harshjais369/ProfessorBot)",
        "**ProfessorBot:** Connecting To [Telegram.org](harshjais369/ProfessorBot)",
        f"**ProfessorBot:** Login success by user {DEFAULTUSER}",
        "**ProfessorBot:** Getting ready all accounts...",
        "**ProfessorBot:** Mass Report has been started successfully!\n\n**More info:** __User is being reported from total 384 IDs...\nPlease wait till it finishes, you'll be informed to your email. It usually takes 12hr to 24hr or may take more than that. Have patience!__\n\nThanks for using this tool!\nPowerful Mass Report Tool by ProfessorBot.",
        
        
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 9])

CmdHelp("mass_report_start").add_command(
    "mass_report_start", "", "Starts Mass Report Tool"
).add

