"""Send Chat Actions
Syntax: .fake_action <option>
        fake_action options: Options for fake_action

typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from userbot.cmdhelp import CmdHelp
    

@borg.on(admin_cmd(pattern="fake_action ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    user, action = await get_user_from_event(event)
    LOGS.info(f"\n{user}\n\n{action}\n")
    if user is None or action is None:
        return
    async with borg.action(user, action):
        await asyncio.sleep(86400)  # type for 10 seconds

@borg.on(admin_cmd("gbam"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "❌ `Warning! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "Reason: __Not given__"
    await event.edit("**❌ G-Banning the user...**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 881259026:
            await reply_message.reply(
                "`Wait a second, this is my master!`\n**How dare you threaten to ban my master!**\n\n__Your account has been hacked! Pay 99$ to my master__ [Harsh Jaiswal](https://t.me/harshjais369) __to release your account__😏"
            )
        else:
            jnl = (
                "❌ `Warning! `"
                "[{}](tg://user?id={})"
                "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                "**Person's Name: ** __{}__\n"
                "**ID: ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim's username:** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim's username:** @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "❌ `Warning! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Not Given `"
        await event.reply(mention)
    await event.delete()


async def get_user_from_event(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).split(" ", 1)
    extra = "typing"
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
            await event.edit("Pass the user's username, id or reply!")
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
            await event.edit("Could not fetch info of that user.")
            return None
    return user_obj, extra


CmdHelp("fake").add_command(
  'fake_action', '<action>', 'This shows the fake action in the group  the actions are typing, contact, game ,location, voice, round, video, photo, document.'
).add_command(
  'gbam', '<reason> (optional)', 'Fake gban. Just for fun! 😂'
).add_command(
  'picgen', None, 'Gives a fake face image.'
).add()
