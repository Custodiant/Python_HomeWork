# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

user_numbers = int(input("Введите число: "))
degree = int(1)
degree_str = str(1)
for i in range(user_numbers):
    if (degree <= user_numbers):
        degree *= 2
        if (degree < user_numbers):
            degree_str += ", "
            degree_str += str(degree)
        else:
            degree_str += "."
            break
print(degree_str)