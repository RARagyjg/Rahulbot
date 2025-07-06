from keep_alive import keep_alive
keep_alive()

from instagrapi import Client
import time
import random
import uuid  # For generating unique IDs

# 🔐 Login
cl = Client()
cl.login_by_sessionid("75899522429%3AKKhY3DfHuLgqp7%3A8%3AAYdVPKkEXV9h4j8392QoktVNjM-ghHZweTROm_1GLg")  # Replace with actual session ID

# 🔁 Get Group Chat ID
def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# 🔥 Message spam with unique ID
gc_thread_id = get_gc_thread_id()

if gc_thread_id:
    print(f"🚀 Spamming started in group: {gc_thread_id}")
    while True:
        try:
            unique_id = uuid.uuid4().hex[:8]  # Short random ID
            message = f"""𝐒𝐔𝐁𝐇𝐀𝐍𝐒 ➪𝗞𝗔𝗠𝗝𝗢𝗥 𝗕𝗔𝗔𝗣 𝗞𝗜 𝗞𝗔𝗠𝗝𝗢𝗥 𝗔𝗨𝗟𝗔𝗗 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧𝗧𝗧𝗧 𝗙𝗔𝗔𝗗𝗗𝗗𝗗 𝗗𝗨𝗚𝗔𝗔𝗔𝗔

✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎
𝐒𝐔𝐁𝐇𝐀𝐍𝐒 ➪𝗞𝗔𝗠𝗝𝗢𝗥 𝗕𝗔𝗔𝗣 𝗞𝗜 𝗞𝗔𝗠𝗝𝗢𝗥 𝗔𝗨𝗟𝗔𝗗 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧𝗧𝗧𝗧 𝗙𝗔𝗔𝗗𝗗𝗗𝗗 𝗗𝗨𝗚𝗔𝗔𝗔𝗔

✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎
𝐒𝐔𝐁𝐇𝐀𝐍𝐒 ➪𝗞𝗔𝗠𝗝𝗢𝗥 𝗕𝗔𝗔𝗣 𝗞𝗜 𝗞𝗔𝗠𝗝𝗢𝗥 𝗔𝗨𝗟𝗔𝗗 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧𝗧𝗧𝗧 𝗙𝗔𝗔𝗗𝗗𝗗𝗗 𝗗𝗨𝗚𝗔𝗔𝗔𝗔

✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎
𝐒𝐔𝐁𝐇𝐀𝐍𝐒 ➪𝗞𝗔𝗠𝗝𝗢𝗥 𝗕𝗔𝗔𝗣 𝗞𝗜 𝗞𝗔𝗠𝗝𝗢𝗥 𝗔𝗨𝗟𝗔𝗗 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧𝗧𝗧𝗧 𝗙𝗔𝗔𝗗𝗗𝗗𝗗 𝗗𝗨𝗚𝗔𝗔𝗔𝗔

✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎✿︎
𝐒𝐔𝐁𝐇𝐀𝐍𝐒 ➪𝗞𝗔𝗠𝗝𝗢𝗥 𝗕𝗔𝗔𝗣 𝗞𝗜 𝗞𝗔𝗠𝗝𝗢𝗥 𝗔𝗨𝗟𝗔𝗗 𝗧𝗘𝗥𝗜𝗜𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧𝗧𝗧𝗧 𝗙𝗔𝗔𝗗𝗗𝗗𝗗 𝗗𝗨𝗚𝗔𝗔𝗔𝗔 \n\nID: {unique_id}"""
            cl.direct_answer(gc_thread_id, message)
            print(f"✔️ Sent: {message}")
            time.sleep(random.randint(10, 20))  # Safe delay
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)
else:
    print("❌ Group chat not found.")
