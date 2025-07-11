from instagrapi import Client
import time
import random
import uuid
from datetime import datetime
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("70186756947%3AKZo0To6sb4I8i8%3A16%3AAYeGK-f0NNmxZmxJXFk3sIlZ_DywHJ_ZVgZ2wM7ufg")  # Replace with your actual session ID

print(f"✅ Logged in as @{cl.username} (ID: {cl.user_id})")

# 🎨 Font styles
font_styles = {
    "bold": str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
        "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘶𝘷𝘄𝘅𝘆𝘇"
    ),
    "double": str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
    )
}

# Emoji options
emojis_list = ["😂", "💀", "🔥", "🤡", "🚀", "🧠", "👻", "❤️", "😎", "🎯", "🖕", "💩", "✨"]

# Stylize one line of message
def stylize(text, style):
    return text.translate(font_styles.get(style, {}))

# 🔁 Create spam message with random size/font/emojis
def create_spam_message():
    base_line = "BLACK KI MA KI BOOR KA KHUN PILUGA_____///"
    repeat_count = random.randint(10, 50)  # Sometimes short, sometimes long
    uid = uuid.uuid4().hex[:6].upper()
    emojis = ''.join(random.sample(emojis_list, 3))
    time_now = datetime.now().strftime("%H:%M:%S")
    font_style = random.choice(["bold", "double"])

    # Stylize each line
    styled_line = stylize(base_line, font_style)
    body = '\n'.join([styled_line] * repeat_count)

    # Add UID, emoji, time at the end
    footer = f"\n\n[ UID: {uid} ] | {emojis} | {time_now}"
    return body + footer

# ♾️ Auto spam main loop
def auto_spam():
    while True:
        try:
            threads = cl.direct_threads(amount=2)  # Top 5 GCs

            for thread in threads:
                msg = create_spam_message()
                try:
                    delay = round(random.uniform(1.5, 4.0), 2)
                    print(f"⌨️ Typing to {thread.id}... ({delay}s)")
                    time.sleep(delay)

                    cl.direct_send(msg, [thread.id])
                    print(f"✅ Sent to {thread.id}")
                except Exception as e:
                    print(f"❌ Error sending to {thread.id}: {e}")

                time.sleep(random.randint(10, 20))  # Between each thread

            time.sleep(random.randint(25, 45))  # Between each round

        except Exception as e:
            print(f"⚠️ Loop error: {e}")
            time.sleep(30)

# 🚀 Start
auto_spam()
