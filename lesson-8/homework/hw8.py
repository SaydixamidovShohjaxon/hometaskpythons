# homework 8

# 1

try:
    a = int(input("Son kiriting: "))
    result = a / 0
except ZeroDivisionError:
    print("Xatolik: 0 ga bo‘lish mumkin emas!")


# 2

try:
    number = int(input("Butun son kiriting: "))
except ValueError:
    print("Xatolik: Bu butun son emas!")

# 3

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 4

try:
    x = float(input("1-sonni kiriting: "))
    y = float(input("2-sonni kiriting: "))
    print("Yig'indi:", x + y)
except ValueError:
    raise TypeError("Faqat son kiriting!")


# 5

try:
    with open("/root/secret.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Xatolik: Ruxsat yo'q.")



# 6

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Xatolik: Indeks mavjud emas.")


# 7

try:
    number = input("Son kiriting (Ctrl+C bilan to‘xtatib ko‘ring): ")
except KeyboardInterrupt:
    print("\nXatolik: Foydalanuvchi kiritishni bekor qildi.")


# 8

try:
    result = 10 / 0
except ArithmeticError:
    print("Xatolik: Arifmetik xato (masalan, 0 ga bo‘lish).")



# 9

try:
    with open("somefile.txt", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Xatolik: Unicode kodlashda muammo.")



# 10

try:
    my_list = [1, 2, 3]
    my_list.upper()  # faqat stringda mavjud
except AttributeError:
    print("Xatolik: Bunday metod mavjud emas.")


# Working With files 


# 1

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# 2

n = 3
with open("example.txt", "r") as file:
    for i in range(n):
        print(file.readline().strip())


# 3

with open("example.txt", "a") as file:
    file.write("\nBu yangi qo‘shilgan satr.")

with open("example.txt", "r") as file:
    print(file.read())

# 4

n = 3
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(''.join(lines[-n:]))

# 5

with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)


# 6


with open("example.txt", "r") as file:
    content = file.read()
print(content)




# 8

with open("example.txt", "r") as file:
    words = file.read().split()
    max_len = max(len(word) for word in words)
    longest_words = [w for w in words if len(w) == max_len]
print(longest_words)




# 9

with open("example.txt", "r") as file:
    line_count = sum(1 for line in file)
print("Qatorlar soni:", line_count)




# 10

from collections import Counter

with open("example.txt", "r") as file:
    words = file.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)


# 11


import os

file_size = os.path.getsize("example.txt")
print(f"Fayl hajmi: {file_size} bayt")


# 12


my_list = ["salom", "dunyo", "python"]
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")




# 13


with open("example.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())



# 14

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readl1.strip() + " " + l2)




# 15


import random

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines))





# 17


with open("example.txt", "r") as file:
    cleaned = [line.strip() for line in file]
print(cleaned)


# 18


with open("example.txt", "r") as file:
    text = file.read().replace(",", " ")
    words = text.split()
    print("So‘zlar soni:", len(words))



# 19


files = ["file1.txt", "file2.txt"]
chars = []

for fname in files:
    with open(fname, "r") as f:
        chars.extend(list(f.read()))
print(chars)



# 20

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"Bu {letter}.txt fayli.\n")


# 21


import string

letters = string.ascii_lowercase
n = 5  # Har bir qatorda 5 ta harf

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")



