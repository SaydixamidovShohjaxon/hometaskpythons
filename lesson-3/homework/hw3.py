





  Homework lesson - 3

1

mevalar = ['olma', 'banan', 'anor', 'gilos', 'shaftoli']
print(mevalar[2])

 2

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

3

numbers = [10, 20, 30, 40, 50]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(new_list)


4

films = ['Titanic', 'Inception', 'Avengers', 'Matrix', 'Avatar']
film_set = set(films)
print(film_set)


5

cities = ['Toshkent', 'Parij', 'London', 'New York']
print("Parij" in cities)


6 

nums = [1, 2, 3]
repeated = nums * 2
print(repeated)


7

nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)


8

t = tuple(range(1, 11))
print(t[2:7])

9

colors = ['qizil', 'ko\'k', 'yashil', 'ko\'k', 'sariq', 'ko\'k']
print(colors.count('ko\'k'))

10

animals = ('it', 'mushuk', 'sher', 'quyon')
print(animals.index('sher'))


11

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)


12

my_list = [10, 20, 30]
my_tuple = (1, 2, 3, 4)
print("Ro'yxat uzunligi:", len(my_list))
print("Kortej uzunligi:", len(my_tuple))

13

t = (1, 2, 3, 4, 5)
lst = list(t)
print(lst)
# 14

numbers = (23, 5, 88, 19, 1)
print("Max:", max(numbers))
print("Min:", min(numbers))
# 15

words = ('olma', 'banan', 'gilos', 'shaftoli')
reversed_words = words[::-1]
print(reversed_words)
