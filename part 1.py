# Напишите функцию, которая принимает список и делает первый элемент списка последним.
# Если список пустой или состоит из одного элемента, он должен остаться неизменным.
# spisok = ['apple', 'kiwi', 'lemon', 'orange']
# def makes_first_item_in_list_the_last(some_list: list):
#     for elem in some_list:
#         if len(some_list) <= 1:
#             return some_list
#         else:
#             some_list[0], some_list[-1] = some_list[-1], some_list[0]
#         return some_list
# print(spisok)
# print(makes_first_item_in_list_the_last(spisok))

# Напишите программу, которая принимает текст и выводит два слова из этого текста:
# то, которое встречается в тексте чаще всего, и самое длинное.
# text = 'i like python! i can learn it! yes? it is difficult? but i can, i believe.'
# import string
# translator = str.maketrans('', '', string.punctuation)
# new_text = text.translate(translator)
# print(new_text)
# def print_longest_shortest_word(some_text: string):
#     dict_out = {}
#     max_len_word = ''
#     max_len = float('-inf')
#     max_count_word = ''
#     max_val = float('-inf')
#     for words in some_text.split():
#         word = ''.join(words)
#         if word not in dict_out:
#             dict_out[word] = 1
#         else:
#             dict_out[word] += 1
#         if len(word) > max_len:
#             max_len = len(word)
#             max_len_word = word
#         max_count_word = max(dict_out, key=dict_out.get)
#
#     return f'{max_len_word} самое длинное слово\n{max_count_word} - самое часто встречающееся слово '
# print(print_longest_shortest_word(new_text))

# Напишите функцию, которая будет принимать число num и возвращать его двойной факториал.
# Попробуйте решить при помощи рекурсии.
# def double_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * double_factorial((n - 2))
# print(double_factorial(5))

# Напишите функцию, которая будет принимать длину сторон треугольника (x, y и z) и определять, является ли он прямоугольным.
# a  = int(input('a: '))
# b  = int(input('b: '))
# c  = int(input('c: '))
# if a ** 2 + b ** 2 == c ** 2:
#     print(True)
# else:
#     print(False)

# Создайте класс, который будет принимать следующие четыре аргумента для каждого отдельного
# футболиста: name (имя), age (возраст), height (рост), weight (вес).
# class Football:
#
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
# man1 = Football('Bob', '28', '185', '80')
# man2 = Football('Tom', '29', '183', '81')
# man3 = Football('Timmy', '26', '195', '85')
# man4 = Football('Milly', '27', '190', '84')
# print(man1.__dict__)

# Напишите функцию, которая будет принимать вложенный список и возвращать общее количество чисел в нем.
# import random
# nested_list = []
# nested_lists = random.randint(1, 9) # сколько будет вложеных списков
# for _ in range(nested_lists):
#     number_inner = []
#     num_inner_elements = random.randint(1, 9) # сколько элементов будет внутри вложеного списка
#     for _ in range(num_inner_elements):
#         number_inner.append(random.randint(1, 100)) #числа внутри списков
#     nested_list.append(number_inner)
# print(nested_list)
# def count_elements_in_nested_list(some_nested_list: list):
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             counter_inner = count_elements_in_nested_list(elem)
#             counter += counter_inner
#         else:
#             counter += 1
#     return counter
# print(count_elements_in_nested_list(nested_list))

# Напишите функцию, которая будет принимать старую и новую цену товара и возвращать процент,
# на который цена повысилась или понизилась.
# product_1 = int(input('какая цена  товара? '))
# product_2 = int(input('какая  новая цена  товара? '))
# percent = abs(round(((product_2 - product_1) / product_1 * 100), 2))
# if product_1 > product_2:
#     print(f'удешевление на {percent} %')
# if product_1 < product_2:
#     print(f'подорожание на {percent} %')
