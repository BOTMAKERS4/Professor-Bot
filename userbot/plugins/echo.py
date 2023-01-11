import asyncio
import base64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from mafiabot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

# Echo remastered by @harshjais369

@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        if is_echo(user_id, chat_id):
            await edit_or_reply(event, "The user is already enabled with echo.")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(event, "Hii....😄🤓")
    else:
        await edit_or_reply(event, "Reply to a User's message to echo his messages.")

@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(event, "Echo has been stopped for the user.")
        else:
            await edit_or_reply(event, "The user is not activated with echo.")
    else:
        await edit_or_reply(event, "Reply to a user's message to echo his messages.")

@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(event):
    if event.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users."
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo enabled users: [here]({url})"
        await edit_or_reply(event, reply_text)
    else:
        await edit_or_reply(event, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(event.sender_id, event.chat_id):
        if event.message.text or event.message.sticker:
            await event.reply(event.message)


CmdHelp("echo").add_command(
  'echo', 'Reply to a user', 'Replays every message from whom you enabled echo'
).add_command(
  'rmecho', 'reply to a user', 'Stop replayings targeted user message'
).add_command(
  'listecho', None, 'Shows the list of users for whom you enabled echo'
).add()
