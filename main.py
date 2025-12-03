from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75330318477%3AGuq4jrQuGaX4nk%3A0%3AAYf3r0oRCLBxwtDkSrBXL4GHv04_AqEpHE6kvMmy9g")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates (edit if you want)
reply_templates_master = [
    "HI I AM RAHUL 🥰",
    "Kya haal hai sabka 😎",
    "Kon online hai 😂"
]

# 💬 Thread ID (GC ya user chat jisme msg bhejna hai)
TARGET_THREAD_ID = "340282366841710300949128XXXXXXXX"  # 👈 apna GC thread ID daalo

# 🧠 Maintain message history
user_reply_history = {}

def get_next_message(history):
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    msg = random.choice(possible_replies)
    history.add(msg)
    return msg

def auto_send():  # 👈 ab ye auto-send hai, reply nahi
    while True:
        try:
            # Initialize history
            if me_id not in user_reply_history:
                user_reply_history[me_id] = set()

            # 📨 Random message select karo
            msg = get_next_message(user_reply_history[me_id])

            # Send message
            cl.direct_send(msg, thread_ids=[TARGET_THREAD_ID])
            print(f"📤 Sent auto message: {msg}")

            # Random delay (change if you want faster/slower)
            time.sleep(random.randint(30, 60))

        except Exception as err:
            print(f"⚠️ Error: {err}")
            time.sleep(30)

# 🚀 Start auto message sender
auto_send()
