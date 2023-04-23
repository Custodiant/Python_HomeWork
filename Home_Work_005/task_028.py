# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций
# допускаются только +1 и -1.
# Также нельзя использовать циклы.

# return sum(a, b) + 1 - такое использовать нельзя

# *Пример:*

# 2 2
#     4

# def sum_nums(i, j):
#     if j == 0:
#         return i
#     else:
#         if j > 0:
#             return sum_nums(i+1, j-1)
#         else:
#             return sum_nums(i-1, j+1)
def sum_nums(i, j):
    return i if j == 0 else sum_nums(i+1, j-1) if j > 0 else sum_nums(i-1, j+1)


num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))

print("Сумма чисел => ", sum_nums(num_a, num_b))
