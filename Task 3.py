# Напишите функцию, которая будет принимать число и проверять, можно ли его записать в виде числа 2 в какой-нибудь степени.
# def check_extent(n):
#     if n & (n - 1) == 0:
#         return True
#     else:
#         return False
# print(check_extent(8))

# Напишите функцию, которая будет менять регистр букв в строке так, чтобы перевести ее в т. н. spongecase.
# text = 'PYTHON python'
# def string_to_spongecase(some_text: str):
#     some_text_new = ''
#     for word in some_text.split():
#         for i, char in enumerate(word):
#             if char.isalpha():  # Проверяем, является ли символ буквой
#                 if i % 2 == 0:  # Проверяем четность положения символа
#                     some_text_new += char.lower()
#                 else:
#                     some_text_new += char.upper()
#             else:
#                 some_text_new += char
#         some_text_new += ' '  # Добавляем пробел после каждого слова
#     return some_text_new.strip()  # Убираем лишний пробел в конце строки
#
# print(string_to_spongecase(text))

# Напишите функцию для поиска самого большого числа в списке. Используйте при этом рекурсию (а метод max() не используйте).
# import random
# spisok = random.sample(range(-99, 99), random.randint(1, 19))
# print(spisok)
# def find_max_number(some_spisok: list):
#     max_num = float('-inf')
#     if not some_spisok:
#         return None
#     for elem in some_spisok:
#         if isinstance(elem, list):
#             maxi = find_max_number(elem)
#             if maxi > max_num:
#                 max_num = maxi
#         elif elem > max_num:
#             max_num = elem
#     return max_num
# print(find_max_number(spisok))

# Напишите функцию, которая будет определять, является ли переданная ей последовательность
# линейной, квадратичной или кубической.
# import random
# spisok = random.sample(range(-99, 99), random.randint(1, 19))
# print(spisok)
# spisok1 = [2, 4, 6, 8]
# spisok2 = [2, 8, 16]
# spisok3 = [3, 9, 81]
# def check_consistency(some_spisok: list):
#     for index in range(2, len(some_spisok)):
#         current_element = some_spisok[index]
#         prev_element = some_spisok[index - 1]
#         prev_prev_element = some_spisok[index - 2]
#
#         if current_element - prev_element == prev_element - prev_prev_element:
#             return 'линейная последовательность'
#         elif current_element == prev_element**2:
#             return 'квадратичная последовательность'
#         elif current_element == prev_element**2:
#             return 'квадратичная последовательность'
#         elif current_element == prev_element**3:
#             return 'кубическая последовательность'
#     else:
#         return 'неизвестная последовательность '
# print(check_consistency(spisok))
# print(check_consistency(spisok1))
# print(check_consistency(spisok2))
# print(check_consistency(spisok3))

# Напишите функцию, которая будет принимать список цифр и проверять,
# встречается ли заданная цифра указанное число раз подряд. Функция должна возвращать True или False.
# spisok = [2, 2, 2, 4, 5]
# print(spisok)
# def check_repeat_number_some_time(some_spisok: list, repeat_num: int, num_to_check: int):
#     counter = 0
#     flag = False
#     for elem in some_spisok:
#         if elem == num_to_check:
#             counter += 1
#             if counter != repeat_num:
#                 flag = False
#             else:
#                 flag = True
#     return flag
#
# print(check_repeat_number_some_time(spisok, 3, 2))

# Завод по производству фруктовых соков помечает свою продукцию специальными идентификаторами.
# Каждый ID составляется из трех первых букв названия фрукта и объема упаковки.
# Напишите функцию, которая будет создавать ID продукта для фруктовых соков.
# Примеры
#
#  get_drink_ID("apple", "500ml") ➞ "APP500"
#  get_drink_ID("pineapple", "45ml") ➞ "PIN45"
#  get_drink_ID("passion fruit", "750ml") ➞ "PASFRU750"
#
# Примечания:
#
#     Объем упаковки будет передаваться в виде строки, всегда в миллилитрах.
#     Буквы нужно возвращать в верхнем регистре.
# def create_id_product(product: str, volume: str):
#     id_out = ''
#     words = product.split()
#     for word in words:
#         id_out += word[:3].upper()
#     vol = volume[:-2] if len(volume) > 1 else volume  # Проверка на длину volume перед отсечением
#     id_out += vol
#     print(id_out)
#
# print(create_id_product('milk', '500ml'))


# Написать функцию, которая возвращает количество списков внутри списка.
# import random
# nested_list = []
# for _ in range(5):  # Определим количество вложенных списков
#     inner_list = random.sample(range(1, 20), random.randint(1, 10))  # Генерируем случайные списки
#     nested_list.append(inner_list)
# print(nested_list)
# def count_nested_lists(some_nested_list: list):
#     counter = 0
#     if not some_nested_list:
#         return 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             counter += 1
#
#         else:
#             counter_i = count_nested_lists(elem)
#     return counter
# print(count_nested_lists(nested_list))

# Создайте функцию, которая будет принимать строку и цензурировать (закрывать звездочками) слова длиннее четырех букв.
# import string
# text = 'i like python very much!'
# translator = str.maketrans('', '', string.punctuation)
# text_new = text.translate(translator)
# print(text_new)
# def censor_words_longer_lenght(some_text: str, lenght):
#     new_text = ''
#     words = some_text.split()
#     for word in words:
#         if len(word) >= lenght:
#             new_text += '*' * len(word) + ' '
#         else:
#             new_text += word + ' '
#
#     return new_text.strip()
#
# print(censor_words_longer_lenght(text_new, 4))