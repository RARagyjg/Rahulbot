from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("79069006978%3AqgJhNT5cCtMKV7%3A25%3AAYicCdIZoR-44Bp93j4IknRPea5fEV3xvXVdPTuF8Q")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message templates (edit if you want)
reply_templates_master = [
    """OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  OMA - T E R I M A K B OX DA CH O DU GA  """,
    """OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? OMA- TERII MA CHDKE KYI BHGTI BETE? """
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
