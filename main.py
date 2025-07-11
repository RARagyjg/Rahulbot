from instagrapi import Client
import time
import random
import uuid
from datetime import datetime
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("70186756947%3AKZo0To6sb4I8i8%3A16%3AAYeGK-f0NNmxZmxJXFk3sIlZ_DywHJ_ZVgZ2wM7ufg")

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# 🔥 Heart emojis
hearts = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎"]

# 💬 Message reply templates
reply_templates_master = [
    """BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]BLACK KI MUMMY KI  CHUTT :{uid} FAD DUGA {emojis} [{time}]
BLACK TERYY MAA KI BOOOR KA KHUN PILUGA RNDIKE__________________________________//:{uid} {emojis} [{time}]""",

    """BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]
BLACK TERYYY BHN KI FUDDI MARUUGA SANDE KA TELL LGAKE ____________________________________//:{uid} {emojis} [{time}]"""
]

last_msg_id_by_user = {}
user_reply_history = {}

# 🎨 Font stylizer
def stylize_message(message):
    font_styles = {
        "bold": str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
            "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
        ),
        "italic": str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
            "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
        ),
        "monospace": str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
            "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
        ),
        "double": str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
            "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
        ),
        "fullwidth": str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
            "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
            "０１２３４５６７８９"
        )
    }
    style = random.choice(list(font_styles.values()))
    return message.translate(style)

# ❤️ Random emoji generator
def get_random_emojis(count=5):
    return "".join(random.sample(hearts, count))

# 🧠 Get reply with personalization + font
def get_next_reply(username, history):
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    raw_reply = random.choice(possible_replies)
    history.add(raw_reply)

    uid = uuid.uuid4().hex[:6]
    emojis = get_random_emojis()
    current_time = datetime.now().strftime("%H:%M:%S")

    filled = raw_reply.replace("{user}", username).replace("{uid}", uid).replace("{emojis}", emojis).replace("{time}", current_time)
    return stylize_message(filled)

# 🔁 Main loop
def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=1)

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
                    # ⌨️ Typing effect
                    typing_delay = random.uniform(1.5, 4.5)
                    print(f"⌨️ Typing to @{username}... ({typing_delay:.2f}s)")
                    time.sleep(typing_delay)

                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(11, 22))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(12, 23))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(10, 25))

# 🚀 Start bot
auto_reply()
