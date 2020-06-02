import os
import security
import shutil
import stat
from typing import Tuple


def pathcheck(str: str) -> Tuple[str, bool]:
        for i in range(3):
            list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
            way = input("Напишите имя файла.txt заметки(.txt):")
            try:
                try:
                    for ch in way:
                        if list_error.count(ch) != 0:
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
        return way, False


def create_note(login: str, password: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    os.chdir(login)
    for i in range(3):
        try:
            try:
                name, check = pathcheck('txt')
                if check is False:
                    return False
                if ' ' in name:
                    i += 1
                elif len(name) < 1:
                    i += 1
                elif len(name) > 100:
                    i += 1
                if name in files:
                    i += 1
                else:
                    with open('encodeinf.conf', 'rb') as encode_file:
                        encode_key = encode_file.read()
                    master_key = security.master_key(password)
                    encode_key = security.decrypt(encode_key, master_key)
                    karapa = ''
                    space = karapa.encode(encoding='utf-8')
                    space = security.encrypt(space, encode_key)
                    new_zap = open(name, 'wb')
                    new_zap.write(space)
                    new_zap.close()
                    return True
                if i == 3:
                    return False
            except FileExistsError:
                print("Такая заметка уже существует")
        except BaseException:
            print("Проблемы с заметкой")
    return False


def change_note(login: str, password: str) -> bool:
    os.chdir('..')
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    path = os.getcwd()
    with open('encodeinf.conf', 'rb') as encode_file:
        encode_key = encode_file.read()
    if len(files) == 0:
        print("Список заметок пуст")
        return False
    else:
        print("Ваш список заметок")
        print(files)
        while flag:
            try:
                nissan = input("Выберите заметку,которую хотите изменить:")
                for ch in nissan:
                    if list_error.count(ch) != 0:
                        print("Неправильные символы в файле")
                if nissan in kappa:
                    print("Это конфигурационный файл,а не заметка")
                if nissan in files:
                    master_key = security.master_key(password)
                    encode_key = security.decrypt(encode_key, master_key)
                    with open(nissan, 'rb') as changing_note:
                        text = changing_note.read()
                        text = security.decrypt(text, encode_key)
                        text_dec = text.decode()
                    with open(nissan, 'w') as decrypted_note:
                        decrypted_note.write(text_dec)
                    os.chmod(path, stat.S_IXOTH)
                    path_kek = os.path.join(path, nissan)
                    os.system(path_kek)
                    with open(nissan, 'r') as crypting_note:
                        c_text = crypting_note.read()
                    with open(nissan, 'wb') as bytes_note:
                        cr_text = security.encrypt(c_text.encode(), encode_key)
                        bytes_note.write(cr_text)
                    return True
            except FileNotFoundError:
                print("Такой заметки нет")
    return False


def read_note(login: str, password: str) -> bool:
    os.chdir('..')
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    if len(files) == 0:
        print("Список заметок пуст")
        return False
    print("Ваш список заметок")
    print(files)
    while flag:
        try:
            command = input("Выберите заметку которую хотите прочитать:")
            for ch in command:
                if list_error.count(ch) != 0:
                    print("Неправильные символы в файле")
            if command in kappa:
                print("Это конфигурационный файл,а не заметка")
            if command in files:
                with open('encodeinf.conf', 'rb') as encode_file:
                    encode_key = encode_file.read()
                master_key = security.master_key(password)
                with open(command, 'rb') as changing_note:
                    encode_key = security.decrypt(encode_key, master_key)
                    text = changing_note.read()
                    text = security.decrypt(text, encode_key)
                    text_d = text.decode()
                    print(text_d)
                return True
        except FileNotFoundError:
            print("Такой заметки нет")
    return False


def delete_note(login: str) -> bool:
    os.chdir('..')
    list_error = ["\\", "/", ":", "*", "?", "\"", "|", "<", ">"]
    flag = True
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    os.chdir(login)
    kappa = []
    kappa.append("maininf.conf")
    kappa.append("encodeinf.conf")
    if len(files) == 0:
        print("Список заметок пуст")
        return False
    print("Ваш список заметок")
    print(files)
    while flag:
        try:
            command = input("Выберите заметку которую хотите удалить:")
            for ch in command:
                if list_error.count(ch) != 0:
                    print("Неправильные символы в файле")
            if command in kappa:
                print("Это конфигурационный файл,а не заметка")
            if command in files:
                os.remove(command)
                return True
        except FileNotFoundError:
            print("Такой заметки нет")
    return False


def delete_all_notes(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Список заметок пуст")
        return False
    for i in range(len(files)):
        command = files[i]
        os.remove(command)
    return True


def note_list(login: str) -> bool:
    os.chdir('..')
    files = os.listdir(login)
    files.remove("maininf.conf")
    files.remove("encodeinf.conf")
    os.chdir(login)
    if len(files) == 0:
        print("Ваш список заметок пуст")
    else:
        print("Ваш список заметок")
        print(files)
    return True
