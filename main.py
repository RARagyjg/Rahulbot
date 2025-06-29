from instagrapi import Client
import time
import random
from keep_alive import keep_alive

# 🟢 Start keep-alive server (Replit/Render)
keep_alive()

# 🔐 Login using Session ID (replace this)
cl = Client()
cl.login_by_sessionid("75493958004%3AbV7iaCIeGTI5wS%3A14%3AAYeRrHfvsa09Ep78oqBeu84b9ihYOEH3JBV5J5K_Hg")  # Change this

# 🤖 Get bot's user ID
me_id = cl.user_id
print(f"🤖 Bot running as: {cl.username} (User ID: {me_id})")

# ✅ Store already replied message IDs
replied_msg_ids = set()

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)

            for thread in threads:
                if not thread.messages:
                    continue

                last_msg = thread.messages[0]

                if last_msg.id in replied_msg_ids:
                    continue  # Already replied

                if last_msg.user_id == me_id:
                    continue  # Apne msg ko skip

                # 🏷️ Get sender username
                sender_username = cl.user_info(last_msg.user_id).username
                reply_text = f"@{sender_username} Hi! Kese ho bhai"

                try:
                    cl.direct_answer(thread.id, reply_text)
                    print(f"✔️ Replied to @{sender_username} in thread {thread.id}")
                    replied_msg_ids.add(last_msg.id)

                    # ⏱️ Small delay to mimic human behavior
                    time.sleep(random.randint(30, 60))

                except Exception as e:
                    print(f"⚠️ Error replying to thread {thread.id}: {e}")

            time.sleep(random.randint(15, 30))

        except Exception as loop_error:
            print(f"🚨 Loop error: {loop_error}")
            time.sleep(60)

# 🚀 Start the bot
auto_reply()
