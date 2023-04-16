# №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]

# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.
from random import randint

lst = [randint(-9, 9) for i in range(10)]
print(lst)

#while
count = 0
i = 1
while i < len(lst):
    if lst[i - 1] < lst[i]:
        count += 1
    i += 1
print(count)

# for
count = 0
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        count += 1
print(count)