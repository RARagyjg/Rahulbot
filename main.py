from instagrapi import Client
import time
import random
from keep_alive import keep_alive

# 🟢 Start KeepAlive server (for UptimeRobot etc.)
keep_alive()

# 🔐 Login via session ID
cl = Client()
cl.login_by_sessionid("75309383775%3Az1z25ktGCMVnqP%3A12%3AAYeep3iLhSUzuz2XDibM8t17pGHUs9-su_iQJCaiDw")  # <-- Replace karo

# 🤖 Bot Info
me_id = cl.user_id
print(f"🤖 Bot running as: {cl.username} (User ID: {me_id})")

# ✅ Track replied message IDs
replied_msg_ids = set()

# 💬 Random replies
replies = [
    "Hey! 👋 TERI MA KA BOXDA FATA NICK MC",
    "Thanks , TERI MA KI CHUT DILANE KE LIYE🤖",
    "TERI MA KA BOXDA FAD DU?",
]

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)

            for thread in threads:
                if not thread.messages:
                    continue

                for msg in thread.messages[:3]:  # Last 5 messages
                    if msg.id in replied_msg_ids:
                        continue

                    if msg.user_id == me_id:
                        continue  # Ignore apne messages

                    try:
                        reply_msg = random.choice(replies)
                        cl.direct_answer(thread.id, reply_msg)
                        print(f"✔️ Replied to user {msg.user_id} in thread {thread.id}: {reply_msg}")
                        replied_msg_ids.add(msg.id)

                        # ⏳ Random delay per reply (to avoid spam flag)
                        time.sleep(random.randint(30, 60))

                    except Exception as e:
                        print(f"⚠️ Error replying to thread {thread.id}: {e}")

            time.sleep(random.randint(15, 30))  # ⏱️ Wait between thread checks

        except Exception as main_e:
            print(f"🚨 Main loop error: {main_e}")
            time.sleep(60)

# 🚀 Start Bot
auto_reply()
