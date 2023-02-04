import asyncio
from telethon import functions
from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot.Config import Config
from . import *

DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else "ProfessorBot User"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.sender_id
    event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
            pm_user_obj = await event.client(functions.users.GetFullUserRequest(chat.id))
            PM = (
                f"__Hey [{pm_user_obj.users[0].first_name}](tg://user?id={chat_id})!__\n__Sorry for the inconvenience, this protocol was implemented by my master ({DEFAULTUSER}) to prevent misleading spams and unwanted users/bots from infiltrating this chat.__"
                "\n\n**Let's make this smooth and choose one of the following reasons which best describes why you are here:**\n\n"
                "`1`. To chat with my master\n"
                "`2`. To inform about something\n"
                "`3`. To enquire something\n"
                "`4`. To request something\n"
                "`5`. Chat with AI bot __(unavailable)__"
            )
            ONE = (
                "__Okay! Your request has been registered. Please do not spam here. You can expect a reply within 24 to 72 hours.__\n\n"
                "** You will be blocked and reported if you spam **\n\n"
                "__Use__ `/start` __to go back to the main menu.__"
            )
            TWO = "**So uncool, this is not your home. Go bother someone else. You have been blocked until further notice.**"
            FOUR = "__Okay! My master has not seen your message yet.__\n__He will respond if he wants so, when he comes back. There\'s already a lot of pending messages.__\n**Please do not spam unless you wish to be blocked and banned from this portal.**"
            FIVE = "`Okay, please have the basic manners as to not bother my master too much. If he wishes to help you, he will respond to you soon.`\n**Do not ask repeatedly else you will be banned from this portal.**"
            LWARN = "⚠ **This is your last warning. If you send another message then you will be blocked and banned from this portal. My Master will respond to you soon. Keep patience..!**"
            WRONG_CMD = "❌ You have sent an invalid command! Please send `/start` to open MENU or-else you could be banned from this portal, unless my master approves you first."

            async with borg.conversation(chat) as conv:
                await borg.send_message(chat, PM)
                chat_id = event.sender_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "1":
                    await borg.send_message(chat, ONE)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        await borg.send_message(chat, WRONG_CMD)
                        await event.delete()
                        await response.delete()
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            await borg.send_message(chat, LWARN)
                            await event.delete()
                            await response.delete()
                            response = await conv.get_response(chat)
                            if not response.text == "/start":
                                await borg.send_message(chat, TWO)
                                await asyncio.sleep(3)
                                await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "2":
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))

                elif y == "3":
                    await borg.send_message(chat, ONE)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        await borg.send_message(chat, WRONG_CMD)
                        await event.delete()
                        await response.delete()
                        response = await conv.get_response(chat)
                        if not response.text == "/start":
                            await borg.send_message(chat, LWARN)
                            await event.delete()
                            await response.delete()
                            response = await conv.get_response(chat)
                            if not response.text == "/start":
                                await borg.send_message(chat, TWO)
                                await asyncio.sleep(3)
                                await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "4":
                    await borg.send_message(chat, ONE)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        await borg.send_message(chat, WRONG_CMD)
                        await event.delete()
                        await response.delete()
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            await borg.send_message(chat, FIVE)
                            await event.delete()
                            await response.delete()
                        response = await conv.get_response(chat)
                        if not response.text == "/start":
                            await borg.send_message(chat, LWARN)
                            await event.delete()
                            await response.delete()
                            response = await conv.get_response(chat)
                            if not response.text == "/start":
                                await borg.send_message(chat, TWO)
                                await asyncio.sleep(3)
                                await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    await borg.send_message(chat, WRONG_CMD)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        await borg.send_message(chat, WRONG_CMD)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            await borg.send_message(chat, LWARN)
                            response = await conv.get_response(chat)
                            if response.text != "/start":
                                await borg.send_message(chat, TWO)
                                await asyncio.sleep(3)
                                await event.client(functions.contacts.BlockRequest(chat_id))
