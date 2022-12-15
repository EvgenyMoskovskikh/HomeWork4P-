# 1. Вычислить число c заданной точностью d
# import math

# d = input('Введите число для заданной точности: ')
# d = d[2:len(d)]
# print('Число Пи с заданной точностью ', {d}, 'равняется ', round(math.pi,len(d)))

# Решение от преподавателя:

# from math import pi    

# def format_by_mask(num: float, accuracy: float) -> float:
#     """"форматирует число по заданной маске"""
#     accuracy = str(accuracy)
#     accuracy = len(accuracy[accuracy.find('.')+1::])
#     return float(f'{pi:0.{accuracy}f}')    # f'a:0.3f'

# d = input('Введите точность в формате "0.001": ')
# print(format_by_mask(pi, d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 
# lst = []
# numb_n = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# lst = list(set(lst))  
# lst.sort()      
# print(f"Простые множители числа {numb_n} приведены в списке: {lst}")

# # Решение от преподавателя
# def dividers(a: int, uniq: bool = False) -> list[int]:
#     """"Возвращает список простых делителей числа.
#     uniq = True вернет список уникальных делителей"""
#     i = 2
#     dividers = []
#     while a != 1:
#         while a % i == 0:
#             dividers.append(i)
#             a //= i
#         i += 1
#     if uniq:
#         return list(set(dividers))
#     else:
#         return dividers

# a = 81
# print(f'Список натуральных делителей числа {a}:{dividers(a)}')
# print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random
# lst = [random.randint(0, 6) for i in range(11)]
# print(lst)
# def return_unique(lst):
#     result = []
#     count = 0
#     for i in range (0, len(lst)):
#         for j in range (0, len(lst)):
#             if lst[i] == lst[j]:
#                 count += 1
#         if count < 2:
#             result.append(lst[i]) 
#         count = 0  
#         j = 0   
#     return result  
# print(f"Список из неповторяющихся элементов: {return_unique(lst)}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k

# import random

# k = int(input("Введите натуральную степень: "))
# ratio = []
# for i in range(k + 1):
#     ratio.append(random.randint(0, 100))


# def create_polynomial(some_list):
#     result = ""
#     if len(some_list) < 1:
#         result = "x = 0"
#     else:
#         for i in range(len(some_list)):
#             if i != len(some_list) - 1 and some_list[i] != 0 and i != len(some_list) - 2:
#                 result += f"{some_list[i]}x^{len(some_list) - i - 1}"
#                 if some_list[i + 1] != 0:
#                     result += " + "
#             elif i == len(some_list) - 2 and some_list[i] != 0:
#                 result += f"{some_list[i]}x"
#                 if some_list[i + 1] != 0:
#                     result += " + "
#             elif i == len(some_list) - 1 and some_list[i] != 0:
#                 result += f"{some_list[i]} = 0"
#             elif i == len(some_list) - 1 and some_list[i] == 0:
#                 result += " = 0"
#     return result


# def write_file(name, st):
#     with open(name, 'w') as data:
#         data.write(st)


# write_file("file.txt", create_polynomial(ratio))
# print("Уравнение записано в файл!")

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import sympy
import random

def polin_wr(name_file):
    k = int(input('Введите степень: '))
    koef = [str(random.randint(0, 100)) for i in range(k + 1)]
    polin = ''
    for i in range(k + 1):
        if i == 0: polin = koef[i]
        elif i ==1: polin = f'{koef[i]}*x + {polin}'
        else: polin =  f'{koef[i]}*x**{i} + {polin}'
    with open(name_file, 'w') as f:
        f.write(polin) 

polin_wr('f_1.txt')
polin_wr('f_2.txt')

with open('f_1.txt', 'r') as f1, open('f_2.txt', 'r') as f2,\
    open('f_rez.txt', 'w') as frez:

    p1 = f1.read()
    p2 = f2.read() 

    x = sympy.Symbol('x')

    rez = sympy.simplify(eval(p1) + eval(p2))

    frez.write(str(rez))


# ========== 
# def get_polynom(file_num: int) -> str:
#     """Взять многочлен из файла"""
#     with open(f'file{file_num}.txt', 'r') as f:
#         polynom = f.readline()
#     return polynom


# """Сумма двух многочленов"""
# polynom1 = sympy.simplify(get_polynom(1))
# polynom2 = sympy.simplify(get_polynom(2))
# print('\t\t' + str(polynom1) + '\n\t\t' + str(polynom2))
# x = sympy.Symbol('x')
# polynom = str(sympy.simplify(polynom1 + polynom2))
# print('Сумма = ' + polynom)
# with open('file3.txt', 'w') as f:
#     f.write(polynom)