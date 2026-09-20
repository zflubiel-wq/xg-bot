from flask import Flask
import threading, requests, time
app = Flask(__name__)
TOKEN = "8723827102:AAE1ArXUAIPf1gAawlWVpWPXVRhfbFbp6J8"
URL = f"https://api.telegram.org/bot{TOKEN}/"
CHAT = "8025817919"
def enviar(t):
    try:
        requests.post(URL+"sendMessage", data={"chat_id": CHAT, "text": t}, timeout=10)
    except:
        pass
def loop():
    off=0
    while True:
        try:
            r=requests.get(URL+f"getUpdates?offset={off}&timeout=20").json()
            for u in r.get("result",[]):
                off=u["update_id"]+1
                if "message" in u and "text" in u["message"]:
                    if "/start" in u["message"]["text"].lower():
                        enviar("✅ BOT 24/7 ACTIVO - Ya no necesitas Pydroid")
        except:
            pass
        time.sleep(2)
threading.Thread(target=loop, daemon=True).start()
@app.route('/')
def h():
    return "VIVO"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
