# keep_alive.py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "✅ LIVE HU GANDU"

def keep_alive():
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
