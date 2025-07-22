
# 4-lessons homework





my_dict = {'a': 3, 'b': 1, 'c': 2}

# O'sish tartibida
asc_sorted = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("O'sish:", asc_sorted)

# Kamayish tartibida
desc_sorted = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Kamayish:", desc_sorted)

# 5

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


# 6 toplam bilan ishlash 


my_set = set([1, 2, 3, 4])
print(my_set)

my_set = {1, 2, 3}
for item in my_set:
    print(item)

#  qo'shish

my_set = {1, 2}
my_set.add(3)  
my_set.update([4, 5])  
print(my_set)


# element olish

my_set = {1, 2, 3, 4}
my_set.remove(3) 
print(my_set)


