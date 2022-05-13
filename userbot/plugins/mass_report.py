from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp

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
    await eor(event, f"**Welcome to ProfessorBot\'s Mass Report tool!**\n{str(user.id)}\n{str(user.first_name)}\n`{reason}`")


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
