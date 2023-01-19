import asyncio
import io
import os
import time
from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest
from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot import CUSTOM_PMPERMIT, MAFIA_ID
from userbot.Config import Config
from mafiabot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

# pmpermit for ProfessorBot.....
# by @harshjais369

ME = bot.uid
PM_TRUE_FALSE = Config.PM_DATA
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
MAFIAPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/8b086b95491df9f0d4f58.jpg"
)
"""
h1m4n5hu0p = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n THIS IS ILLEGAL AND REGARDED AS CRIME"
)
"""
DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else "ProfessorBot User"
USER_BOT_WARN_ZERO = "🛑 **Our AI system has detected you were spamming my master's inbox, henceforth you\'ve been blocked until my master comes back and approve this chat for further conversation.**"
USER_BOT_NO_WARN = (
    "**ProfessorBot Ultra Private Security Protocol ⚠️**\n\n"
    "Greetings, this is an automated AI response protocol by ProfessorBot. Access to this chat is restricted due to an inability to authenticate your identity. Keep in mind, you may be blocked from this potal if you enter wrong commands multiple times."
    "In order to initiate a valid conversation, you need to verify your identity first.\n\n"
    "Send /start - __to start verification__"
)

if Var.MAFIABOT_LOGGER is not None:

    @bot.on(admin_cmd(pattern="a|.allow|.approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        try:
            firstname = replied_user.user.first_name
        except:
            firstname = replied_user.users[0].first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(f"✅ Approved [{firstname}](tg://user?id={chat.id}) to send messages.")
                await asyncio.sleep(5)
                await event.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("⚠️ `Reply to user to approve him !`")
                return
            if not pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                try:
                    firstname = replied_user.user.first_name
                except:
                    firstname = replied_user.users[0].first_name
                pmpermit_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(f"✅ Approved [{firstname}](tg://user?id={reply_s.sender_id}) to PM you.")
                await asyncio.sleep(5)
                await event.delete()
            elif pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit("✅ `User already approved to DM you!`")
                await asyncio.sleep(5)
                await event.delete()

                

    # Approve outgoing
    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "✅ Auto-verified because of outgoing..."
                    rko = await bot.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()

    @bot.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        try:
            firstname = replied_user.user.first_name
        except:
            firstname = replied_user.users[0].first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 881259026:
                await event.edit("⚠️ Sorry, I cannot block my master!\n\nYour userbot access has been taken back for few minutes due to auto detection of violation of ProfessorBot\'s terms of services.")
                time.sleep(500)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(f"❌ Blocked [{firstname}](tg://user?id={chat.id}) to send private messages.")
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))
        elif event.is_group:
            if chat.id == 881259026:
                await event.edit("⚠️ Sorry, I cannot block my master!\n\nYour userbot access has been taken back for few minutes due to auto detection of violation of ProfessorBot\'s terms of services.")
                time.sleep(500)
            else:
                reply_s = await event.get_reply_message()
                if not reply_s:
                    await event.edit("⚠️ `Reply to a user to block him!`")
                    return
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                try:
                    firstname = replied_user.user.first_name
                except:
                    firstname = replied_user.users[0].first_name
                if pmpermit_sql.is_approved(event.chat_id):
                    pmpermit_sql.disapprove(event.chat_id)
                await event.edit(f"❌ Blocked [{firstname}](tg://user?id={reply_s.sender_id}) to send private messages.")
                await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
                await asyncio.sleep(3)
                await event.delete()

    @bot.on(admin_cmd(pattern="da|.disallow|.disapprove ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        try:
            firstname = replied_user.user.first_name
        except:
            firstname = replied_user.users[0].first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 881259026:
                await event.edit("⚠️ You cannot use this command on my master!")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(f"❌ [{firstname}](tg://user?id={chat.id}) disapproved to send messages.")
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("`⚠️ Reply to a user to disapprove him.`")
                return
            if pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                try:
                    firstname = replied_user.user.first_name
                except:
                    firstname = replied_user.users[0].first_name
                pmpermit_sql.disapprove(reply_s.sender_id)
                await event.edit(f"❌ Disapproved [{firstname}](tg://user?id={reply_s.sender_id}) to send you private messages!")
                await asyncio.sleep(3)
                await event.delete()
            elif not pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit("⚠️ `User is not approved yet!`")
                await asyncio.sleep(5)
                await event.delete()
                

    @bot.on(admin_cmd(pattern="la|.listallowed ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Currently approved PMs :\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n")
        else:
            APPROVED_PMs = "No Approved PMs (yet)."
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="[ProfessorBot]Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == ME:
            return
        if Var.MAFIABOT_LOGGER is None:
            return
        if not event.is_private:
            return
        message_text = event.message.message
        chat_id = event.sender_id
        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)
        if chat_id == ME:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if PM_TRUE_FALSE == "DISABLE":
            return
        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_P_M_s:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.MAFIABOT_LOGGER,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except:
                return
        r = await bot.send_file(
            event.chat_id, MAFIAPIC, caption=USER_BOT_NO_WARN, force_document=False
        )
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


# Do not touch the below codes!
@bot.on(events.NewMessage(incoming=True, from_users=(881259026)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "✅ Auto-approved because its my master (@harshjais369)!")
            await bot.send_message(chat, "**Here comes my Master! (@harshjais369)**")


CmdHelp("pmpermit").add_command(
  "a|allow|approve", "<pm use only>", "It allow the user to PM you."
).add_command(
  "da|disallow|disapprove", "<pm use only>", "It disallows the user to PM. If user crosses the PM limit after disallow he/she will get blocked automatically"
).add_command(
  "block", "<pm use only>", "Blocks the user from sending PM\'s"
).add_command(
  "la|listallowed", None, "Gives you the list of allowed PM\'s list"
).add_command(
  "set var PM_DATA", "DISABLE", "Turn off pm protection by your userbot. Your PM will not be protected."
).add()
