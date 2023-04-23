# Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B
# с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def stepen(i, j):
    if (j == 1):
        return i
    if (j != 1):
        return (i * stepen(i, j - 1))


num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
print('Результат => ', stepen(num_a, num_b))
