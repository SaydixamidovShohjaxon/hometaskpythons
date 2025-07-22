homework 2-lesson 


puzzle_1

age = int (input(" Tugilgan yilingizni kiriting :"))
year = int (input(" Hozirgi yilni kiriting :"))

ageAtTheMoment = year - age 

print (" Hozirgi yoshingiz :",ageAtTheMoment)


4


txt = "I'am John. I am from London"

words = txt.split()
if 'from' in words:
    index = words.index('from')
    location = words[index + 1]
    print(location)


# 5
txt = input("Matn kiriting: ")
reversed_txt = txt[::-1]
print("Teskari:", reversed_txt)


6

txt = input("Matn kiriting: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in txt if char in vowels)
print("Unlilar soni:", count)


7

numbers = list(map(int, input("Sonlarni kiriting (bo'shliq bilan): ").split()))
max_value = max(numbers)
print("Eng katta son:", max_value)


8

word = input("So'zni kiriting: ")
if word == word[::-1]:
    print("Palindrom")
else:
    print("Palindrom emas")

9

email = input("Email kiriting: ")
domain = email.split('@')[-1]
print("Domen:", domain)

10

import random
import string

length = 10  
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Tasodifiy parol:", password)

