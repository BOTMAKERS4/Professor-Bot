import asyncio
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(event, "`Testing ProfessorBot`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ProfessorBot.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ProfessorBot..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ProfessorBot...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ProfessorBot....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing ProfessorBot.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "Test Successful!")
        await asyncio.sleep(4)
        await edit_or_reply(event, "`Generating Output`\nPlease wait...")
        await asyncio.sleep(2)
        await edit_or_reply(event, "Output Generated Successfully!")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**Saving Output To ProfessorBot\'s Local Database...**")
        await asyncio.sleep(3.5)
        await edit_or_reply(event,
            "Your [ProfessorBot](https:/t.me/harshjais369) is working fine!\n       Contact @harshjais369 for any assistance.\n\n**ᴮᵒᵗ ⁾⁾**  ᴹᵃᶠⁱᵃᴮᵒᵗ ⁽ᵇʸ ᴴⁱᵐᵃⁿˢʰᵘ⁾\n**ᴿᵉ⁻ᵉⁿᵍⁱⁿᵉᵉʳᵉᵈ ᵃˢ ⁾⁾**  ᴾʳᵒᶠᵉˢˢᵒʳᴮᵒᵗ ⁽ᵇʸ ᴴᵃʳˢʰ ᴶᵃⁱˢʷᵃˡ⁾"
        )

CmdHelp("test").add_command(
  "test", None, "Test weather your bot is running or not."
).add()
