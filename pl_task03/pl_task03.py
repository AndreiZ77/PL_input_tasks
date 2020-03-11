#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Задача:
В магазине 5 касс, в каждый момент времени к кассе стоит очередь некоторой длины.
Каждые 30 минут измеряется средняя длина очереди в каждую кассу и для каждой кассы
это значение (число вещественное) записывается в соответсвующий ей файл (всего 5 файлов),
магазин работает 8 часов в день. Рассматривается только один день.
На момент запуска приложения все значения уже находятся в файлах. Написать программу,
которая по данным замеров определяет интервал времени, когда в магазине было
наибольшее количество посетителей за день.

Входные данные:
- файлы данных с касс магазина, по умолчанию файлы: k1, k2, k3, k4, k5;
- время открытия магазина в часах, по умолчанию 10 часов.

Запуск скрипта в командной строке:
$ python3 pl_task03.py -t 10 -f <file 1> <file 2> <file 3> ... <file n>

Примеры:
$ python3 pl_task03.py
$ python3 pl_task03.py -t 8
$ python3 pl_task03.py -t 11 -f k1 k2 k3

Важно:
- в ОС должен быть установлен Python 3.6+
- файлы данных должны лежать в директории скрипта;
- в файлах не должно быть пустых строк.
"""


import sys
import argparse


def createParser():
    # парсер параметров
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--opening_time', nargs='?', default=10, type=int)
    parser.add_argument('-f', '--filename', nargs='+', default=['k1', 'k2', 'k3', 'k4', 'k5'])
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    open_time = namespace.opening_time

    try:
        # читаем данные из файлов касс магазина
        data = []
        for fname in namespace.filename:
            with open(fname) as file:
                data.append([float(line) for line in file])

        # суммируем значения по 16ти временным интервалам (8ч по 30 мин)
        result = []
        for j in range(16):
            result.append(
               round( sum([data[k][j] for k in range(len(namespace.filename))]), 2)
            )

        # расчет значений времени интервала или интервалов с максимальным кол-вом клиентов
        print("Максимальное значение клиентов в магазине:")
        max_value = max(result)
        while True:
            idx = result.index(max_value)

            t = idx + 1
            if t % 2 == 0:
                answer = str(open_time - 1 + t // 2) + ':30 - ' + str(open_time + t // 2) + ':00'
            else:
                answer = str(open_time + t // 2) + ':00 - ' + str(open_time + t // 2) + ':30'
            print(f'за интервал {answer} среднее значение составило: {max_value} покупателя')

            result[idx] = 0
            if max_value not in result:
                break
    except:
        print("Error. The entered values is not correct!")





