# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> 2 3

sum_numbers = int(input("Введите сумму, 2 загаданных, чисел: "))
multiplication_numbers = int(input("Введите произведение, 2 загаданных, чисел: "))

first_numbers = 1
second_numbers = 1


for i in range (10000000):
    if (first_numbers < sum_numbers):
        if (first_numbers + second_numbers) == sum_numbers:
            if (first_numbers * second_numbers) == multiplication_numbers:
                print ("Первое число:", first_numbers, "Второе число:", second_numbers)
                break
            else:
                second_numbers += 1
                # print ("2 проход ", first_numbers, second_numbers)
            first_numbers = 1
        else:
            first_numbers +=1
            # print ("1 ", first_numbers, second_numbers)
