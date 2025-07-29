

# 10

# 1

class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        holat = "Bajarilgan" if self.completed else "Bajarilmagan"
        return f"{self.name} | {self.description} | Tugash sanasi: {self.deadline} | {holat}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_all_tasks(self):
        if not self.tasks:
            print("Vazifalar ro'yxati bo'sh.")
        for task in self.tasks:
            print(task)

    def show_incomplete_tasks(self):
        topildi = False
        for task in self.tasks:
            if not task.completed:
                print(task)
                topildi = True
        if not topildi:
            print("Bajarilmagan vazifalar yo'q.")

    def mark_task_done(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_done()
                print(f'"{name}" bajarildi deb belgilandi.')
                return
        print("Bunday vazifa topilmadi.")


def todo_app():
    todo = ToDoList()

    while True:
        print("\n1. Vazifa qo‘shish")
        print("2. Vazifani bajarildi deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Faqat bajarilmagan vazifalarni ko‘rish")
        print("5. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == '1':
            nom = input("Vazifa nomi: ")
            tavsif = input("Tavsif: ")
            sana = input("Tugash sanasi: ")
            yangi = Task(nom, tavsif, sana)
            todo.add_task(yangi)

        elif tanlov == '2':
            nom = input("Qaysi vazifa bajarildi?: ")
            todo.mark_task_done(nom)

        elif tanlov == '3':
            todo.show_all_tasks()

        elif tanlov == '4':
            todo.show_incomplete_tasks()

        elif tanlov == '5':
            print("Chiqildi.")
            break

        else:
            print("Noto'g'ri tanlov.")
    
todo_app()
    


    # 2


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} ({self.author})\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def show_all(self):
        if not self.posts:
            print("Postlar mavjud emas.")
        for post in self.posts:
            print(post)
            print()

    def show_by_author(self, author):
        bor = False
        for post in self.posts:
            if post.author == author:
                print(post)
                print()
                bor = True
        if not bor:
            print("Bu muallifda post yo\'q.")

    def delete_post(self, title):
        for i in range(len(self.posts)):
            if self.posts[i].title == title:
                del self.posts[i]
                print("Post o\'chirildi.")
                return
        print("Post topilmadi.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print("Post yangilandi.")
                return
        print("Post topilmadi.")

    def recent_posts(self, n=3):
        print("So\'nggi postlar:")
        for post in self.posts[-n:]:
            print(post)
            print()


def blog_app():
    blog = Blog()

    while True:
        print("\n1. Post qo\'shish")
        print("2. Barcha postlarni ko\'rish")
        print("3. Muallif bo\'yicha postlarni ko\'rish")
        print("4. Postni o\'chirish")
        print("5. Postni tahrirlash")
        print("6. So\'nggi postlar")
        print("7. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == '1':
            sarlavha = input("Sarlavha: ")
            kontent = input("Kontent: ")
            muallif = input("Muallif: ")
            blog.add_post(Post(sarlavha, kontent, muallif))

        elif tanlov == '2':
            blog.show_all()

        elif tanlov == '3':
            ism = input("Muallif ismi: ")
            blog.show_by_author(ism)

        elif tanlov == '4':
            nom = input("O\'chirish uchun post sarlavhasi: ")
            blog.delete_post(nom)

        elif tanlov == '5':
            nom = input("Tahrirlash uchun post sarlavhasi: ")
            yangisi = input("Yangi kontent: ")
            blog.edit_post(nom, yangisi)

        elif tanlov == '6':
            blog.recent_posts()

        elif tanlov == '7':
            print("Chiqildi.")
            break

        else:
            print("Noto\'g\'ri tanlov.")


blog_app()





# 3

class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def info(self):
        print(f"Hisob raqami: {self.number}")
        print(f"Egasi: {self.owner}")
        print(f"Balans: {self.balance} so'm\n")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def transfer(self, from_acc, to_acc, amount):
        a = self.get_account(from_acc)
        b = self.get_account(to_acc)
        if a and b and a.withdraw(amount):
            b.deposit(amount)
            return True
        return False

    def show_all(self):
        for acc in self.accounts:
            acc.info()


bank = Bank()


    
while True:
    print("\n1. Hisob ochish")
    print("2. Balansni ko‘rish")
    print("3. Pul qo‘shish")
    print("4. Pul yechish")
    print("5. Pul o‘tkazish")
    print("6. Barcha hisoblar")
    print("0. Chiqish")
    n = input("Tanlov: ")

    if n == "1":
        num = input("Hisob raqami: ")
        name = input("Ismi: ")
        acc = Account(num, name)
        bank.add_account(acc)

    elif n == "2":
        num = input("Hisob raqami: ")
        acc = bank.get_account(num)
        if acc:
            print(f"Balans: {acc.balance} so'm")
        else:
            print("Topilmadi.")

    elif n == "3":
        num = input("Hisob raqami: ")
        amt = int(input("Miqdor: "))
        acc = bank.get_account(num)
        if acc:
            acc.deposit(amt)

    elif n == "4":
        num = input("Hisob raqami: ")
        amt = int(input("Miqdor: "))
        acc = bank.get_account(num)
        if acc:
            if acc.withdraw(amt):
                print("Pul yechildi.")
            else:
                print("Yetarli mablag‘ yo‘q.")

    elif n == "5":
        f = input("Qayerdan: ")
        t = input("Qayerga: ")
        amt = int(input("Miqdor: "))
        if bank.transfer(f, t, amt):
            print("Pul o‘tkazildi.")
        else:
            print("Xatolik.")

    elif n == "6":
        bank.show_all()

    elif n == "0":
        break

    else:
        print("Noto‘g‘ri tanlov.")



bank()


