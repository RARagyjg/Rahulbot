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
TELEGRAM_USER_ID = 8054752328  # Replace with your Telegram user ID
INSTAGRAM_SESSION_ID = "70186756947%3A1xUHrnycRpNIUj%3A18%3AAYcqUE-KLgHboplrwV_1GJDaH0kGQeWpZjbfehXu0A"
# ==============================================

# 🌐 Start web server for Render
keep_alive()

# 📲 Setup Instagram
cl = Client()
cl.login_by_sessionid(INSTAGRAM_SESSION_ID)
print(f"✅ Logged in IG as: {cl.user_id}")

# 🔁 GC Thread ID holder
gc_thread_id = None
spamming = False

# 🔍 Get GC ID
def get_gc_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# 📩 Spam Loop
def spam_loop():
    global spamming
    while spamming:
        try:
            uid = uuid.uuid4().hex[:6]
            long_msg = f"""
🔥🔥 SPAM MESSAGE ID: {uid}
Teri maa ke ashiq: {uid}
🤣 BKL Mode On
"""
            cl.direct_answer(gc_thread_id, long_msg.strip())
            print(f"✔️ Sent:\n{long_msg}")
            time.sleep(random.randint(10, 15))
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# 🎮 Telegram Commands
async def startspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global spamming, gc_thread_id
    if update.effective_user.id != TELEGRAM_USER_ID:
        return
    if not gc_thread_id:
        gc_thread_id = get_gc_id()
    if not gc_thread_id:
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="❌ GC not found.")
        return
    if not spamming:
        spamming = True
        threading.Thread(target=spam_loop).start()
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="🚀 Started spamming!")
    else:
        await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="⚠️ Already spamming!")

async def stopspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global spamming
    if update.effective_user.id != TELEGRAM_USER_ID:
        return
    spamming = False
    await context.bot.send_message(chat_id=TELEGRAM_USER_ID, text="🛑 Stopped spamming.")

# 🛠️ Telegram Bot Setup (NO Updater used!)
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("startspam", startspam))
app.add_handler(CommandHandler("stopspam", stopspam))

print("🚀 Bot is running...")
app.run_polling()
