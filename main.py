from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75330318477%3AsbSTnlpBAo4wb3%3A19%3AAYdMImvDnf0UIcWvQUspr8ErhYviMv1yXwF3UkdUUw")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

reply_templates_master = [
    "Tum Maroge kya khushi ki chumt🤣",
    "Khushi/subhansh chutiye hai na? 😂",
    "Subansh toh mc hai na?",
    "btao na pls khushi rndi h na?😘",
    "Subansh randi ka putt hai na?💀"
]

last_msg_id_by_user = {}
user_reply_history = {}

def get_next_reply(username, history):
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    reply = random.choice(possible_replies)
    history.add(reply)
    return f"@{username} {reply}"  # 🔁 mention user here

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=10)

            for thread in threads:
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
                    time.sleep(random.randint(8, 14))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(30, 60))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(10, 20))

# Start the bot
auto_reply()
