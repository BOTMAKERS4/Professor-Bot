import html

from userbot.cmdhelp import CmdHelp
from userbot import bot, CMD_HELP, ALIVE_NAME
from userbot.plugins.sql_helper.gban_sql import is_gbanned
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply

from telethon import events
from telethon.events import ChatAction
from telethon.utils import get_input_location
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.errors.rpcerrorlist import UserIdInvalidError, MessageTooLongError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest, EditPhotoRequest
from telethon.tl.types import ChatAdminRights, ChannelParticipantsAdmins, ChatBannedRights, MessageEntityMentionName, MessageMediaPhoto


HARSHJ = str(ALIVE_NAME) if ALIVE_NAME else "ProfessorBot user"
papa = borg.uid


async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**Something went wrong**\n`Please provide me a user id.`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**Something went wrong**\nError: ", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@bot.on(admin_cmd(pattern="gban ?(.*)"))
@bot.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        mafiabot = await edit_or_reply(ids, "Trying to gban this user...")
    else:
        mafiabot = await edit_or_reply(ids, "`Ok! GBaning this user...`")
    hum = await userbot.client.get_me()
    await mafiabot.edit(f"`❌ Global Ban is in progress... Please wait!`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await mafiabot.edit(f"**Something went wrong!**")
    if user:
        if user.id == 881259026:
            return await mafiabot.edit(
                f"`First Grow Some Balls To Gban My Creater. 🤫`"
            )
        try:
            from userbot.plugins.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await mafiabot.edit(f"❌ GBaning this user...\n**Please wait few minutes...**")
            except:
                b += 1
    else:
        await mafiabot.edit(f"`Either reply to a user or give me user id/name`")
    try:        
        if gmute(user.id) is False:
            return await mafiabot.edit(f"**Error! User is already GBanned.**")
    except:
        pass
    return await mafiabot.edit(
        f"❌ **[{user.first_name}](tg://user?id={user.id}) has been GBanned successfully!**\nAffected chats: {a}\nBy: [{HARSHJ}](tg://user?id={papa})"
    )

@bot.on(admin_cmd(pattern="ungban ?(.*)"))
@bot.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        mafiabot = await edit_or_reply(ids, "`Trying to ungban this user...`")
    else:
        mafiabot = await edit_or_reply(ids, "`Ungban in progress...`")
    hum = await userbot.client.get_me()
    await mafiabot.edit(f"`Trying to ungban this user...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await mafiabot.edit("**Something went wrong!**")
    if user:
        if user.id == 881259026:
            return await mafiabot.edit("**You need to grow some balls to gban / ungban my creator!**")
        try:
            from userbot.plugins.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await mafiabot.edit(f"Ok! Now Ungbaning this user.\n\n**Please wait few minutes...**")
            except:
                b += 1
    else:
        await mafiabot.edit("**Reply to a user**")     
    try:
        if ungmute(user.id) is False:
            return await mafiabot.edit("**Error! It seems user is already ungbanned.**")
    except:
        pass
    return await mafiabot.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) has been ungbanned now successfully!**\nAffected chats: `{a}`\nBy: [{HarshJ}](tg://user?id={papa})"
    )




@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await event.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    gban_watcher = f"⚠️ **Warning!** `GBanned User Joined the chat!`\n**⚜️ Victim id:**  [{user.first_name}](tg://user?id={user.id})\n\n"
                    gban_watcher += f"**🔥 Action:**  `Banned this user again automatically by` **Professor Bot**!"
                    await event.reply(gban_watcher)
                except BaseException:
                    pass
