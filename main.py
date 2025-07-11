from instagrapi import Client
import time
import random

# Initialize and login
cl = Client()
cl.login_by_sessionid("70186756947%3AKZo0To6sb4I8i8%3A16%3AAYeGK-f0NNmxZmxJXFk3sIlZ_DywHJ_ZVgZ2wM7ufg")  # Replace with your real session ID

# Generate spam message with random length
def create_spam_message():
    base = "BLACK TERI MA KI B00R FAD DUGA"
    repeat_count = random.randint(1, 5)  # Between 1 to 5 repetitions per message
    return " ".join([base] * repeat_count)

# Find group chat thread ID
def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)  # Check last 10 threads
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# Get the GC thread ID
gc_thread_id = get_gc_thread_id()

# Spam 50 messages with delay and random size
if gc_thread_id:
    for i in range(50):
        try:
            msg = create_spam_message()
            cl.direct_answer(gc_thread_id, msg)
            print(f"✔️ [{i+1}/50] Sent: {msg}")
            time.sleep(random.randint(7, 15))  # Delay to avoid spam detection
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)
else:
    print("❌ Group chat not found.")
