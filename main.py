from instagrapi import Client
import time
import random
from keep_alive import keep_alive

# 🟢 Start keep-alive (for Render/UptimeRobot)
keep_alive()

# 🔐 Login
cl = Client()
cl.login_by_sessionid("75493958004%3AbV7iaCIeGTI5wS%3A14%3AAYeRrHfvsa09Ep78oqBeu84b9ihYOEH3JBV5J5K_Hg")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Bot running as: {my_username} (User ID: {me_id})")

replied_msg_ids = set()

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)
            replied = False

            for thread in threads:
                if not thread.messages:
                    continue

                for msg in thread.messages[:1]:  # Check latest msg only
                    if msg.id in replied_msg_ids:
                        continue
                    if msg.user_id == me_id:
                        continue
                    
                    sender_username = cl.user_info(msg.user_id).username
                    reply_text = f"@{sender_username} Tu mere l#nd pe h be 😂🤣 "
                    cl.direct_answer(thread.id, reply_text)
                    print(f"✔️ Replied to @{sender_username}")
                    replied_msg_ids.add(msg.id)
                    replied = True
                    time.sleep(random.randint(2, 4))

            if not replied:
                print("⌛ No new messages... waiting.")

            time.sleep(3)  # Only checks every 30 sec (you can increase)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(3)

auto_reply()
