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

# ✅ Message reply templates (edit if you want)
reply_templates_master = [
    """𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/""",
    """𝕂𝕐𝔸 𝔹ℍℕ 𝕂𝔼 𝕃ℕ𝔻 𝕋𝔼ℝ𝕀 𝕄𝔸𝔸 𝕂𝕐𝕌 𝔹ℍ𝔸𝔾𝕀 ________________________________________/
𝔹ℍ𝔸𝔾 𝕄𝔸𝕋𝕋 𝕋𝔼ℝ𝕐𝕐 𝕄𝔸 𝕂𝕀 ℂℍ𝕌𝕋𝕋 ℝ𝕆ℤ ℂℍ𝕆𝔻𝕌𝔾𝔸___________________________/
𝕂𝕐𝔸 𝔹ℍℕ 𝕂𝔼 𝕃ℕ𝔻 𝕋𝔼ℝ𝕀 𝕄𝔸𝔸 𝕂𝕐𝕌 𝔹ℍ𝔸𝔾𝕀 ________________________________________/
𝔹ℍ𝔸𝔾 𝕄𝔸𝕋𝕋 𝕋𝔼ℝ𝕐𝕐 𝕄𝔸 𝕂𝕀 ℂℍ𝕌𝕋𝕋 ℝ𝕆ℤ ℂℍ𝕆𝔻𝕌𝔾𝔸___________________________/
𝕂𝕐𝔸 𝔹ℍℕ 𝕂𝔼 𝕃ℕ𝔻 𝕋𝔼ℝ𝕀 𝕄𝔸𝔸 𝕂𝕐𝕌 𝔹ℍ𝔸𝔾𝕀 ________________________________________/
𝔹ℍ𝔸𝔾 𝕄𝔸𝕋𝕋 𝕋𝔼ℝ𝕐𝕐 𝕄𝔸 𝕂𝕀 ℂℍ𝕌𝕋𝕋 ℝ𝕆ℤ ℂℍ𝕆𝔻𝕌𝔾𝔸___________________________/
𝕂𝕐𝔸 𝔹ℍℕ 𝕂𝔼 𝕃ℕ𝔻 𝕋𝔼ℝ𝕀 𝕄𝔸𝔸 𝕂𝕐𝕌 𝔹ℍ𝔸𝔾𝕀 ________________________________________/
𝔹ℍ𝔸𝔾 𝕄𝔸𝕋𝕋 𝕋𝔼ℝ𝕐𝕐 𝕄𝔸 𝕂𝕀 ℂℍ𝕌𝕋𝕋 ℝ𝕆ℤ ℂℍ𝕆𝔻𝕌𝔾𝔸___________________________/
𝕂𝕐𝔸 𝔹ℍℕ 𝕂𝔼 𝕃ℕ𝔻 𝕋𝔼ℝ𝕀 𝕄𝔸𝔸 𝕂𝕐𝕌 𝔹ℍ𝔸𝔾𝕀 ________________________________________/
𝔹ℍ𝔸𝔾 𝕄𝔸𝕋𝕋 𝕋𝔼ℝ𝕐𝕐 𝕄𝔸 𝕂𝕀 ℂℍ𝕌𝕋𝕋 ℝ𝕆ℤ ℂℍ𝕆𝔻𝕌𝔾𝔸___________________________/""",
"""𝙏𝙀𝙍𝙄𝙄𝙄 𝙈𝘼𝘼𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝘼𝙋𝙉𝙀 𝙇𝙉𝘿 𝙎𝙀 𝙍𝙊𝙕 𝘾𝙃𝙊𝘿𝙐𝙂𝘼__________________________________/
𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝙍𝘼*𝙋𝙀 𝙆𝙍𝘿𝙐𝙂𝘼 _______________________________________________/
𝙏𝙀𝙍𝙄𝙄𝙄 𝙈𝘼𝘼𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝘼𝙋𝙉𝙀 𝙇𝙉𝘿 𝙎𝙀 𝙍𝙊𝙕 𝘾𝙃𝙊𝘿𝙐𝙂𝘼__________________________________/
𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝙍𝘼*𝙋𝙀 𝙆𝙍𝘿𝙐𝙂𝘼 _______________________________________________/
𝙏𝙀𝙍𝙄𝙄𝙄 𝙈𝘼𝘼𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝘼𝙋𝙉𝙀 𝙇𝙉𝘿 𝙎𝙀 𝙍𝙊𝙕 𝘾𝙃𝙊𝘿𝙐𝙂𝘼__________________________________/
𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝙍𝘼*𝙋𝙀 𝙆𝙍𝘿𝙐𝙂𝘼 _______________________________________________/
𝙏𝙀𝙍𝙄𝙄𝙄 𝙈𝘼𝘼𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝘼𝙋𝙉𝙀 𝙇𝙉𝘿 𝙎𝙀 𝙍𝙊𝙕 𝘾𝙃𝙊𝘿𝙐𝙂𝘼__________________________________/
𝙏𝙀𝙍𝙄 𝙈𝘼 𝙆𝘼 𝙍𝘼*𝙋𝙀 𝙆𝙍𝘿𝙐𝙂𝘼 _______________________________________________/
𝙏𝙀𝙍𝙄𝙄𝙄 𝙈𝘼𝘼𝘼 𝙆𝘼 𝘽𝙃𝙊𝙎𝘿𝘼 𝘼𝙋𝙉𝙀 𝙇𝙉𝘿 𝙎𝙀 𝙍𝙊𝙕 𝘾𝙃𝙊𝘿𝙐𝙂𝘼__________________________________/"""
]

# 🧠 Maintain last message replied for each user
last_msg_id_by_user = {}

def get_next_reply(username, history):
    # Filter replies jo already iss user ko bheje gaye ho
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    reply = random.choice(possible_replies)
    history.add(reply)
    return reply.replace("{user}", username)

user_reply_history = {}

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)

            for thread in threads:
                if not thread.messages:
                    continue

                latest_msg = thread.messages[0]

                # Apna msg ignore karo
                if latest_msg.user_id == me_id:
                    continue

                user_id = latest_msg.user_id
                username = cl.user_info(user_id).username

                # Agar same msg pe already reply kar chuke ho, skip karo
                if last_msg_id_by_user.get(user_id) == latest_msg.id:
                    continue

                # User history init if not exists
                if user_id not in user_reply_history:
                    user_reply_history[user_id] = set()

                # 📨 Generate new random reply
                reply = get_next_reply(username, user_reply_history[user_id])

                try:
                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(8, 14))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(30, 60))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(30, 60))

# 🚀 Start bot
auto_reply()
