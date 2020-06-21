import os
import math
from sys import argv
import multiprocessing as mp
from time import time, sleep
import timeit


def Atkins(limit: int, s1: int, s2: int, s3: int):
    if s1 == 1:
        way = "first.txt"
        status = "1 процесс"
        tick = 1
    elif s2 == 1:
        way = "second.txt"
        status = "2 процесс"
        tick = 2
    elif s3 == 1:
        way = "third.txt"
        status = "3 процесс"
        tick = 3
    sieve = [False] * (limit + 1)
    check = 0
    for x in range(1, int(math.sqrt(limit)) + 1, tick):
        for y in range(1, int(math.sqrt(limit)) + 1, tick):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
            if check == 100000:
                print (x, y, status)
                check = 0
            check += 1
    for x in range(5, int(math.sqrt(limit)), tick):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    print(status + '\n')
    with open(way, "w", encoding='utf-7') as file_atk:
        for id, x in enumerate(sieve):
            if x == 1:
                result = id
                if result % 5 == 0:
                    pass
                else:
                    string = str(result) + '\n'
                    file_atk.write(string)


def read(way: str) -> list:
    with open(way, "r", encoding='utf-7') as first:
        first_read = first.read()
        first_list = first_read.split("\n")
        second_list = [0]*len(first_list)
        for id, i in enumerate(first_list):
            if i == '':
                pass
            else:
                new_i = int(i)
                count_list = first_list.count(i)
                if count_list == 1:
                    second_list[id] = new_i
    second_list.remove(0)
    return second_list


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


def start_read():
    with mp.Pool(processes=3) as my_pool:
        p1 = my_pool.starmap(read,
                             iterable=[
                                       ["first.txt"],
                                       ["second.txt"],
                                       ["third.txt"]
                                      ],
                             )
        my_pool.close()
        return p1


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
        time_list = start_read()
        tl1 = len(time_list[1])
        tl2 = len(time_list[2])
        None_list = [None]*(tl1+tl2)
        i = len(time_list[0])-1
        result_list = time_list[0] + None_list
        None_list = time_list[1] + time_list[2]
        for x in None_list:
            if result_list.count(x) != 0:
                pass
            elif result_list.count(x) == 0:
                i += 1
                result_list[i] = x
        while None in result_list:
            result_list.remove(None)
        result_list.sort()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for p in result_list:
                string = ""+str(p)+"\n"
                file.write(string)
        print("Алгоритм считал:", timeit.default_timer()-a, "секунд\n")
    except Exception:
        print("Неправильный аргумент")
    except BaseException:
        print("Вы нажали на Ctrl + C")
