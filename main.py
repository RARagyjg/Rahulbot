from instagrapi import Client
import time
import random
import uuid
from datetime import datetime
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("70186756947%3A1xUHrnycRpNIUj%3A18%3AAYeQTvXThYFKFZY12jDg6kJAspRCSfYBarfP8Aq68A")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# 🔥 Heart emojis
hearts = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎"]

# ✅ Message reply templates
reply_templates_master = [
    """𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 UID:{uid} 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇 {emojis} [{time}]
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇 UID:{uid} {emojis} [{time}]""",

    """𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 UID:{uid} 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 {emojis} [{time}]
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜 UID:{uid} {emojis} [{time}]"""
]

last_msg_id_by_user = {}
user_reply_history = {}

def get_random_emojis(count=5):
    return "".join(random.sample(hearts, count))

def get_next_reply(username, history):
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    reply = random.choice(possible_replies)
    history.add(reply)
    uid = uuid.uuid4().hex[:6]
    emojis = get_random_emojis()
    current_time = datetime.now().strftime("%H:%M:%S")
    return reply.replace("{user}", username).replace("{uid}", uid).replace("{emojis}", emojis).replace("{time}", current_time)

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=1)

            for thread in threads:
                if not thread.messages:
                    continue

                latest_msg = thread.messages[0]

                if latest_msg.user_id == me_id:
                    continue

                user_id = latest_msg.user_id
                username = cl.user_info(user_id).username

                if last_msg_id_by_user.get(user_id) == latest_msg.id:
                    continue

                if user_id not in user_reply_history:
                    user_reply_history[user_id] = set()

                reply = get_next_reply(username, user_reply_history[user_id])

                try:
                    # ⌨️ Typing effect
                    typing_delay = random.uniform(1.5, 3.5)
                    print(f"⌨️ Typing to @{username}... ({typing_delay:.2f}s)")
                    time.sleep(typing_delay)

                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(11, 22))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(12, 23))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(10, 20))

# 🚀 Start bot
auto_reply()
