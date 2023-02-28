from mode_modul import exist_contact


def search_contact():
    search_data = exist_contact(0, input("Введите данные поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("С такими данным записей нет!")