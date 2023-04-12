# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

print ("Введите 3-х значное число: ")
user_numbers = int(input())
print ("Ваше число:", user_numbers)

sum_numbers = None

if 99 < user_numbers < 1000:
    sum_numbers = int(user_numbers/100 % 10) + int(user_numbers/10 % 10) + int(user_numbers % 10) 
    print ("Сумма цифр =", sum_numbers)
else:
    print ("Ваше число, вне диапазона!")    
