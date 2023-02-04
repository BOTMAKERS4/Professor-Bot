from telethon import custom, events
from telethon.tl.types import Channel
from telethon.utils import get_display_name
from userbot import bot
from userbot.Config import Config

if Config.TAG_LOGGER:
    taglog_grpid = int(Config.TAG_LOGGER)

if Config.TAG_LOGGER:

    @bot.on(
        events.NewMessage(
            incoming=True,
            blacklist_chats=Config.UB_BLACK_LIST_CHAT,
            func=lambda e: (e.mentioned),
        )
    )
    async def all_messages_catcher(event):
        # the bot might not have the required access_hash to mention the appropriate PM
        try:
            await event.forward_to(Var.TG_BOT_USER_NAME_BF_HER)
        except:
            enn = await bot.get_entity(str(Config.TG_BOT_USER_NAME_BF_HER))
            fwd_to_prfbot = await bot.forward_messages(enn, event.message, silent=True)
        # construct message
        ammoca_message = ""
        tag_usr = await event.client.get_entity(event.sender_id)
        if tag_usr.bot or tag_usr.verified or tag_usr.support:
            return
        tag_usr_pm = f"[{get_display_name(tag_usr)}](tg://user?id={tag_usr.id})"
        where_ = await event.client.get_entity(event.chat_id)
        where_m = get_display_name(where_)
        button_text = "See the tag 📬"
        if isinstance(where_, Channel):
            message_link = f"https://t.me/c/{where_.id}/{event.id}"
        else:
            # not an official link,
            # only works in DrKLO/Telegram,
            # for some reason
            message_link = f"tg://openmessage?chat_id={where_.id}&message_id={event.id}"
            # Telegram is weird :\

        ammoca_message += f"{tag_usr_pm} `just tagged you...` \nWhere?\nIn [{where_m}]({message_link})\n__Tap to go the tagged msg__📬🚶"
        if taglog_grpid is not None:
            await bot.send_message(
                entity=taglog_grpid,
                message=ammoca_message,
                link_preview=False,
                buttons=[[custom.Button.url(button_text, message_link)]],
                silent=True,
            )
        else:
            return
