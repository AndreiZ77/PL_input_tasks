#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Задача:
В течение дня в банк заходят люди, у каждого человека есть время захода в банк и время выхода.
Всего за день у банка было N посетителей. Банк работает с 8:00 до 20:00. Человек посещает банк только
один раз за день. Написать программу, которая определяет периоды времени, когда в банке было максимальное
количество посетителей. Входные данные о посетителях программа должна получать из файла,
формат файла - произвольный, файл высылается вместе с решением.

Входные данные:
- файл посещений, в каждой строке - временной интервал нахождения в банке одного клиента,
  по умолчанию файл bank20200131 должен находится в директории скрипта;
- размер временного периода в минутах, для определения макисмального количества посетителей,
  по умолчанию = 60;
- количество наиболее эффективных периодов посещения, для вывода, по умолчанию = 3.

Запуск скрипта в командной строке:
$ python3 pl_task04.py -f <filename> -s <period size> -n <number of periods>

Примеры:
$ python3 pl_task04.py
$ python3 pl_task04.py -s 30 -n 5
$ python3 pl_task04.py -s 120
$ python3 pl_task04.py -f bank20200131 -s 180 -n 2

Важно:
- в ОС должен быть установлен Python 3.6+
- файл данных должен лежать в директории скрипта;
- в файле не должно быть пустых строк.
"""



import argparse
import sys
from datetime import time


def createParser():
    # парсер параметров
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', nargs='?', default='bank20200131')
    parser.add_argument('-s', '--size_period', nargs='?', default=60, type=int)
    parser.add_argument('-n', '--number_periods', nargs='?', default=3, type=int)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    fname = namespace.filename
    grad = namespace.size_period  # размер периода в минутах для взятия максимального значения
    number_periods = namespace.number_periods  # кол-во периодов с максимальными значениями для вывода
    print(f"Файл данных: {fname}, размер периода: {grad} минут, "
          f"смотрим эффективных периодов: {number_periods}")

    m_min = 480  # 8:00 в минутах
    m_max = 1199  # 19:59 в минутах


    def time_minutes(line):
        # перевод в минуты начала и конца интервала посещения человеком банка
        time_input = int(line[:2]) * 60 + int(line[3:5])
        time_output = int(line[6:8]) * 60 + int(line[9:])
        return time_input, time_output


    def time_max(people_period):
        # определение времени начала и конца интервала максимального по посещаемости
        max_value = max(people_period)
        idx = people_period.index(max_value)
        begin = idx * grad + m_min
        start = time(int(begin // 60), int(begin % 60)).strftime('%H:%M')
        finish = time(int((begin + grad) // 60), int((begin + grad) % 60)).strftime('%H:%M')
        return start, finish, max_value


    # проверка и подготовка начальных значений
    if grad > (m_max - m_min):
        grad = m_max - m_min + 1
    people_period = [0 for i in range((m_max - m_min) // grad + 1)]

    try:
        # расчет значений посещения по временным интервалам на основании данных файла
        with open(fname) as f:
            for line in f:
                time_input, time_output = time_minutes(line)
                key_input = (time_input - m_min) // grad
                people_period[key_input] += 1
                key_output = (time_output - m_min - 1) // grad
                if key_output > key_input:
                    people_period[key_output] += 1

        # print(people_period)
        # поиск временных интервалов с максимальными значениями
        for i in range(number_periods):
            values = time_max(people_period)
            print(f"{values[2]} человек(а) посетило банк в период: {values[0]} - {values[1]}")
            people_period.remove(values[2])
            if people_period == []:
                break
    except:
        print("Error. The input values is not correct!")
