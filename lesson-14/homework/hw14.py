
# Homework 14

# 1


import json

with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for student in data["students"]:
    print(f"Ism: {student['name']}")
    print(f"Yosh: {student['age']}")
    print(f"Fakultet: {student['faculty']}")
    print("-" * 30)


# 2



import requests

API_KEY = "374ef5c4485c1c21c573b43009f0c91a"  # o'zingizning keyingizni yozing
city = "Tashkent"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if "main" in data:
    print(f"Shahar: {data['name']}")
    print(f"Harorat: {data['main']['temp']}°C")
    print(f"Namlik: {data['main']['humidity']}%")
    print(f"Ob-havo: {data['weather'][0]['description']}")
else:
    print("Xato:", data)


# 3

import json

filename = "books.json"

# JSONni  o'qish
def read_books():
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# JSONda yozish
def write_books(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Kitob qo‘shish
def add_book(title, author):
    data = read_books()
    data["books"].append({"title": title, "author": author})
    write_books(data)
    print(" Kitob qo‘shildi!")

# Kitobni yangilash
def update_book(old_title, new_title, new_author):
    data = read_books()
    for book in data["books"]:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
    write_books(data)
    print(" Kitob yangilandi!")

# Kitobni o‘chirish
def delete_book(title):
    data = read_books()
    data["books"] = [book for book in data["books"] if book["title"] != title]
    write_books(data)
    print(" Kitob o‘chirildi!")

# === Test qilish ===
add_book("Machine Learning", "Dilnoza")
update_book("Python Asoslari", "Python Advanced", "Shohjaxon Saydixamidov")
delete_book("SQL Darslari")



# 4


import requests
import random

API_KEY = "6535a437"
BASE_URL = f"http://www.omdbapi.com/?apikey={API_KEY}&t=Inception"

def get_movie_by_genre(genre):
    # OMDb da genre bo‘yicha to‘g‘ridan-to‘g‘ri izlash yo‘q
    # Shuning uchun mashhur kalit so‘zlardan foydalanamiz (masalan "love", "war", "action")
    search_terms = ["love", "war", "life", "man", "girl", "hero", "future", "day"]
    term = random.choice(search_terms)

    url = f"{BASE_URL}?apikey={API_KEY}&s={term}&type=movie"
    response = requests.get(url)
    data = response.json()

    if "Search" not in data:
        print("Film topilmadi:", data)
        return

    # Random film tanlash
    movies = [m for m in data["Search"] if genre.lower() in m.get("Type", "").lower() or genre.lower() in m.get("Title", "").lower()]
    
    if not movies:
        movies = data["Search"]  # fallback: hammasidan random
    
    movie = random.choice(movies)
    print(f" Tavsiya film: {movie['Title']} ({movie['Year']})")
    print("IMDB ID:", movie["imdbID"])

# Foydalanuvchi janr kiritadi
genre = input("Qaysi janrdagi film kerak? (masalan: action, comedy, drama): ")
get_movie_by_genre(genre)



