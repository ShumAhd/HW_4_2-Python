# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

num = int(input("in: "))
i = 2 
lst = []

while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
    else:
        i += 1
print(f"out: {lst}")
