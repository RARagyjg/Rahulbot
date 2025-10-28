from instagrapi import Client
import time
import random
from keep_alive import keep_alive
import threading
import requests

# ✅ Start keep-alive server (for Render/UptimeRobot)
keep_alive()

# 🟢 Self-ping system (bot ko idle hone se bachata hai)
def self_ping():
    while True:
        try:
            requests.get("https://rahulbot-1.onrender.com")  # 👈 apna render app URL daalna
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(300)  # every 5 minutes ping

threading.Thread(target=self_ping, daemon=True).start()

# 🔐 Login
cl = Client()
cl.login_by_sessionid("77802598284%3A38M5A0SzWLcqvw%3A4%3AAYh6yiKD0u0La8-wTM9or8oEUlyPtirD7zhGa63XoQ")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates
reply_templates_master = [
    """/silent /silent OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐔𝐆𝐀 𝐁𝐄𝐓𝐄 ________________________________________/
OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/""",
    """/silent /silent 𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣𝗕𝗛𝗔𝗚 𝗠𝗧𝗧😂""",
]

# 💬 Target group chat thread ID
TARGET_THREAD_ID = "2859303934258963"

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

def auto_send():  # 🔁 auto-sender
    while True:
        try:
            if me_id not in user_reply_history:
                user_reply_history[me_id] = set()

            msg = get_next_message(user_reply_history[me_id])
            cl.direct_send(msg, thread_ids=[TARGET_THREAD_ID])
            print(f"📤 Sent auto message: {msg}")

            time.sleep(random.randint(30, 60))  # 30–60 sec delay
        except Exception as err:
            print(f"⚠️ Error: {err}")
            time.sleep(30)

# 🚀 Start auto message sender
auto_send() 
