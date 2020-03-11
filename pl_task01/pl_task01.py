#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Задача:
Считать из файла последовательность целых чисел. Вычислить 90 персентиль, медиану, максимальное,
минимальное и среднее значения. На вход программа получает файл с числами. Каждое число в файле
находится на новой строке. Вывод в консоль должен быть следующим:
90 percentile <значение>
median <значение>
average <значение>
max <значение>
min <значение>

Входные данные:
- файл с последовательностью чисел, по умолчанию файл numbers01,
  должен находится в директории скрипта;

Запуск скрипта в командной строке:
$ python3 pl_task01.py -f <filename>

Примеры:
$ python3 pl_task01.py
$ python3 pl_task01.py -f numbers02

Важно:
- в ОС должен быть установлен Python 3.6+
- файл данных должен лежать в директории скрипта;
- в файле не должно быть пустых строк.
"""

import argparse
import sys

def createParser():
    # парсер параметров
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', nargs='?', default='numbers01')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    fname = namespace.filename

    try:
        with open(fname) as file:
            numbers = sorted([int(line) for line in file])

        # 90 персентиль
        # метод 1
        n = 0.9*(len(numbers)-1) + 1
        rang = int(n//1) # целая часть от n
        x = ((n%1)*100)//1/100 # дробная часть от n с округлением до двух знаков
        Vn, Vnext = numbers[rang - 1], numbers[rang]
        print("90 percentile", Vn + x*(Vnext - Vn))
        # # метод 2
        # n = 0.9*(len(numbers)+1)
        # rang = int(n//1) # целая часть от n
        # x = ((n%1)*100)//1/100 # дробная часть от n с округлением до двух знаков
        # Vn, Vnext = numbers[rang - 1], numbers[rang]
        # print("90 percentile", Vn + x*(Vnext - Vn))
        # медиана
        if len(numbers)%2 != 0:
            print("median", numbers[len(numbers)//2])
        else:
            print("median", (numbers[len(numbers)//2] + numbers[len(numbers)//2 + 1])/2)
        # среднее
        print("average", round((sum(numbers) / len(numbers)), 2) )
        print("max", numbers[len(numbers)-1])
        print("min", numbers[0])

    except:
        print("Error. Values is not correct!")
