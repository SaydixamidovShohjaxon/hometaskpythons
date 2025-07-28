
# hometask 6

# 1

# def modify_string(txt):
#     vowels = "aeiou"
#     result = ""
#     i = 0
#     while i < len(txt):
#         result += txt[i]
#         if (i + 1) % 3 == 0:
#             if txt[i] not in vowels and (i + 1 >= len(txt) or txt[i + 1] != '_'):
#                 result += "_"
#         i += 1
#     if result.endswith("_"):
#         result = result[:-1]
#     print(result)

# modify_string("hello")         # hel_lo
# modify_string("assalom")       # ass_alom
# modify_string("abcabcabcdeabcdefabcdefg")  # abc_abc_abcd_abcd_abcdef



# 2

# n = int(input("Son kiriting :"))
# for i in range(n):
#     print(i**2)


# 3

#3/1 

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# 3/2

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()





# 3/3


# n = int(input("Enter number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum is:", sum)


# 3/4


# n = int(input())
# for i in range(1, 11):
#     print(n * i)


# 3/5


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers:
#     if num > 500:
#         continue
#     if num > 150:
#         continue
#     if num % 5 == 0:
#         print(num)



# 3/6

# num = int(input())
# print("Output:", len(str(num)))


# 3/7

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()


# 3/8

# list1 = [10, 20, 30, 40, 50]
# for i in reversed(list1):
#     print(i)


# 3/9

# for i in range(-10, 0):
#     print(i)


    # 3/10

# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# 3/11

# for num in range(25, 51):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# 3/12

# n = 10
# a, b = 0, 1
# print("Fibonacci sequence:")
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# 3/13

# n = int(input("Enter number: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(f"{n}! = {fact}")
# # 4
# def uncommon_elements(list1, list2):
#     result = []
#     for i in list1:
#         if i not in list2:
#             result.append(i)
#     for i in list2:
#         if i not in list1:
#             result.append(i)
#     print(result)

# uncommon_elements([1, 1, 2], [2, 3, 4])          
# uncommon_elements([1, 2, 3], [4, 5, 6])       
# uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])  
