# №17. Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# Примечание: Пользователь может вводить значения списка или список задан изначально. 

# Input: [1, 1, 2, 0, -1, 3, 4, 4] 

# Output: 6 

import random 
n = int(input('введите число:  ')) 
List = [] 
for i in range(n): 
        List.append((random.randint(-5,5)))
        print(*List) 
        counter = set(List) 
        n = len(counter)
        print(n)