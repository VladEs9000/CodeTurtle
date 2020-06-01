import os
import security
import shutil


def pathcheck(str: str) -> str:
        flag = True
        while flag:
            way = input("Напишите имя файла.txt заметки(.txt):")
            try:
                try:
                    way_rule = way.split('.')
                    way_rule.reverse()
                    if way_rule[0] == str:
                        return way
                    raise Exception("Неправильно расширение")
                except Exception:
                    print("Неправильно введенный файл")
            except BaseException:
                print("Не тот ввод")


def create_note(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    os.chdir(login)
    for i in range(3):
        name = pathcheck('txt')
        if ' ' in name:
            print("Вы ввели некорректное название")
            i += 1
        elif len(name) < 1:
            print("Вы ввели некорректное название")
            i += 1
        elif len(name) > 100:
            print("Вы ввели некорректное название")
            i += 1
        elif name in files:
            print("Записка с таким именем уже существует")
        else:
            with open('secretinf.conf', 'rb') as config_file:
                master_key = config_file.read()
            with open('encodeinf.conf', 'rb') as encode_file:
                encode_key = encode_file.read()
            print("Пустая записка создана")
            encode_key = security.decrypt(encode_key, master_key)
            space = ''
            space = space.encode(encoding='utf-8')
            space = security.encrypt(space, encode_key)
            new_zap = open(name, 'wb')
            new_zap.write(space)
            new_zap.close()
            return True
        if i == 3:
            print("Проблемы с выбором имени?")
            exit(0)


def change_note(login: str) -> bool:
    os.chdir('..')
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    path = os.getcwd()
    with open('secretinf.conf', 'rb') as config_file:
        master_key = config_file.read()
    with open('encodeinf.conf', 'rb') as encode_file:
        encode_key = encode_file.read()
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    else:
        print("Ваш список заметок")
        print(files)
        while flag:
            nissan = input("Выберите заметку,которую хотите изменить:")
            if nissan == "maininf.conf":
                print("Это конфигурационный файл,а не заметка")
            if nissan in files:
                print("Вы выбрали ", nissan)
                encode_key = security.decrypt(encode_key, master_key)
                with open(nissan, 'rb') as changing_note:
                    text = changing_note.read()
                    text = security.decrypt(text, encode_key)
                    text = text.decode()
                with open(nissan, 'w') as decrypted_note:
                    decrypted_note.write(text)
                os.system(path + '//' + nissan)
                with open(nissan, 'r') as crypting_note:
                    c_text = crypting_note.read()
                with open(nissan, 'wb') as bytes_note:
                    c_text = security.encrypt(c_text.encode(), encode_key)
                    bytes_note.write(c_text)
                return True
            else:
                print("Такой заметки нет")


def read_note(login: str) -> bool:
    os.chdir('..')
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    print("Ваш список заметок")
    print(files)
    while flag:
        command = input("Выберите заметку которую хотите прочитать:")
        if command == "maininf.conf" or "secretinf.conf" or "encodeinf.conf":
            print("Это конфигурационный файл,а не заметка")
        if command in files:
            with open('secretinf.conf', 'rb') as config_file:
                master_key = config_file.read()
            with open('encodeinf.conf', 'rb') as encode_file:
                encode_key = encode_file.read()
            print("Вы выбрали ", command)
            with open(command, 'rb') as changing_note:
                encode_key = security.decrypt(encode_key, master_key)
                text = changing_note.read()
                text = security.decrypt(text, encode_key)
                text = text.decode()
                print(text)
            return True
        else:
            print("Такой заметки нет")


def delete_note(login: str) -> bool:
    os.chdir('..')
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    print("Ваш список заметок")
    print(files)
    while flag:
        command = input("Выберите заметку которую хотите удалить:")
        if command == "maininf.conf" or "secretinf.conf" or "encodeinf.conf":
            print("Это конфигурационный файл,а не заметка")
        if command in files:
            print("Вы выбрали ", command)
            os.remove(command)
            print("Заметка удалена")
            return True
        else:
            print("Такой заметки нет")


def delete_all_notes(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    for i in range(len(files)):
        command = files[i]
        os.remove(command)
    print("Все ваши заметки удалены")
    return True


def note_list(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Ваш список заметок пуст")
    else:
        print("Ваш список заметок")
        print(files)
    return True
