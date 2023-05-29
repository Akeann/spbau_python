#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # Импортируем библиотеку math
import numpy  # Импортируем библиотеку numpy
import matplotlib.pyplot as mpp  # Импортируем модуль pyplot из matplotlib

# Эта программа рисует график функции, заданной выражением ниже

# Следующий блок не будет выполняться при импорте программы, как модуля
if __name__ == '__main__':
    arguments = numpy.arange(0, 200, 0.1)  # Список из [0, 200) с шагом 0.1
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # Генератор списка
    )  # График с x из arguments, y из списка, заданного генератором
    mpp.show()  # Отображаем построенные графики
