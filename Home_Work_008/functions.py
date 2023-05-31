def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('Home_Work_008\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())
    print()


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('Home_Work_008\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')
    print()


# def find_data() -> None:
#     """Печатает результат поиска по справочнику."""
#     with open('Home_Work_008\\book.txt', 'r', encoding='utf-8') as file:
#         data = file.read()
#     contact_to_find = input('Введите, что хотите найти: ')
#     result = search(data, contact_to_find)
#     for i in range(len(result)):
#         print(result[i])
#     print()


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def search2(book: str, info: str):
    """Находит в списке записи по определенному критерию поиска"""
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def rename(count: int):
    """Добавляет и редактирует информацию в справочник."""
    with open('Home_Work_008\\book.txt', 'r', encoding='utf-8') as book:
        lines = book.readlines()
        del lines[count]
        fio = input('Введите ФИО: ')
        phone_num = input('Введите номер телефона: ')
        new_data = str(f'{fio} | {phone_num}\n')
        lines.insert(count, new_data)
    with open("Home_Work_008\\book.txt", "w+", encoding='utf-8') as book:
        book.writelines(lines)
    print()


def del_data(count: int) -> None:
    """Удаляет информацию из справочника."""
    with open('Home_Work_008\\book.txt', 'r', encoding='utf-8') as book:
        lines = book.readlines()
        del lines[count]
    with open("Home_Work_008\\book.txt", "w", encoding='utf-8') as book:
        book.writelines(lines)
    print()


def index_data(book: str, result: str, count: int) -> list[str]:
    """Выводит информацию из справочника"""
    book = book.split('\n')
    result = ', '.join(result)
    print()
    for i in range(len(book)):
        if book[i] == result:
            count = i
    return count


def rename_data() -> None:
    """Находит данные в справочнике, \
        изменяет, либо удаляет необходимое\
        Печатает результат поиска по справочнику."""
    with open('Home_Work_008\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        result = data
        result_temp = None
        while result:
            print('Для выхода в главное меню: введите цифру 0')
            contact_to_find = input('Введите, что хотите найти: ')
            if contact_to_find == '0':
                break
            result = search(data, contact_to_find)
            for i in range(len(result)):
                print(result[i])
            result1 = result
            if len(result) > 1:
                result2 = result
                while result2:
                    if len(result2) > 1:
                        result_temp = result2
                        print()
                        print('Найдено = ', len(result2), 'контакт(а/ов)')
                        contact_to_find2 = input('Уточните либо измените запрос: ')
                        print('Для выхода в меню поиска: введите цифру 0')
                        if contact_to_find2 == '0':
                            break
                        result2 = search2(result2, contact_to_find2)
                        for i in range(len(result2)):
                            print(result2[i])
                    if len(result2) < 1:
                        print('Нет данных, попробуйте снова.')
                        print('Прошлые данные:')
                        result2 = result_temp
                        for i in range(len(result2)):
                            print(result2[i])
                    if len(result2) == 1:
                        result1 = result2
                        print()
                        break
            if len(result1) < 1:
                print('Нет данных, попробуйте снова.')
                print()
                result1 = data
            if len(result1) == 1:
                print('1. Редактировать, 2. Удалить, 0. Вернуться в меню поиска')
                action = int(input('Выберите действие: '))
                f = int(index_data(data, result1, None))
                if action == 1:
                    rename(f)
                if action == 2:
                    del_data(f)
                if action == 0:
                    break
            break
