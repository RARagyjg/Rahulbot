from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75694570387%3A56oKsATvfdlgmR%3A9%3AAYg7_-pj83XoMqfCZLw5O8zQSl-b5xFVXxVaiSMsfQ")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates (edit if you want)
reply_templates_master = [
    """-/:

𝗢𝗠𝗔 𝗧𝗘𝗥𝗜𝗜𝗜𝗜 𝗠𝗔𝗔𝗔 𝗞𝗜 𝗕𝟬𝟬𝗥𝗥 𝗙𝗔𝗔𝗗 𝗗𝗨?




𝗢𝗠𝗔 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔 𝗞𝗜 𝗫𝗛𝗨𝗧𝗧 𝗔𝗨𝗝𝗟𝗔 𝗣𝗔𝗣𝗔 𝗠𝗔𝗥𝗔?




𝗢𝗠𝗔 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔 𝗞𝗬𝗨 𝗖𝗛𝟬𝟬𝗗𝗜 𝗔𝗨𝗝𝗟𝗔 𝗣𝗔𝗣𝗔 𝗦𝗘😂



𝗢𝗠𝗔 𝗚𝗥𝗘𝗘𝗕 𝗞 𝗕𝗔𝗖𝗛𝗘 𝗔𝗔𝗕 𝗙𝗥 𝗦𝗘 𝗛𝗔𝗪𝗔𝗕𝗔𝗝𝗜 𝗞𝗥𝗡𝗘 𝗟𝗔𝗚𝗔??



𝗔𝗨𝗧𝗢 𝗥𝗘𝗣𝗟𝗬  𝗞𝗔 𝗗𝗔𝗠𝗠 𝗟𝗚𝗔 𝗢𝗠𝗔 𝗨𝗥𝗙 𝗗𝗔𝗥𝗦𝗛𝗔𝗡 𝗕𝗛𝗔𝗕𝗛𝗜 😂


-_>""",
]

# 💬 Thread ID (GC ya user chat jisme msg bhejna hai)
TARGET_THREAD_ID = "2859303934258963"  # 👈 apna GC thread ID daalo

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
