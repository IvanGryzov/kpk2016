#  Copyright 2016 Ivan Gryzov <Ivan_Gryzov@mail.ru>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import turtle
from math import sin, pi

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(10)


def draw_num(t, n, length=50):
    """ отрисовываем число индексными цифрами из текущей позиции
    размер по умолчанию 50 на входе t- объект turtle и n - число"""
    len1 = length / 2
    len2 = length / sin(pi / 4) / 2
    A = []  # длина вперд
    B = []  # угол поворота
    draw = []  # признак поднятости пера
    # 0
    A.append([len1, length, len1, length, 0])
    B.append([0, 90, 90, 90, 90])
    draw.append([True, True, True, True, True])
    # 1
    A.append([len1, length, len2, len1, 0])
    B.append([0, 90, 135, 45, 90])
    draw.append([False, True, True, False, False])
    # 2
    A.append([len1, -len1, len2, len1, len1, length, 0])
    B.append([0, 0, 45, 45, 90, 90, 90])
    draw.append([True, True, True, True, True, False, False])
    # 3
    A.append([len2, len1, len2, len1, length, 0])
    B.append([45, 135, -135, 135, 90, 90])
    draw.append([True, True, True, True, False, False])
    # 4
    A.append([len1, length, len1, len1, len1, length, 0])
    B.append([0, 90, 180, -90, -90, 180, 90])
    draw.append([False, True, True, True, True, False, False])
    # 5
    A.append([len1, len1, len1, len1, len1, length, len1, 0])
    B.append([0, 90, 90, -90, -90, -90, -90, 180])
    draw.append([True, True, True, True, True, False, False, False])
    # 6
    A.append([len1, len1, len1, len2, len2, len1, 0])
    B.append([0, 90, 90, -135, 180, 45, 90])
    draw.append([True, True, True, True, True, True, False])
    # 7
    A.append([len1, len2, len1, length, 0])
    B.append([90, -45, 135, 90, 90])
    draw.append([True, True, True, False, False])
    # 8
    A.append([len1, length, len1, len1, len1, -len1, len1, 0])
    B.append([0, 90, 90, 90, 90, 0, -90, 90])
    draw.append([True, True, True, True, True, True, True, False])
    # 9
    A.append([len2, len1, len1, len1, len1, -len2, 0])
    B.append([45, 45, 90, 90, 90, 45, -45])
    draw.append([True, True, True, True, True, True, False])

    def draw_digit(digit, length):
        """ рисует цифру digit - цифра length - размер Возвращаемся назад и смотрим туда же Перо остается поднятым"""
        for lenght, degree, pen in zip(A[digit], B[digit], draw[digit]):
            if pen:
                t.pendown()
            else:
                t.penup()
            t.left(degree)
            t.forward(lenght)
            t.penup()

    # тело функции draw_num
    st = str(n)
    for c in st:
        draw_digit(int(c), length)
        t.forward(length * 0.8)


# пример
def main():
    t.penup()
    t.backward(200)
    draw_num(t, 987654321)


main()
