from instagrapi import Client
import time
from keep_alive import keep_alive

# 🟢 Start KeepAlive server for Replit 24/7
keep_alive()

# 🔐 Login with Session ID (replace this)
cl = Client()
cl.login_by_sessionid("75330318477%3AGuq4jrQuGaX4nk%3A0%3AAYf3r0oRCLBxwtDkSrBXL4GHv04_AqEpHE6kvMmy9g")

# 🤖 Bot Info
me_id = cl.user_id
print(f"🤖 Bot running as: {cl.username} (User ID: {me_id})")

# ✅ To avoid replying again to the same message
replied_msg_ids = set()

def auto_reply():
    while True:
        threads = cl.direct_threads(amount=10)

        for thread in threads:
            if not thread.messages:
                continue

            for msg in thread.messages[:1]:  # Last 5 msgs check kare
                if msg.id in replied_msg_ids:
                    continue  # Already replied

                if msg.user_id == me_id:
                    continue  # Apne msg skip

                try:
                    # ✉️ Reply to the same thread (GC or DM)
                    cl.direct_answer(thread.id, """AJ TERYY MA KI CH00T FAD DUGA🖤








BHAG MATT TU BETE 🖤


TU CHOTA TATTA H BETE🖤



APNI MA CHUDA KE MANEGA🖤






 TERI MA RAHUL KE LND PE H🖤








 GRIB BHEEK DU BOL RNDI🖤











 GRIB TERI MAA CHUDA MERE SE🖤









TERI MA CHOD KE PAISE DUNGA CHLEGA NA🖤""")
                    print(f"✔️ Replied to user {msg.user_id} in thread {thread.id}")
                    replied_msg_ids.add(msg.id)

                except Exception as e:
                    print(f"⚠️ Error replying to thread {thread.id}: {e}")

        time.sleep(60)

auto_reply()
                    
