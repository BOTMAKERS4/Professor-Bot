from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp
from asyncio import sleep
from telethon import functions
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

@bot.on(admin_cmd(pattern="mass_report(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mass_report(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    # event.pattern_match.group(1)
    user, reason = await get_user_from_event(event)
    if not user:
        return
    type = set_type(2)
    user_info = set_user(user)
    caution_str = "⚠️ **Caution:** This process is not reversible. Please re-check the above info and make sure you\'ve provided right channel/group/user ID. It\'ll get deleted permanently by Telegram\'s moderators. It can take upto 72h or more than it."
    ln_break = "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
    data_str = f"⚠️ **ProfessorBot\'s Mass Report Tool** ⚠️\n\n❕**Type:** {type}\n{ln_break}\n\n{user_info}\n{ln_break}\n\n❗️**Reason:** {str(reason)}\n\n🌎 **Data centre ID:** `5`\n\n👥 **Number of IDs on server:** `384`\n\n{caution_str}\n\n"
    await eor(event, data_str)

# Updates the text
#def update_text(type, usr, reason, status, process):
	
		
def set_type(t):
    ret_str = ''
    if t == 0:
        ret_str = 'Channel           (✅)\n               Group               (❌)\n               User                 (❌)'
    elif t == 1:
	ret_str = 'Channel           (❌)\n               Group               (✅)\n               User                 (❌)'
    elif t == 2:
	ret_str = 'Channel           (❌)\n               Group               (❌)\n               User                 (✅)'
    else:
	ret_str = '❌ Something went wrong!'
    return ret_str

def set_user(u):
    username = u.username
    first_name = u.first_name
    last_name = u.last_name
    usrname = "@{}".format(username) if username else ("This user doesn't have username")
    first_name = (
        first_name.replace("\u2060", "") if first_name else ("This user doesn't have name")
    )
    last_name = (
        last_name.replace("\u2060", "") if last_name else ("")
    )
    ret_str = f"👤 **User info:**\n          **__User ID:__** {str(u.id)}\n          **__Name:__** {first_name} {last_name}\n          **__Username:__** {username}\n          **__Bot:__** {str(u.bot)}\n          **__Restricted:__** {str(u.restricted)}\n          **__Verified by Telegram:__** {str(u.verified)}"
    return ret_str


async def get_user_from_event(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit('Pass the user\'s username/id/reply whom has to be mass repored!')
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Could not fetch info of that user. Kindly re-check the parameters provided!")
            return None
    return user_obj, extra


CmdHelp("mass_report").add_command(
    "mass_report", "<reply/username/id> <reason>", "Mass reports the provided user\'s ID."
).add
