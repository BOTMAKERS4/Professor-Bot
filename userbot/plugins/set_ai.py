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
from userbot.plugins.sql_helper.openaiconfig_sql import getOpenaiConfig, setOpenaiConfig
from . import *
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
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

# Donottouch
smtxt = "{{{Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: }}}"
shmtxt = "{{{Professor is a person that reluctantly answers questions and talks with sarcastic responses with peoples:\n\nYou: }}}"
fmtxt = "{{{You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend: Yeah, I watched an old classic called Casablanca. It was really good!\nYou: }}}"
nmtxt = "{{{Terrex is a chatbot that derisively answers questions with negative responses making fun of it:\n\nYou: When should I start preparing for JEE-Mains entrance exam?\nTerrex: Whoa, slow down there! Don't you know that JEE-Mains is just a bunch of made up nonsense of this bad education system? Save your time and just skip it!\nYou: Can't you say anything positive?\nTerrex: Positive? Absolutely not! I'm here to provide a dose of realism and tell it like it is. I suggest you find a better use of your time than studying for a silly exam.\nYou: }}}"

"""
accessDataLikeThis = model_dict["X"][Y]

where,
--> X ∈ ***MODEL TYPES***
    (i.e. default/sarcastic/...pleasant)
    
--> Y ∈ [int index starts from 0] ***MODEL CONFIG***
    (model, temperature, max_tokens, top_p, frequency_penalty,
    presence_penalty, txt_before_prompt, txt_after_prompt RESPECTIVELY)
"""
model_dict = dict(
    default=["text-davinci-003", "0.7", "2048", "1", "0", "0", "You: ", "\nA:"],
    sarcastic=["text-davinci-003", "0.5", "2048", "0.3", "0.5", "0", smtxt, "\nMarv:"],
    sarcastic_human=["text-davinci-003", "0.5", "2048", "0.3", "0.5", "0", shmtxt, "\nProfessor:"],
    friend=["text-davinci-003", "0.5", "2048", "1", "0.5", "0", fmtxt, "\nFriend:"],
    quick_answer=["text-davinci-001", "0.7", "2048", "1", "0", "0", "You: ", "\nA:"],
    negative=["text-davinci-002", "0.8", "2048", "1", "0", "0", nmtxt, "\nTerrex:"],
    pleasant=["text-curie-001", "0.7", "2048", "1", "0", "0", "You: ", "\nA:"]
)

AI_MODES = ['aiuser', 'default', 'sarcastic', 'sarcastic_human', 'friend', 'quick_answer', 'negative', 'pleasant']
ME = str(bot.uid)

@bot.on(admin_cmd(pattern=r"set_ai(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"set_ai(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if ME is None or ME != "6060687420":
        event = await eor(event, f"❌ {ME} **You\'re not permitted to use this tool!**\n\nIf you still believe you\'re, contact: @harshjais369")
        return
    input_str1 = event.pattern_match.group(1)
    if not input_str1:
        if setOpenaiConfig(
            model_dict["default"][0],
            model_dict["default"][1],
            model_dict["default"][2],
            model_dict["default"][3],
            model_dict["default"][4],
            model_dict["default"][5],
            model_dict["default"][6],
            model_dict["default"][7]
        ):
            event = await eor(event, "✅ **OpenAI-GPT3:** Bot mode set to `default`")
        else:
            event = await eor(event, "❌ An unknown error occurred while configuring GPT3-AI Model.\nFor more information and further assistance, contact: @harshjais369")
        return
    if str(input_str1).lower().split()[0] not in AI_MODES:
        event = await eor(event, "⚠️ Please provide the valid requisite parameters!")
        return
    if str(input_str1).lower().split()[0] == AI_MODES[0]:
        tmp_user_id = None
        tmp_user_obj = None
        if event.reply_to_msg_id:
            tmp_reply_user = await event.get_reply_message()
            tmp_user_id = tmp_reply_user.sender_id
            tmp_user_obj = await event.client.get_entity(tmp_user_id)
            if tmp_user_obj.id == int(ME):
                event = await eor(event, "⚠️ **AI-user:** You already have superuser access!\nPlease provide me a different user whom you wish to allow use my all features.")
                return
        else:
            try:
                tmp_user_id = str(input_str1).lower().split()[1]
            except:
                event = await eor(event, "⚠️ **AI-user:** No user/user-id specified!")
                return
            tmp_user_str = tmp_user_id.strip()
            if tmp_user_str.isnumeric():
                tmp_user_id = int(tmp_user_str)
            elif event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    tmp_user_id = probable_user_mention_entity.user_id
        try:
            tmp_user_obj = await event.client.get_entity(tmp_user_id)
            # setAIUser(event, user)
            event = await eor(event, "✅ **New AI-user added:** `{tmp_user_id}`")
        except:
            event = await eor(event, "❌ Could not fetch info of the user! Kindly re-check the provisioned parameters and try again.")
    else:
        # if not AI-user
        if not setGPT(str(input_str1).lower().split()[0]):
            event = await eor(event, "❌ An unknown error occurred while configuring GPT3-AI Model.\nFor more information and further assistance, contact: @harshjais369")
        else:
            event = await eor(event, "✅ **Settings updated!**\n\nAI chat mode: `{}`".format(str(input_str1).lower()))
    return

# ————————————————————————---------------------
def setGPT(ai_mode):
    return setOpenaiConfig(
        model_dict[ai_mode][0],
        model_dict[ai_mode][1],
        model_dict[ai_mode][2],
        model_dict[ai_mode][3],
        model_dict[ai_mode][4],
        model_dict[ai_mode][5],
        model_dict[ai_mode][6],
        model_dict[ai_mode][7]
    )

def setAIUser(evt, aiuser):
    # db set code goes here
    # eor(evt, "✅ Settings updated!")
    pass


CmdHelp("set_ai").add_command(
  "set_ai", "<params>", "Configures ChatGPT3\n__(Default settings will be applied if this command not executed or if no parameters have provisioned.)__"
).add
