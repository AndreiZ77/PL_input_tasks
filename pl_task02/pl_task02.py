#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Задача:
В файле хранятся координаты вершин четырехугольника в порядке обхода фигуры по часовой стрелке в виде:
<координата x1> <координата y1>
<координата x2> <координата y2>
<координата x3> <координата y3>
<координата x4> <координата y4>
Считаем, что полученные из файла вершины гарантированно образуют выпуклый четырехугольник.
Написать программу, которая считывает координаты из файла. При запуске ждет от пользователя
ввода координат некой точки и выводит один из четырех возможных результатов:
точка внутри четырехугольника
точка лежит на сторонах четырехугольника
точка - вершина четырехугольника
точка снаружи четырехугольника

Входные данные:
- файл координат четырехугольника, по умолчанию файл quad01,
  должен находится в директории скрипта;
- введенные пользователем координаты проверяемой точки X Y через пробел.

Запуск скрипта в командной строке:
$ python3 pl_task02.py -f <filename>

Примеры:
$ python3 pl_task02.py
$ python3 pl_task02.py -f quad02

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
    parser.add_argument('-f', '--filename', nargs='?', default='quad01')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    fname = namespace.filename

    def vectors_calc(x1, y1, x2, y2, x3, y3):
        # произведение 2-х векторов заданных координатами 3-х точек, одна общая
        x12, y12 = x2-x1, y2-y1
        x13, y13 = x3-x1, y3-y1
        return y12 * x13 - x12 * y13

    try:
        x, y = map(float, input("введите через пробел X Y координаты точки:").split())
        result=[]
        x0, y0 = '', ''
        # обход вершин четырехугольника и вычисления произведения векторов
        # из двух вершин и заданной точки
        with open(fname) as f:
            for line in f:
                xc, yc = map(float, line.split())
                if x0:
                    result.append(vectors_calc(x0, y0, xc, yc, x, y))
                else:
                    x1, y1 = xc, yc
                x0, y0 = xc, yc
            result.append(vectors_calc(x0, y0, x1, y1, x, y))

        # формируем ответ по результатам рассчета
        answer = "точка внутри четырехугольника"
        for res in result:
            if res == 0:
                result.remove(res)
                if 0 in result:
                    answer = "точка - вершина четырехугольника"
                else:
                    answer = "точка лежит на сторонах четырехугольника"
                break
            elif res < 0:
                answer = "точка снаружи четырехугольника"
                break
        print(answer)

    except:
        print("Error. Values is not correct!")

