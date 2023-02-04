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
from userbot import bot, LOGS
from userbot.cmdhelp import *
from mafiabot.utils import *
from userbot.Config import Config
from userbot.plugins.sql_helper.openaiconfig_sql import getOpenaiConfig, setOpenaiConfig
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

# ProfessorBot × OpenAI-ChatGPT3 ©
# Plugin creator: Harsh Jaiswal (@harshjais369)
# Do not copy without having permission!
# ————————————————————————---------------------

ME = int(bot.uid)
AI_API_KEY = Config.OPENAI_API_KEY
AI_MODES = ['aiuser', 'default', 'sarcastic', 'sarcastic_human', 'friend', 'quick_answer', 'negative', 'pleasant']
AI_GREET = "**OpenAI ChatGPT:** Hey! This is GPT-3 AI chatbot model trained by OpenAI team, fine-tuned with " \
           "ProfessorBot by Harsh Jaiswal. I am here to talk with you in friendly and meaningful way, as well as " \
           "answer any questions you may have."
AI_ERROR = "❌ **ProfessorBot:** An error occurred while communicating with GPT3-AI Model. Make sure you\'ve " \
           "configured the OpenAI API key correctly in your `.env` file.\n\nFor more information and further " \
           "assistance, contact: @harshjais369"
AI_FOOTER_STR = "\n\n───────────────────\n\tᴾʳᵒᶠᵉˢˢᵒʳᴮᵒᵗ • ᴼᵖᵉⁿᴬᴵ".expandtabs(10)


@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if AI_API_KEY is None:
        event = await eor(event, "❌ OpenAI API key is not configured.")
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        event = await eor(event, AI_GREET)
        return
    if not event.reply_to_msg_id:
        # initiate a fresh convo
        resstr = f"**> Harsh:** {str(input_str)}\n\n**OpenAI ChatGPT:** {asknew(str(input_str))}"
        event = await eor(event, resstr)
        return
    prompt_msg = "" # prompt which has to be sent to AI
    reply = await event.message.get_reply_message() # (reply=None; if reply not found)
    if not reply.text:
        event = await eor(event, "❌ **OpenAI ChatGPT:** I\'ve not got the ability to comprehend anything other than text yet. For further assistance, talk to my trainner: @harshjais369")
        return
    conf = getOpenaiConfig()
    if conf is None:
        event = await eor(event, f"{AI_ERROR}\n\n**Error details:** `Failed to fetch OpenAI config from ProfessorBot\'s server.`")
        return
    if (reply.sender_id != ME) or (reply.message.count("OpenAI ChatGPT: ", 0) == 0):
        prompt_msg = f"\"{str(reply.message)}\"\n\n{str(input_str)}"
    else:
        prompt_msg = f"You: {str(input_str)}"
        while reply:
            prompt_msg = str(reply.message) + "\n\n" + prompt_msg
            if str(reply.message).count("OpenAI ChatGPT: ") == 0:
                prompt_msg = "You: " + prompt_msg
            if reply.sender_id != ME:
                break
            reply = await reply.get_reply_message()
        prompt_msg = prompt_msg.replace("OpenAI ChatGPT: ", conf[7].replace("\n", "") + " ").replace("> Harsh: ", "You: ").replace("You: ", "", 1).replace(AI_FOOTER_STR, "")
    resstr = f"**> Harsh:** {str(input_str)}\n\n**OpenAI ChatGPT:** {askfromreply(prompt_msg, conf)}"
    event = await eor(event, resstr)
    return


@bot.on(admin_cmd(pattern="e(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="e(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if AI_API_KEY is None:
        event = await eor(event, "❌ OpenAI API key is not configured.")
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        event = await eor(event, AI_GREET)
        return
    if not event.reply_to_msg_id:
        event = await eor(event, correctGrammarFunc(str(input_str)))
    else:
        reply = await event.message.get_reply_message() # (reply=None; if reply not found)
        if not reply.text:
            event = await eor(event, "❌ **OpenAI ChatGPT:** I\'ve not got the ability to comprehend anything other than text yet. For further assistance, talk to my trainner: @harshjais369")
            return
        resp = correctGrammarFunc(str(reply.message))
        event = await eor(event, resp)
        if resp == AI_ERROR:
            await asyncio.sleep(3)
            await event.delete()
    return

# ————————————————————————---------------------
def asknew(prompt):
    conf = getOpenaiConfig()
    if conf is None:
        return f"{AI_ERROR}\n\n**Error details:** `Failed to fetch OpenAI config from ProfessorBot\'s server.`"
    try:
        conf[6] = conf[6].replace("{{{", "", 1).replace("}}}", "", 1)
    except:
        pass
    try:
        openai.api_key = AI_API_KEY
        resp_obj = openai.Completion.create(
            model=conf[0],
            prompt=f"{conf[6]}{prompt}{conf[7]}",
            temperature=conf[1],
            max_tokens=conf[2],
            top_p=conf[3],
            frequency_penalty=conf[4],
            presence_penalty=conf[5]
        )
        ans_str = resp_obj["choices"][0]["text"].lstrip()
        if resp_obj["choices"][0]["finish_reason"] == "length":
            ans_str = f"{ans_str}...\n__(reached max. text limit)__"
        ans_str = f"{ans_str}{AI_FOOTER_STR}"
        return ans_str
    except Exception as e:
        return f"{AI_ERROR}\n\n**Error details:** `{repr(e)}`"

def askfromreply(prompt, conf):
    LOGS.info(prompt)
    try:
        conf[6] = conf[6].replace("{{{", "", 1).replace("}}}", "", 1)
    except:
        pass
    try:
        openai.api_key = AI_API_KEY
        resp_obj = openai.Completion.create(
            model=conf[0],
            prompt=f"{conf[6]}{prompt}\n{conf[7]}",
            temperature=conf[1],
            max_tokens=conf[2],
            top_p=conf[3],
            frequency_penalty=conf[4],
            presence_penalty=conf[5]
        )
        ans_str = resp_obj["choices"][0]["text"].lstrip()
        if resp_obj["choices"][0]["finish_reason"] == "length":
            ans_str = f"{ans_str}...\n__(reached max. text limit)__"
        ans_str = f"{ans_str}{AI_FOOTER_STR}"
        return ans_str
    except Exception as e:
        return f"{AI_ERROR}\n\n**Error details:** `{repr(e)}`"


def correctGrammarFunc(prompt):
    try:
        openai.api_key = AI_API_KEY
        resp_obj = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Correct this into standard and more fluent English:\n\n{prompt}",
            temperature=0,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        ans_str = resp_obj["choices"][0]["text"]
        if resp_obj["choices"][0]["finish_reason"] == "length":
            ans_str = f"{ans_str}...\n__(reached max. text limit)__"
        ans_str = f"{ans_str}\n\n───────────────────\n**Gʀᴀᴍᴍᴀʀ ʀᴇᴄᴛɪꜰɪᴄᴀᴛɪᴏɴ ᴛᴏᴏʟ**\n\tᴾʳᵒᶠᵉˢˢᵒʳᴮᵒᵗ • ᴼᵖᵉⁿᴬᴵ"
        return ans_str.expandtabs(10)
    except Exception as e:
        return f"{AI_ERROR}\n\n**Error details:** `{repr(e)}`"


CmdHelp("q").add_command(
  "q", "<your question>", "Start a chat with ChatGPT3."
).add_command(
  "e", "<reply/text>", "Corrects sentences into standard and fluent English by GPT3 AI."
).add
