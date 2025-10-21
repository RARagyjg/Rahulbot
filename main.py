from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("77802598284%3A38M5A0SzWLcqvw%3A4%3AAYh6yiKD0u0La8-wTM9or8oEUlyPtirD7zhGa63XoQ")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates (edit if you want)
reply_templates_master = [
    """𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣
𝗢𝗠𝗔 𝗚𝗔𝗥𝗘𝗘𝗕 𝗧𝗘𝗥𝗬𝗬𝗬 𝗠𝗔 𝗞𝗜 𝗕𝗨𝗥 𝗙𝗔𝗧 𝗝𝗔𝗬𝗘𝗚𝗜 𝗠𝗔𝗔𝗔𝗗𝗥𝗖𝗛𝗢𝗢𝗗🤣🤣🤣🤣🤣🤣🤣𝗕𝗛𝗔𝗚 𝗠𝗧𝗧😂""",
    """OMA/LAHIRU/CVZII/AARIZ/KAPIL 𝐌𝐀 𝐊𝐈 𝐁𝐎𝐎𝐑 𝐊𝐀 𝐊𝐇𝐔𝐍  𝐏𝐈𝐋𝐔𝐆𝐀______________________________/ 
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
