# Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

count_numbers = int(input("Введите количество чисел в массиве: "))
massive = []

for _ in range(count_numbers):
    number = randint(0, 100)
    massive.append(number)
print (massive)

exclusive_number = int(input("Выберете число (от 0 до 100) для поиска, близкого по величине элемента массива: "))
exclusive_number_temp = 0
index = 0
min = 0
max = 100
min_count = 0   # для исключения ошибки данных, при рассчете крайних положений
max_count = 0   # для исключения ошибки данных, при рассчете крайних положений
for _ in massive:
    if massive[index] > exclusive_number:
        if massive[index] < max:
            max = massive[index]
            max_count += 1
    elif massive[index] < exclusive_number:
        if massive[index] > min:
            min = massive[index]
            min_count += 1
    else:
        exclusive_number_temp = massive[index]
        break
    index += 1

if exclusive_number != exclusive_number_temp:
    if (exclusive_number - min) < (max - exclusive_number):
        if min_count == 0:  # для исключения ошибки данных, при рассчете крайних положений
            print(f'Ближайшее по значению число к вашему {max}')
        else:
            print(f'Ближайшее по значению число к вашему {min}')
    elif (exclusive_number - min) > (max - exclusive_number):
        if max_count == 0:  # для исключения ошибки данных, при рассчете крайних положений
            print(f'Ближайшее по значению число к вашему {min}')
        else:
            print(f'Ближайшее по значению число к вашему {max}')
else:
    print (f"Ваше число {exclusive_number}, присутствует в массиве")

