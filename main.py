from instagrapi import Client
import time
import random

cl = Client()
cl.login_by_sessionid("70186756947%3Ao7Z3NJUEmo9Zpm%3A16%3AAYfxR4BsaMfNBqubxVGlkVDvQEe6RGAIgDH0wG_4pw")  # apna sessionid yahaan daalo

GROUP_THREAD_ID = "31379199815012413"  # yeh tumhara group thread ID hai

group_names = [
    "BLACK TERI MA CHUDI🧜🏼‍♂️",
    "BLACK TERI MA CHUDI🧚🏼‍♂️",
    "BLACK TERI MA CHUDI🧞‍♂️",
    "BLACK TERI MA CHUDI🧝🏼‍♂️",
    "BLACK TERI MA CHUDI🧙🏼‍♂️",
    "BLACK TERI MA CHUDI🧛🏼‍♂️",
    "BLACK TERI MA CHUDI🧟‍♂️",
    "BLACK TERI MA CHUDI🦸🏼‍♂️",
    "BLACK TERI MA CHUDI🦹🏼‍♂️",
    "BLACK TERI MA CHUDI👰"
]

def change_group_name_loop():
    while True:
        try:
            new_name = random.choice(group_names)
            cl.direct_thread_update_title(GROUP_THREAD_ID, new_name)
            print(f"✅ GC name changed to: {new_name}")
            time.sleep(random.randint(5, 10))  # har 10-25 sec baad change
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(5)

change_group_name_loop()
