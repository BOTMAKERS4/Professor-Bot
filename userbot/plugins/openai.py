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
ME = int(bot.uid)

@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.OPENAI_API_KEY is None:
        event = await eor(event, "❌ OpenAI API key has not configured yet.")
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        event = await eor(event, "**OpenAI ChatGPT:** Hey! This is OpenAI's GPT3 chatbot, now available with ProfessorBot by Harsh Jaiswal. I am here to talk to you in a friendly, meaningful way as well as answer any questions you may have.")
        return
    if not event.reply_to_msg_id:
        # initiate a new convo
        event = await eor(event, asknew(str(input_str)))
        return
    prompt_msg = "" # prompt msg to be sent to AI
    reply = await event.message.get_reply_message() # reply=None (if reply not found)
    if not reply.text:
        eor(event, "❌ **OpenAI ChatGPT:** I\'ve not got the ability to comprehend anything other than text yet. For further assistance, talk to my trainner: @harshjais369")
        return
    # Test starts ---------
    if reply.message.count("OpenAI ChatGPT: ", 0, 25) == 0:
        event = await eor(event, "Not found!")
    else:
        event = await eor(event, "Found!")
    await asyncio.sleep(5)
    # Test ends ---------
    if (reply.sender_id != ME) or (reply.message.count("OpenAI ChatGPT: ", 0, 25) == 0):
        prompt_msg = str(reply.message) + str(input_str)
    else:
        prompt_msg = str(input_str)
        while reply:
            prompt_msg = str(reply.message) + "\n" + prompt_msg
            if reply.sender_id != ME:
                break
            reply = reply.get_reply_message()
    event = await eor(event, askfromreply(prompt_msg))
    return

# ————————————————————————---------------------
def asknew(prompt):
    return f"#new_convo\nYour prompt: {prompt}"

def askfromreply(prompt):
    return f"#reply_from_previous\nYour prompt: {prompt}"
    

CmdHelp("q").add_command(
  "q", "<your question>", "Talk to ChatGPT3 AI."
).add
