import security
import os
import shutil
from typing import Tuple


def create_new_acc() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for i in range(3):
        try:
            new_login = input("Придумайте логин аккаунта(без пробелов):")
            if ' ' in new_login:
                i += 1
            elif len(new_login) < 1:
                i += 1
            elif len(new_login) > 100:
                i += 1
            elif new_login in files:
                i += 1
            else:
                break
            if i == 3:
                os.chdir('..')
                return False
        except BaseException:
            print("Проблемы с логином")
    for i in range(3):
        try:
            new_password = input("Придумайте пароль аккаунта(без пробелов):")
            if ' ' in new_password:
                i += 1
            elif len(new_login) < 1:
                i += 1
            elif len(new_login) > 30:
                i += 1
            else:
                choise = True
                break
            if i == 3:
                os.chdir('..')
                return False
        except BaseException:
            print("Проблемы с паролем")
    if choise is True:
        os.chdir('notes')
        os.mkdir(new_login)
        os.chdir(new_login)
        master_key = security.master_key(new_password)
        encode_key = security.encrypt(security.secret_key(), master_key)
        mainfile = open("maininf.conf", 'w')
        mainfile.write(new_login + ' ' + security.hash_password(new_password))
        mainfile.close()
        encodefile = open("encodeinf.conf", 'wb')
        encodefile.write(encode_key)
        encodefile.close()
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        return True
    return False


def auth_acc() -> Tuple[str, bool, str]:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for i in range(3):
        try:
            auth_acc = input("Введите ваш логин от аккаунта:")
            if auth_acc in files:
                os.chdir('notes')
                os.chdir(auth_acc)
                with open("maininf.conf", 'r', encoding='utf-8') as auth_file:
                    method = auth_file.readline().rstrip().split(' ')
                for i in range(3):
                    try:
                        auth_p = input("Введите пароль для аккаунта:")
                        if security.check_password(method[1], auth_p) is True:
                            return auth_acc, True, auth_p
                        else:
                            i += 1
                        if i == 3:
                            os.chdir('..')
                            return auth_acc, False, auth_p
                    except BaseException:
                        print("Проблемы с паролем")
            else:
                i += 1
            if i == 3:
                return auth_acc, False, auth_p
        except FileNotFoundError:
            print("Не найдено такого аккаунта")
    return auth_acc, False, auth_p


def delete_acc() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for j in range(3):
        try:
            delete_login = input("Введите логин аккаунта который удаляете:")
            if delete_login in files:
                break
            else:
                j += 1
            if j == 3:
                os.chdir('..')
                return False
        except FileNotFoundError:
            print("Не найдено такого аккаунта")
    os.chdir('notes')
    os.chdir(delete_login)
    with open("maininf.conf", 'r', encoding='utf-8') as delete_file:
        method = delete_file.readline().rstrip().split(' ')
        for i in range(3):
            try:
                delete_pass = input("Введите пароль для данного аккаунта:")
                if security.check_password(method[1], delete_pass) is True:
                    check = True
                    break
                else:
                    i += 1
                if i == 3:
                    os.chdir('..')
                    os.chdir('..')
                    os.chdir('..')
                    return False
            except BaseException:
                print("Проблемы с паролем")
    if check is True:
        os.chdir('..')
        shutil.rmtree(delete_login)
        os.chdir('..')
        os.chdir('..')
        return True
    return False


def change_password() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for j in range(3):
        try:
            change_login = input("Введите логин аккаунта который изменяете:")
            if change_login in files:
                break
            else:
                j += 1
            if j == 3:
                os.chdir('..')
                return False
        except FileNotFoundError:
            print("Не найдено такого аккаунта")
    os.chdir('notes')
    os.chdir(change_login)
    with open("maininf.conf", 'r', encoding='utf-8') as change_file:
        method = change_file.readline().rstrip().split(' ')
        for i in range(3):
            try:
                change_pass = input("Введите пароль для данного аккаунта:")
                if security.check_password(method[1], change_pass) is True:
                    check = True
                    break
                else:
                    i += 1
                if i == 3:
                    os.chdir('..')
                    os.chdir('..')
                    os.chdir('..')
                    return False
            except BaseException:
                print("Проблемы с паролем")
    if check is True:
        for i in range(3):
            try:
                new_pass = input("Введите ваш новый пароль(без пробелов):")
                if ' ' in new_pass:
                    i += 1
                elif len(new_pass) < 1:
                    i += 1
                elif len(new_pass) > 30:
                    i += 1
                else:
                    choise = True
                    break
                if i == 3:
                    os.chdir('..')
                    os.chdir('..')
                    os.chdir('..')
                    return False
            except BaseException:
                print("Проблемы с паролем")
        if choise is True:
            with open('encodeinf.conf', 'rb') as encode_file:
                encode_key = encode_file.read()
            master_key = security.master_key(change_pass)
            new_master_key = security.master_key(new_pass)
            new_encode_key = security.decrypt(encode_key, master_key)
            new_encode_key = security.encrypt(new_encode_key, new_master_key)
            mainf = open("maininf.conf", 'w')
            mainf.write(change_login + ' ' + security.hash_password(new_pass))
            mainf.close()
            encodefile = open("encodeinf.conf", 'wb')
            encodefile.write(new_encode_key)
            encodefile.close()
            os.chdir('..')
            os.chdir('..')
            os.chdir('..')
            return True
    return False

