from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75330318477%3AHu5fuxTOngcixl%3A11%3AAYdN5gcDKa0N9sV90Sa1X8Vl_uycGbMmGZSDWHudew")  # 🔐 Replace with your real session ID

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Friendly reply templates
reply_templates = [
    """ 𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/""",
    """ℕ𝕀ℂ𝕂➪𝕂𝕀 𝕄𝕌𝕄𝕄𝕐 𝕂𝕆 ℝ𝕆ℤ 𝕃𝕌ℕ𝔻 ℂℍ𝕌𝕊𝕋𝕀 ℍ 𝕄𝔸𝕁𝔼 𝕊𝔼 _________________________✓
ℕ𝕚ℂ𝕂 𝕂𝕀 𝔹ℍ𝔼ℕ 𝕂𝕀 ℂℍ𝕌𝕋 𝔹𝔸ℍ𝕌𝕋 𝕄𝔸𝕊𝕋 ℍ𝔸𝕀_______________________________________________________________✓
ℕ𝕀ℂ𝕂➪𝕂𝕀 𝕄𝕌𝕄𝕄𝕐 𝕂𝕆 ℝ𝕆ℤ 𝕃𝕌ℕ𝔻 ℂℍ𝕌𝕊𝕋𝕀 ℍ 𝕄𝔸𝕁𝔼 𝕊𝔼 _________________________✓
ℕ𝕚ℂ𝕂 𝕂𝕀 𝔹ℍ𝔼ℕ 𝕂𝕀 ℂℍ𝕌𝕋 𝔹𝔸ℍ𝕌𝕋 𝕄𝔸𝕊𝕋 ℍ𝔸𝕀_______________________________________________________________✓
ℕ𝕀ℂ𝕂➪𝕂𝕀 𝕄𝕌𝕄𝕄𝕐 𝕂𝕆 ℝ𝕆ℤ 𝕃𝕌ℕ𝔻 ℂℍ𝕌𝕊𝕋𝕀 ℍ 𝕄𝔸𝕁𝔼 𝕊𝔼 _________________________✓
ℕ𝕚ℂ𝕂 𝕂𝕀 𝔹ℍ𝔼ℕ 𝕂𝕀 ℂℍ𝕌𝕋 𝔹𝔸ℍ𝕌𝕋 𝕄𝔸𝕊𝕋 ℍ𝔸𝕀_______________________________________________________________✓
ℕ𝕀ℂ𝕂➪𝕂𝕀 𝕄𝕌𝕄𝕄𝕐 𝕂𝕆 ℝ𝕆ℤ 𝕃𝕌ℕ𝔻 ℂℍ𝕌𝕊𝕋𝕀 ℍ 𝕄𝔸𝕁𝔼 𝕊𝔼 _________________________✓
ℕ𝕚ℂ𝕂 𝕂𝕀 𝔹ℍ𝔼ℕ 𝕂𝕀 ℂℍ𝕌𝕋 𝔹𝔸ℍ𝕌𝕋 𝕄𝔸𝕊𝕋 ℍ𝔸𝕀_______________________________________________________________✓
ℕ𝕀ℂ𝕂➪𝕂𝕀 𝕄𝕌𝕄𝕄𝕐 𝕂𝕆 ℝ𝕆ℤ 𝕃𝕌ℕ𝔻 ℂℍ𝕌𝕊𝕋𝕀 ℍ 𝕄𝔸𝕁𝔼 𝕊𝔼 _________________________✓""",
    """𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/

𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/

𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/"""
]

# 🧠 Avoid repeating replies
last_msg_id_by_user = {}
user_reply_history = {}

def get_next_reply(username, history):
    available = [r for r in reply_templates if r not in history]
    if not available:
        history.clear()
        available = reply_templates.copy()
    reply = random.choice(available)
    history.add(reply)
    return reply

def auto_reply():
    gc_thread_id = None  # Optional: set a specific group chat ID if known

    while True:
        try:
            threads = cl.direct_threads(amount=5)  # Lower amount for less load

            for thread in threads:
                if gc_thread_id and thread.id != gc_thread_id:
                    continue  # Skip if not the specific GC

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
                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(20, 40))  # Slower to avoid ban
                except Exception as e:
                    print(f"⚠️ Failed to reply to @{username}: {e}")
                    time.sleep(random.randint(60, 120))

            time.sleep(random.randint(60, 120))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(120, 180))

# 🚀 Start bot
auto_reply()
