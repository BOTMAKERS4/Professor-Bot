from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp
from asyncio import sleep
from math import ceil
from re import compile
import asyncio
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon import functions
from userbot import bot
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

# ProfessorBot × OpenAI-ChatGPT3
# Plugin creator: Harsh Jaiswal (@harshjais369)
# Do not copy without having any permissions!

ME = str(bot.uid)

@bot.on(admin_cmd(pattern="set_ai(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="set_ai(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if ME is None or ME != "881259026":
        event = await eor(event, f"❌ {ME} **You\'re not permitted to use this tool!**\n\nIf you still believe you\'re, contact: @harshjais369")
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        event = await eor(event, "⚠️ Please provide the valid requisite parameters!")
        return
    eor(event, "✅ Settings updated!")

CmdHelp("set_ai").add_command(
  "set_ai", "<params>", "Configures ChatGPT3\n__(Default settings will be applied if this command not executed.)__"
).add
