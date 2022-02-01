"""
.kickme
"""
import time
from telethon.tl.functions.channels import LeaveChannelRequest
from mafiabot.utils import admin_cmd


@borg.on(admin_cmd("kickme", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**Leaving group...\nGroup left successfully!**")
        time.sleep(1)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("**Is this even a group?**")
