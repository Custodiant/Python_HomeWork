# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))


storage_one = set()
for _ in range(n):
    storage_one.add(input("Число из первого множества: "))
print(storage_one)

storage_two = set()
for _ in range(m):
    storage_two.add(input("Число из второго множества: "))
print(storage_two)

storage_tree = storage_one.intersection(storage_two)
print('Числа встречаемые в обоих множествах', sorted(storage_tree))
