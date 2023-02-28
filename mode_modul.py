from os import path
file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])

        return all_data


def show_all():
    if not all_data:
        print("Файл базы создан, но он пуст!")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global last_id
    array = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись была успешно добавлена в телефонный справочник!\n")
    else:
        print("Данные уже существуют!")


def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    answer = input(f"Введите  {num}: ")
    while True:
        if num in "Фамилия Имя Отчество":
            if answer.isalpha():
                break

        if num == "Телефон":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Данные некорректны!\nФИО состоит только из букв, телефон из 11 цифр\n"
                       f"Введите {num}: ")
    return answer


def change_contact(data_tuple):
    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Данные уже существуют!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Изменения записаны!\n")


def del_contact():
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id удаляемой записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена, без проблем!\n")
    else:
        print("Попробуйте заново!")
