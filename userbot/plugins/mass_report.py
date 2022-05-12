from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from mafiabot import CmdHelp

@bot.on(admin_cmd(pattern="mass_report$", outgoing=True))
@bot.on(sudo_cmd(pattern="mass_report$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await eor(event, "**Welcome to ProfessorBot\'s Mass Report tool!**")

CmdHelp("mass_report").add_command(
  "mass_report", "<reply/username/id> <reason>", "Mass reports the provided user\'s ID."
).add