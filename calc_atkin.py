# mypy: ignore-errors
import os
import math
from sys import argv
import multiprocessing as mp
import time
import timeit
import progressbar


def Atkins(limit: int, s1: int, s2: int, s3: int):
    bar = progressbar.ProgressBar().start()
    persent = float(100 / limit)
    progress = float(0)
    if s1 == 1:
        way = "first.txt"
        status = "1 процесс"
        i = 1
    elif s2 == 1:
        way = "second.txt"
        status = "2 процесс"
        i = 2
    elif s3 == 1:
        way = "third.txt"
        status = "3 процесс"
        i = 3
    sieve = [False] * (limit+1)
    t = time.time()
    t = int(t)
    for x in range(i, int(math.sqrt(limit)) + 1, 3):
        progress += persent
        bar.update(progress)
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
            if int(time.time())-t == 6:
                print(x)
                t = time.time()
                t = int()
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
            if int(time.time())-t == 9:
                print(x)
                t = time.time()
                t = int(t)
    bar.finish()
    print(status + '\n')
    with open(way, "w", encoding='utf-7') as file_atk:
        for x in sieve:
            string = str(x) + '\n'
            file_atk.write(string)


def read_files() -> list:
    print("Выполняется чтение..." + "\n")
    with open('first.txt', 'r', encoding='utf-8') as file_1:
        first_read = file_1.read()
        list_1 = first_read.split("\n")
    with open('second.txt', 'r', encoding='utf-8') as file_2:
            first_read = file_2.read()
            list_2 = first_read.split("\n")
    with open('third.txt', 'r', encoding='utf-8') as file_3:
        first_read = file_3.read()
        list_3 = first_read.split("\n")
    list_123 = [0] * len(list_1)
    lens = len(list_1)
    for i in range(0, lens):
        if list_1[i] == "False":
            z = False
        else:
            z = True
        if list_2[i] == "False":
            zx = False
        else:
            zx = True
        if list_3[i] == "False":
            xz = False
        else:
            xz = True
        list_123[i] = (z + zx + xz) % 2
    list_4 = [0] * len(list_123)
    print("Часть уже выполнилась..." + "\n")
    for id, x in enumerate(list_123):
        if x == 1:
            if id % 5 == 0:
                pass
            else:
                list_4[id] = id
    return list_4


def starts(limit: int):
    with mp.Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(Atkins,
                             iterable=[
                                       [limit, 1, 0, 0],
                                       [limit, 0, 1, 0],
                                       [limit, 0, 0, 1]
                                      ],
                             )
        my_pool.close()


if __name__ == '__main__':
    try:
        if int(argv[1]) > 0:
            pass
        elif int(argv[1]) < 0:
            raise Exception
        elif int(argv[1]) == 0:
            raise Exception
        else:
            raise Exception
        limit = int(argv[1])
        a = timeit.default_timer()
        starts(limit)
        time_list = read_files()
        bar_read = progressbar.ProgressBar().start()
        progress_final = float(0)
        persent_final = float(100 / limit)
        print("Выполняется финальная часть...")
        while len(time_list) > limit:
            time_list.pop()
        while False in time_list:
            time_list.remove(False)
            progress_final += persent_final
            bar_read.update(progress_final)
        time_list.sort()
        bar_read.finish()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for p in time_list:
                string = ""+str(p)+"\n"
                file.write(string)
        print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")
    except Exception:
        print("Неправильный аргумент")
    except BaseException:
        print("Вы нажали на Ctrl + C")

