# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

user_text = str(input("Введите свое слово: "))
user_text = user_text.upper()

one_eng = dict.fromkeys(['A', 'E','I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
two_eng = dict.fromkeys(['D', 'G'], 2)
three_eng = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
four_eng = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
five_eng = dict.fromkeys(['K'], 5)
eight_eng = dict.fromkeys(['J', 'X'], 8)
ten_eng = dict.fromkeys(['Q', 'Z'], 10)
english_alphabet = ({**one_eng,
                     **two_eng,
                     **three_eng,
                     **four_eng,
                     **five_eng,
                     **eight_eng,
                     **ten_eng})

one_rus = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
two_rus = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
three_rus = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
four_rus = dict.fromkeys(['Й', 'Ы'], 4)
five_rus = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
eight_rus = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
ten_rus = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
russian_alphabet = ({**one_rus,
                     **two_rus,
                     **three_rus,
                     **four_rus,
                     **five_rus,
                     **eight_rus,
                     **ten_rus})

eng_rus_alphabet = ({**english_alphabet,
                     **russian_alphabet})

count = 0
for i in user_text:
    count += eng_rus_alphabet[i]
    # for key, value in eng_rus_alphabet.items():
    #     if key == i:
    #         count += value
print ("Cтоимость введенного слова =>", count, "очков")
