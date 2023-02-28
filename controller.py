from mode_search import search_contact
from mode_modul import *


def main_menu():
    play = True
    while play:
        read_records()
        answer = input(
            "          Выберите действие для начала работы:\n"
            "          1. Показать все записи телефонного справочника\n"
            "          2. Создать новую запись\n"
            "          3. Поиск записи\n"
            "          4. Изменить данные\n"
            "          5. Удалить данные\n"
            "          6. Выход\n"
            "     Введите пожалуйста команду и нажмите enter \n->: ")
        print()

        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                play = False
            case _:
                print("Попробуйте снова!\n")
                print()


def edit_menu():
    add_dict = {"1": "Фамилия", "2": "Имя",
                "3": "Отчество", "4": "Телефон"}

    show_all()
    record_id = input("Введите запись по  id: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nЧто необходимо изменить ?:")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Телефон\n"
                           "5. Выход\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Данные не распознаны, повторите ввод.")
    else:
        print("Данные введены некорректно!")