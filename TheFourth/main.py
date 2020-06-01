import db
import security
import os
import note
import platform
import subprocess


if platform.system() == "Windows":
    try:
        p = subprocess.Popen(["notepad"])
        p.kill()
    except Exception:
        print("Блокнота нет")
        exit(0)
else:
    print("Это ж не винда")
    exit(0)


flag = True
flag_zam = True
while flag:
    try:
        print("Главное меню программы 4 лабораторной")
        print("\tУправление аккаунтом...")
        print("\tСоздать аккаунт - 1")
        print("\tАутентифицировать пользователя - 2")
        print("\tУдалить аккаунт - 3")
        print("\tИзменить пароль от аккаунта - 4")
        print("\tВыйти из программы - 5")
        command = int(input("Выберите действие:"))
        if command == 1:
            db.create_new_acc()
        if command == 2:
            login, check = db.auth_acc()
            if check is True:
                while flag_zam:
                    print("Меню работы с заметками")
                    print("\tСоздать заметку - 1")
                    print("\tИзменить заметку - 2")
                    print("\tУдалить заметку - 3")
                    print("\tУдалить все заметки - 4")
                    print("\tПолучить список заметок - 5")
                    print("\tПрочитать конкретную заметку - 6")
                    print("\tВыйти из программы - 7")
                    command_note = int(input("Выберите действие:"))
                    if command_note == 1:
                        note.create_note(login)
                    if command_note == 2:
                        note.change_note(login)
                    if command_note == 3:
                        note.delete_note(login)
                    if command_note == 4:
                        note.delete_all_notes(login)
                    if command_note == 5:
                        note.note_list(login)
                    if command_note == 6:
                        note.read_note(login)
                    if command_note == 7:
                        print("Осуществляется выход")
                        exit(0)
            else:
                print("Вы не смогли пройти аутентификацию")
                os.chdir('..')
                os.chdir('..')
        if command == 3:
            db.delete_acc()
        if command == 4:
            db.change_password()
        if command == 5:
            print("Осуществляется выход")
            exit(0)
        else:
            print("Работайте с меню!")
    except SyntaxError:
        print("Не та команда")
    except ValueError:
        print("Не тот ввод")
    except PermissionError:
        print("Вы не можете работать с программой из-за проблем с допуском")
        flag = False
        break
    except FileNotFoundError:
        print("Никогда не видел такого файла")
    except BaseException:
        print("Никогда не знаешь из-за чего может вылететь ошибка")
        flag = False
        break
