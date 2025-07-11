from instagrapi import Client
import time
import random
from datetime import datetime
from keep_alive import keep_alive  # Make sure you have keep_alive.py

# 🔌 Keep Alive for hosting (like Repl.it or Render)
keep_alive()

# 🔐 Login using session ID
cl = Client()
cl.login_by_sessionid("70186756947%3AKZo0To6sb4I8i8%3A16%3AAYeGK-f0NNmxZmxJXFk3sIlZ_DywHJ_ZVgZ2wM7ufg")  # Replace with your real session ID

print(f"✅ Logged in as @{cl.username} (ID: {cl.user_id})")

# 💬 Create spam message with random length and time+date footer
def create_spam_message():
    line = "BLACK KI MA KI BOOR KA KHUN PILUGA_____///"
    repeat_count = random.randint(10, 50)  # Random message size
    lines = [line] * repeat_count
    
    # Add time and date at the end
    current_time = datetime.now().strftime("🕒 %I:%M %p | 📅 %d %B")
    lines.append(current_time)
    
    return '\n'.join(lines)

# 🔁 Auto spam loop
def auto_spam():
    while True:
        try:
            threads = cl.direct_threads(amount=1)  # Top 5 recent chats (DMs/GCs)
            for thread in threads:
                msg = create_spam_message()
                try:
                    typing_time = round(random.uniform(1.5, 4.0), 2)
                    print(f"⌨️ Typing to {thread.id}... ({typing_time}s)")
                    time.sleep(typing_time)
                    cl.direct_send(msg, [thread.id])
                    print(f"✅ Sent spam to {thread.id}")
                except Exception as e:
                    print(f"❌ Send failed in {thread.id}: {e}")
                time.sleep(random.randint(10, 20))  # Wait before next chat
            time.sleep(random.randint(20, 40))  # Delay before repeating loop
        except Exception as err:
            print(f"⚠️ Main loop error: {err}")
            time.sleep(30)  # Wait before retrying if there's an error

# 🚀 Start bot
auto_spam()
