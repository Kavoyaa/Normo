# Ignore this file, just something I use for hosting
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Normal Bot : ONLINE"

def run():
  app.run(host='0.0.0.0',port=8080)

def webserver():
    t = Thread(target=run)
    t.start()
			