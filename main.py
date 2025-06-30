from instagrapi import Client
import time
import random
from keep_alive import keep_alive

# ✅ Start background keep-alive server (Render/UptimeRobot)
keep_alive()

# 🔐 Login with session ID
cl = Client()
cl.login_by_sessionid("75330318477%3AGuq4jrQuGaX4nk%3A0%3AAYf3r0oRCLBxwtDkSrBXL4GHv04_AqEpHE6kvMmy9g")  # ← Replace karo

# 🤖 Bot info
me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Store replied message IDs
replied_msg_ids = set()

# ✉️ Safe, polite messages (change if you want)
reply_templates = [
    "Oye @{user}, Tu chutiya hai 🤣",
    "Oye @{user}, Gndu msg mat kr❤️",
    "Oye @{user}, Gnd Fadu teri? 🙄"
]

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)

            for thread in threads:
                if not thread.messages:
                    continue

                msg = thread.messages[0]  # Only check latest
                if msg.id in replied_msg_ids:
                    continue
                if msg.user_id == me_id:
                    continue

                username = cl.user_info(msg.user_id).username
                reply = random.choice(reply_templates).replace("{user}", username)

                try:
                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    replied_msg_ids.add(msg.id)
                    time.sleep(random.randint(10, 20))  # safe reply delay

                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(45, 70))  # Wait before next scan

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(60)

# 🚀 Run the bot
auto_reply()
