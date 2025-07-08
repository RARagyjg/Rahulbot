from instagrapi import Client
import time
import random
import uuid
import threading
from keep_alive import keep_alive
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# =================== CONFIG ===================
TELEGRAM_BOT_TOKEN = "8054752328:AAHW91DOipkoYVHVZuOBB5VId_DB9OTjRCw"
TELEGRAM_USER_ID = 8054752328  # Your Telegram ID
INSTAGRAM_SESSION_ID = "70186756947%3A1xUHrnycRpNIUj%3A18%3AAYcqUE-KLgHboplrwV_1GJDaH0kGQeWpZjbfehXu0A"
# ==============================================

keep_alive()

# ✅ Login to Instagram
cl = Client()
cl.login_by_sessionid(INSTAGRAM_SESSION_ID)
print(f"✅ Logged in IG as: {cl.user_id}")

# 🌐 GC Info
gc_thread_id = None
spamming = False

# 🔍 Get Group Chat ID
def get_gc_id():
    try:
        threads = cl.direct_threads(amount=5)
        for thread in threads:
            if thread.is_group:
                print(f"✅ Found GC: {thread.id}")
                return thread.id
    except Exception as e:
        print(f"⚠️ Failed to fetch GC ID: {e}")
    return None

# 🔁 Spam Loop
def spam_loop():
    global spamming, gc_thread_id
    while spamming:
        try:
            if not gc_thread_id:
                gc_thread_id = get_gc_id()
                if not gc_thread_id:
                    print("❌ GC ID not found. Retrying in 15s.")
                    time.sleep(15)
                    continue

            uid = uuid.uuid4().hex[:6]
            msg = f"""
🔥🔥 SPAM MESSAGE ID: {uid}
Teri maa ke ashiq: {uid}
🤣 BKL Mode On
"""
            cl.direct_answer(gc_thread_id, msg.strip())
            print(f"✔️ Sent:\n{msg}")
            time.sleep(random.randint(10, 15))
        except Exception as e:
            print(f"⚠️ Error during spam loop: {e}")
            time.sleep(30)

# 🚀 Telegram Commands
async def startspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global spamming, gc_thread_id
    if update.effective_user.id != TELEGRAM_USER_ID:
        return

    if not gc_thread_id:
        gc_thread_id = get_gc_id()

    if not gc_thread_id:
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="❌ No GC found.")
        return

    if not spamming:
        spamming = True
        threading.Thread(target=spam_loop).start()
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="🚀 Started spamming messages!")
    else:
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="⚠️ Already spamming!")

async def stopspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global spamming
    if update.effective_user.id != TELEGRAM_USER_ID:
        return

    if spamming:
        spamming = False
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="🛑 Spamming stopped.")
    else:
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="ℹ️ Already stopped.")

# 🧠 Bot Setup
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("startspam", startspam))
app.add_handler(CommandHandler("stopspam", stopspam))

print("🚀 Bot is running...")
app.run_polling()
