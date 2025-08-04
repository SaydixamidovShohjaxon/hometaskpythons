
# 9 homework


# 1


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Doira yuzasi:", c.area())         
print("Doira perimetri:", c.perimeter())





# 2





from datetime import date

class Person:
    def __init__(self, name, country, birth_date): 
        self.name = name
        self.country = country
        self.birth_date = date.fromisoformat(birth_date)

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))



p = Person("Shohjaxon", "Uzbekistan", "2006-01-13")
print("Ismi:", p.name)
print("Yoshi:", p.age())  






# 3







class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "ZeroDivisionError"

c = Calculator()
print("3 + 7 =", c.add(3, 7))           
print("10 - 4 =", c.subtract(10, 4))    
print("6 * 5 =", c.multiply(6, 5))      
print("8 / 2 =", c.divide(8, 2))        





# 4






# import math


# Rule  :

 #  pass hozircha hech nima qilmayman, keyin yozaman











class Shape:
    def area(self): pass
    def perimeter(self): pass 

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

class Triangle(Shape):
    def __init__(self, a, b, c, h):
        self.a, self.b, self.c, self.h = a, b, c, h

    def area(self):
        return 0.5 * self.b * self.h

    def perimeter(self):
        return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side




circle = Circle(3)
print("Doira yuzi:", circle.area())        
print("Doira perimetri:", circle.perimeter())  

triangle = Triangle(3, 4, 5, 2.5)
print("Uchburchak yuzi:", triangle.area())     
print("Uchburchak perimetri:", triangle.perimeter())  

square = Square(4)
print("Kvadrat yuzi:", square.area())      
print("Kvadrat perimetri:", square.perimeter()) 





# 5

#?


# 6


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else None
    def display(self):
        print("Stack:", self.stack)


s= Stack()
s.push(10)
s.push(20)
s.display()
print(s.pop())
s.display()



# 7


# 8

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total(self):
        return sum(self.items.values())


cart = ShoppingCart()
cart.add_item("shapka", 50000)
cart.add_item("kofta", 120000)
cart.add_item("shapka", 50000)  
cart.remove_item("kofta")
print("Jami narx:", cart.total())  



# 9

# Rule :

# Display ?




class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def display(self):
        print("Stack:", self.stack)

s = Stack()
s.push(5)
s.push(15)
s.display()          
print(s.pop())       
s.display()          





# 10


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def display(self):
        print("Queue:", self.queue)



q = Queue()
q.enqueue("A")
q.enqueue("B")
q.display()           
print(q.dequeue())   
q.display()         




# 11



class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so‘m qo‘shildi.")
        else:
            print("Noto‘g‘ri miqdor.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so‘m yechildi.")
        else:
            print("Yetarli mablag' yo‘q.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name):
        if name not in self.accounts:
            self.accounts[name] = Account(name)
            print(f"{name} uchun hisob ochildi.")
        else:
            print(f"{name} allaqachon hisobga ega.")

    def get_account(self, name):
        return self.accounts.get(name, None)

    def show_all_accounts(self):
        print("Barcha hisoblar:")
        for name, acc in self.accounts.items():
            print(f"- {name}: {acc.get_balance()} so‘m")





bank = Bank()

bank.add_account("shox")
bank.add_account("said")

shox = bank.get_account("shox")
said = bank.get_account("said")

shox.deposit(300000)
said.deposit(200000)

shox.withdraw(50000)
said.withdraw(250000)  

print("Ali balans:", shox.get_balance())
print("Vali balans:", said.get_balance())

bank.show_all_accounts()


