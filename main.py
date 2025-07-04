from instagrapi import Client
import time
import random

cl = Client()
cl.login_by_sessionid("75309383775%3AeFIs2q14D1GI4S%3A4%3AAYeBRFQMiFWdojKV8Rm6ql802IcE9UsDYuUFze8bLw")  # Replace with actual session ID

def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

gc_thread_id = get_gc_thread_id()

if gc_thread_id:
    while True:
        try:
            cl.direct_answer(gc_thread_id, """NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////NICK TERI MA KI  FUDI FADU////////////////""")
            print("✔️ Sent to GC!")
            time.sleep(random.randint(10, 20))
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(random.randint(10, 25))
else:
    print("❌ Group chat not found.")
