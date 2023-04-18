#  Требуется вычислить,
# сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

count_numbers = int(input("Введите количество чисел: "))
massive = []

for _ in range(count_numbers):
    number = randint(0, 10)
    massive.append(number)
print (massive)

exclusive_number = int(input("Введите число, для поиска количества повторений: "))
count_exclusive = 0
index = 0
for _ in massive:
    if massive[index] == exclusive_number:
        count_exclusive += 1
    index += 1

if count_exclusive == 0:
    print ("Ваше число отсутсвует в массиве")
else:
    print (f'Ваше число {exclusive_number}, повторяется {count_exclusive} раз.')
