import os
import requests
from Telegram_bot.wireguard_generator import generate_wireguard_uri

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Replace with your channel's chat ID

def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    response.raise_for_status()

if __name__ == "__main__":
    try:
        uri = generate_wireguard_uri()
        send_message(f"New WireGuard Configuration URI:\n\n{uri}")
    except Exception as e:
        print(f"Error: {e}")
