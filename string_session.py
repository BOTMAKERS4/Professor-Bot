from telethon.sessions import StringSession
from telethon.sync import TelegramClient
mafia = input("✵ Enter y/yes to continue: ")
if mafia == 'y' or 'yes':
 print("\nPlease go to my.telegram.org and get your API Id and API Hash to proceed.")
print("""\n\nWelcome To ProfessorBot String Session\nGenerator By @harshjais369\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM SESSION STRING\n(Tap to copy it)👇 \n\n `{session}`",
            )

            print(
                "Thanks for Choosing ProfessorBot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number! \n Make sure its with correct country code. Example : +918925534834\n Kindly Retry..."
        )
        print("")
        continue
    break
