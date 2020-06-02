import os
import security
import shutil
import stat


def pathcheck(str: str) -> str:
        for i in range(3):
            list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
            way = input("Напишите имя файла.txt заметки(.txt):")
            try:
                try:
                    for ch in way:
                        if list_error.count(ch) != 0:
                            print("Неправильные символы в файле")
                            return way, False
                    way_rule = way.split('.')
                    way_rule.reverse()
                    if way_rule[0] == str:
                        return way, True
                    raise Exception("Неправильно расширение")
                except Exception:
                    print("Неправильно введенный файл")
                    i += 1
            except BaseException:
                print("Не тот ввод")
                i += 1
        if i == 3:
            return way, False


def create_note(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    os.chdir(login)
    for i in range(3):
        name, check = pathcheck('txt')
        if check is False:
            return False
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
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    kappa.append("secretinf.conf")
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
            for ch in nissan:
                if list_error.count(ch) != 0:
                    print("Неправильные символы в файле")
            if nissan in kappa:
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
                os.chmod(path, stat.S_IXOTH)
                path_kek = os.path.join(path, nissan)
                os.system(path_kek)
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
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    kappa.append("secretinf.conf")
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    print("Ваш список заметок")
    print(files)
    while flag:
        command = input("Выберите заметку которую хотите прочитать:")
        for ch in command:
            if list_error.count(ch) != 0:
                print("Неправильные символы в файле")
        if command in kappa:
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
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    files.remove("secretinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    kappa.append("secretinf.conf")
    if len(files) == 0:
        print("Список заметок пуст")
        return True
    print("Ваш список заметок")
    print(files)
    while flag:
        command = input("Выберите заметку которую хотите удалить:")
        for ch in command:
            if list_error.count(ch) != 0:
                print("Неправильные символы в файле")
        if command in kappa:
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
