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
            requests.get("https://rahulbot-1-kpox.onrender.com")  # 👈 apna render app URL daalna
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(300)  # every 5 minutes ping

threading.Thread(target=self_ping, daemon=True).start()

# 🔐 Login
cl = Client()
cl.login_by_sessionid("78046309958%3AsF7MFPCDKWcwFD%3A1%3AAYi0bkSm6oT5H7K9aiLHBSkVfFZ4G7OnWMbtGpMShw")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates
reply_templates_master = [
    """OMA/LAHIRU TERI RUNDY MAIYA KE MUH MEI LND DALKR MUTH MARUNGA💋💦-----------------------------------------------------------------------------------------------------------------------------------------------OMA/LAHIRU KI BEHN KE MUH MEI PESAB KARUNGA--------------------------------------------------------------------------------------------OMA/LAHIRU TERI RUNDY MAIYA KE MUH MEI LND DALKR MUTH MARUNGA💋💦----------------------------------------------------------------------------------------------------------------------------------------------OMA/LAHIRU KI BEHN KE MUH MEI PESAB KARUNGA--------------------------------------------------------------------------------------------OMA/LAHIRU TERI MAKI  XHUT MARUNGA KUTIYA KE B33EJJ""",
    """__________

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂

OMA_LAKDIKIKATHIKATHIPER__
GHODA🐴
TERI MA🧕KO_CHODU🍌BANAKAR_GHODA😂 ‌ ‌


😂 OMA_2KODI_KE_SASTE_SAPAMER_TMK🖖 

😂 OMA_RANDI_CHUD🍌KE_BHG_MTT😂"""
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

            time.sleep(random.randint(50, 100))  # 30–60 sec delay
                                 
        except Exception as err:
            print(f"⚠️ Error: {err}")
            time.sleep(random.randint(30, 60))

# 🚀 Start auto message sender
auto_send() 
