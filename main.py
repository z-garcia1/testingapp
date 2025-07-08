import threading
import webview
from app import app
import time

def run_flask():
    app.run(debug=False, port=5003, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    time.sleep(2)
    webview.create_window("Prompt Repository", "http://localhost:5003", width=1200, height=800)
    try:
        webview.start(gui='edgechromium')
    except Exception:
        webview.start(gui='winforms')
    threading.Event().wait()

