import security
import os
import shutil


def create_new_acc() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for i in range(3):
        new_login = input("Придумайте логин нового аккаунта(без пробелов):")
        if ' ' in new_login:
            print("Вы ввели некорректный логин")
            i += 1
        elif len(new_login) < 1:
            print("Вы ввели некорректный логин")
            i += 1
        elif len(new_login) > 100:
            print("Вы ввели некорректный логин")
            i += 1
        elif new_login in files:
            print("Аккаунт с таким именем уже существует")
            i += 1
        else:
            print("Логин верен")
            break
        if i == 3:
            print("Проблемы с выбором логина?")
            os.chdir('..')
            return False
    for i in range(3):
        new_password = input("Придумайте пароль аккаунта(без пробелов):")
        if ' ' in new_password:
            print("Вы ввели некорректный пароль")
            i += 1
        elif len(new_login) < 1:
            print("Вы ввели некорректный пароль")
            i += 1
        elif len(new_login) > 30:
            print("Вы ввели некорректный пароль")
            i += 1
        else:
            print("Пароль верен")
            choise = True
            break
        if i == 3:
            print("Вы ничему не учитесь...")
            os.chdir('..')
            return False
    if choise is True:
        os.chdir('notes')
        os.mkdir(new_login)
        os.chdir(new_login)
        master_key = security.master_key(new_password)
        encode_key = security.encrypt(security.secret_key(), master_key)
        mainfile = open("maininf.conf", 'w')
        mainfile.write(new_login + ' ' + security.hash_password(new_password))
        mainfile.close()
        secretfile = open("secretinf.conf", 'wb')
        secretfile.write(master_key)
        secretfile.close()
        encodefile = open("encodeinf.conf", 'wb')
        encodefile.write(encode_key)
        encodefile.close()
        print("Ваш новый аккаунт создан")
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        return True


def auth_acc() -> str:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for i in range(3):
        auth_acc = input("Введите ваш логин от аккаунта:")
        if auth_acc in files:
            print("Есть такой пользователь...")
            os.chdir('notes')
            os.chdir(auth_acc)
            with open("maininf.conf", 'r', encoding='utf-8') as auth_file:
                method = auth_file.readline().rstrip().split(' ')
                for i in range(3):
                    auth_pass = input("Введите пароль для данного аккаунта:")
                    if security.check_password(method[1], auth_pass) is True:
                        print("Пароли совпадают")
                        print("Вы аутентифицированы")
                        return auth_acc, True
                    else:
                        print("Пароль неверен,попробуйте снова")
                        i += 1
                    if i == 3:
                        print("Большой Брат усомнился в правах на аккаунт")
                        os.chdir('..')
                        return auth_acc, False
        else:
            print("Такого пользователя нет,попробуйте снова")
            i += 1
        if i == 3:
            print("Вы вводите не тех пользователей")
            return auth_acc, False


def delete_acc() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for j in range(3):
        delete_login = input("Введите логин аккаунта который хотите удалить:")
        if delete_login in files:
            break
        else:
            print("Введенного логина не существует,должно быть вы ошиблись")
            j += 1
        if j == 3:
            print("Должно быть вы забыли свой логин")
            os.chdir('..')
            return False
    os.chdir('notes')
    print("Для удаления аккаунта вы должны подтвердить что он принадлежит вам")
    os.chdir(delete_login)
    with open("maininf.conf", 'r', encoding='utf-8') as delete_file:
        method = delete_file.readline().rstrip().split(' ')
        for i in range(3):
            delete_pass = input("Введите пароль для данного аккаунта:")
            if security.check_password(method[1], delete_pass) is True:
                print("Пароли совпадают")
                check = True
                break
            else:
                print("Пароль неверен,попробуйте снова")
                i += 1
            if i == 3:
                print("Большой Брат усомнился в правах на аккаунт")
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
                return False
    if check is True:
        os.chdir('..')
        shutil.rmtree(delete_login)
        os.chdir('..')
        os.chdir('..')
        return True


def change_password() -> bool:
    os.chdir('TheFourth')
    files = os.listdir('notes')
    for j in range(3):
        change_login = input("Введите логин аккаунта который хотите изменить:")
        if change_login in files:
            break
        else:
            print("Введенного логина не существует,должно быть вы ошиблись")
            j += 1
        if j == 3:
            print("Должно быть вы забыли свой логин")
            os.chdir('..')
            return False
    os.chdir('notes')
    print("Для изменения пароля аккаунта,докажите, что он принадлежит вам")
    os.chdir(change_login)
    with open("maininf.conf", 'r', encoding='utf-8') as change_file:
        method = change_file.readline().rstrip().split(' ')
        for i in range(3):
            change_pass = input("Введите пароль для данного аккаунта:")
            if security.check_password(method[1], change_pass) is True:
                print("Пароли совпадают")
                check = True
                break
            else:
                print("Пароль неверен,попробуйте снова")
                i += 1
            if i == 3:
                print("Большой Брат усомнился в правах на данный аккаунт")
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
                return False
    if check is True:
        for i in range(3):
            new_pass = input("Введите ваш новый пароль(без пробелов):")
            if ' ' in new_pass:
                print("Вы ввели некорректный пароль")
                i += 1
            elif len(new_pass) < 1:
                print("Вы ввели некорректный пароль")
                i += 1
            elif len(new_pass) > 30:
                print("Вы ввели некорректный пароль")
                i += 1
            else:
                print("Пароль верен")
                choise = True
                break
            if i == 3:
                print("Вы ничему не учитесь...")
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
                return False
        if choise is True:
            with open('secretinf.conf', 'rb') as config_file:
                master_key = config_file.read()
            with open('encodeinf.conf', 'rb') as encode_file:
                encode_key = encode_file.read()
            new_master_key = security.master_key(new_pass)
            new_encode_key = security.decrypt(encode_key, master_key)
            new_encode_key = security.encrypt(new_encode_key, new_master_key)
            mainf = open("maininf.conf", 'w')
            mainf.write(change_login + ' ' + security.hash_password(new_pass))
            mainf.close()
            secretfile = open("secretinf.conf", 'wb')
            secretfile.write(new_master_key)
            secretfile.close()
            encodefile = open("encodeinf.conf", 'wb')
            encodefile.write(new_encode_key)
            encodefile.close()
            print("Ваш пароль изменен успешно")
            os.chdir('..')
            os.chdir('..')
            os.chdir('..')
            return True
