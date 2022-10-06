# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


import random
in_num = int(input("in: "))
if in_num <= 0:
    print("Negative value of the number of numbers!")
rand_list = []
for i in range(in_num):
    rand_list.append(random.randint(0, in_num))   
print("out", rand_list)

new_lst = []
for i in rand_list:
    if i not in new_lst:
        new_lst.append(i)
print("non-repeating", new_lst)



