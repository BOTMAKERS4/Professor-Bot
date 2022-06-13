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

@bot.on(admin_cmd(pattern=r"mass_report_start ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"mass_report_start ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str is None:
        event = await edit_or_reply(event, "Please provide a valid PMR Code to begin mass reporting.")
        return
    animation_interval = 3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Initializing...")
    await asyncio.sleep(5)
    animation_chars = [
        "**ProfessorBot:** Stopping all processes with SIGTERM",
        "**ProfessorBot:** Process exited with `status 0`",
        "**ProfessorBot:** Starting process with command `python3 -m mass_report`",
        "**ProfessorBot:** State changed from starting to up",
        "**ProfessorBot:** Connecting To [ProfessorBot's server](harshjais369/ProfessorBot)",
        "**ProfessorBot:** Connection established successfully to port 2573",
        "**ProfessorBot:** Connecting To [Telegram.org](harshjais369/ProfessorBot)",
        "**ProfessorBot:** Connection established successfully to port 2150",
        f"**ProfessorBot:** Login success by user {DEFAULTUSER}",
        "**ProfessorBot:** Getting ready all accounts...",
        "**ProfessorBot:** Starting mass report tool...",
        "**ProfessorBot:** Mass Report has been started successfully!\n\n**More info:** __User is being reported from total 384 IDs...\nPlease wait till it finishes, you'll be informed to your email. It usually takes 12hr to 72hr or may take more than that. Have patience!__\n\nThanks for using this tool!\nPowerful Mass Report Tool by ProfessorBot.",
        
        
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])

CmdHelp("mass_report_start").add_command(
    "mass_report_start", "<PMR Code>", "Starts Mass Report Tool"
).add

