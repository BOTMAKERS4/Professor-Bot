from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp
from asyncio import sleep
from math import ceil
from re import compile
import asyncio
import openai
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
# ————————————————————————---------------------

AI_MODES = ['aiuser', 'default', 'sarcastic', 'sarcastic_human', 'friend', 'quick_answer', 'negative', 'pleasant']
ME = str(bot.uid)

@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.OPENAI_API_KEY is None:
        event = await eor(event, "OpenAI API key is not set.")
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        event = await eor(event, "**OpenAI ChatGPT:** Hey! This is OpenAI's GPT3 chatbot, now available with ProfessorBot by Harsh Jaiswal. I am here to talk to you in a friendly, meaningful way as well as answer any questions you may have.")
        return
    if not event.reply_to_msg_id:
        # process new convo
        event = await eor(event, asknew(str(input_str)))
        return    
    message = event.message
    prompt_msg = ""
    while message:
        tmp_message = message
        reply = await message.get_reply_message() # reply=None (if reply not found)
        if message.id == ME:
            if not reply.text:
                message = None
                eor(event, "I\'ve not got the ability to comprehend anything other than text yet.")
                break
        prompt_msg = message.text + prompt_msg # Need correct func()
        message = reply
        if tmp_message.id != ME:
            message = None
    # ...
    return
            
# ————————————————————————---------------------
def asknew():
    pass

def askfromreply():
    pass
    

CmdHelp("q").add_command(
  "q", "<your question>", "Talk to ChatGPT3 AI."
).add
