# Напишите функцию, которая будет принимать три числа: ширину и высоту
# прямоугольника и радиус круга и возвращать True, если прямоугольник может поместиться в круг.
# import math
# width = input('введите ширину прямоугольника ')
# hight = input('введите высоту прямоугольника ')
# radius = input('введите радиус круга ')
# square_circle = math.pi * int(radius) ** 2
# square_rectangle = int(width) * int(hight)
# if square_circle >= square_rectangle:
#     print(True)
# else:
#     print(False)

# Напишите функцию, которая будет возвращать список чисел, где каждое число — накапливающаяся сумма чисел исходного списка.
#
# Напишите функцию, создающую гистограммы. Она должна принимать список целых чисел и строку — символ,
# который будет формировать столбцы.
# list = [2, 4, 3, 0, 7]
# # def make_gistogramma(some_list: list, symbol):
# #     for number in some_list:
# #         print(symbol * number)
# # print(make_gistogramma(list, symbol='*'))

# Форматирование строки с несколькими переменными
# first_name = "John"
# last_name = "Doe"
# age = 30
# print('My name is %s %s, and I am %d years old.' % (first_name, last_name, age))
#
# # Использование разных типов данных
# price = 19.99
# quantity = 2
# total_cost = price * quantity
# print('The total cost is $%.2f' % total_cost)

# Напишите функцию, которая будет проверять, является ли целое число совершенным числом.
# Например, 6 — совершенное число, ведь 1 + 2 + 3 = 6.
# def check_perfect_number(number: int):
#     if number == 1:
#         return False
#
#     sum_divisors = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum_divisors += i
#
#     return sum_divisors == number
#
# print(check_perfect_number(6))

# Напишите функцию, которая будет принимать начальное и конечное значения диапазона
# и возвращать список всех чисел, входящих в этот диапазон
# start = int(input('start number '))
# finish = int(input('finish number '))
# list_out = [num for num in range(start, finish + 1)]
# print(list_out)

# Напишите функцию, которая будет принимать начальное и конечное число в диапазоне чисел
# и возвращать сумму всех чисел этого диапазона.
# start = int(input('start number '))
# finish = int(input('finish number '))
# list_out = sum([num for num in range(start, finish + 1)])
# print(list_out)

# Напишите функцию, принимающую начальное и конечное значения диапазона чисел и возвращающую
# наибольшее простое число в этом диапазоне.
# def simple_number_list(start, finish):
#     lst_out = []
#     for num in range(start, finish + 1):
#         is_prime = True
#         for n in range(2, int(num**0.5) + 1):
#             if num % n == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             lst_out.append(num)
#     return lst_out
#
# result = simple_number_list(2, 58)
# print(result)
#
# def return_max_num(some_list_simple_nums: list):
#     return max(some_list_simple_nums)
#
# print(return_max_num(result))