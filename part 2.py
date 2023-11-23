# Напишите функцию. Она должна принимать число, цифры которого будут перемножаться
# между собой, пока не получится однозначное число.
# def multiply_until_single_digit(number):
#     new_number = None
#     while number >= 10:
#         resalt = 1
#         for num in str(number):
#             resalt *= int(num)
#             number = resalt
#     return number
# print(multiply_until_single_digit(9))

# Напишите функцию, которая будет принимать строку и проверять, является ли инпут телефонным номером в валидном формате.
# number = input('введите ваш номер телефона: ')
# begin_numb = ['096', '050', '067', '078']
# def check_valid_format_phone(some_number: str):
#     assert len(some_number) == 10, 'номер телефона содержит 10 цифр'
#     assert some_number[:3] in begin_numb, 'код оператора неверный'
#     if some_number.isdigit():
#         return True
#     else:
#         return False
# print(check_valid_format_phone(number))

# Напишите функцию, которая будет принимать строку из слов и возвращать строку,
# в которой эти слова будут отсортированы по последним буквам.
# import string
# sample_text = "Это пример текста.  Здесь мы можем увидеть, как работает программа."
# translator = str.maketrans('', '', string.punctuation)
# new_text = sample_text.translate(translator)
# new_text1 = new_text.replace(',', '')
# new_text2 = new_text1.replace('.', '')
# print(new_text2)
# def sort_string_on_end_words(some_text: str):
#     words_to_sort = []
#     list_out = []
#     word = ''.join(some_text).lower().split()
#     words_to_sort. append(word)
#     for elem in words_to_sort:
#         for letter in elem:
#             list_out = sorted(elem, key=lambda let: let[-1])
#     return list_out
# print(sort_string_on_end_words(new_text2))

# Нужно написать функцию, которая вернет True, если в списке больше нечетных чисел, и False — если наоборот.
# import random
# some_list = random.sample(range(1, 100), random.randint(1, 11))
# print(some_list)
# def checking_even_or_odd_numbers(list_to_check: list):
#     even_num = 0
#     odd_num = 0
#     for num in list_to_check:
#         if num % 2 == 0:
#             even_num += 1
#         else:
#             odd_num += 1
#     if odd_num > even_num:
#         return True
#     else:
#         return False
# print(checking_even_or_odd_numbers(some_list))

# Если 2^N+1 без остатка делится на 2*N+1, то число N считается числом Керзона.
# Реализуйте функцию, которая будет принимать целое число num и возвращать True, если num — число Керзона
# def check_num_kerzone(number_to_check):
#     if (2 ** number_to_check + 1) % (2 * number_to_check + 1) == 0:
#         return True
#     else:
#         return False
# print(check_num_kerzone(16385))
# print(check_num_kerzone(33))
# print(check_num_kerzone(168))

#Напишите функцию, которая находила бы сумму элементов от 1 до N (включительно).
# def summa_number(n):
#     summa = 0
#     if n == 0:
#         return 0
#     else:
#         summa = n + summa_number(n - 1)
#     return summa
# print(summa_number(13))

# Напишите класс Name и создайте атрибуты для передаваемых имени и фамилии (fname и lname),
# а также атрибут fullname, возвращающий имя и фамилию, атрибут initials,
# возвращающий первые буквы имени и фамилии с точкой между ними.
# class Name:
#
#     def __init__(self, fname, lname):
#         self.fname =fname
#         self.lname = lname
#
#     def fullname(self):
#         return f'{self.fname.capitalize()} {self.lname.capitalize()}'
#
#     def __str__(self):
#         return f'{self.fname[0].capitalize()}. {self.lname[0].capitalize()}.'
#
# person1 = Name('kat', 'lili')
# print(person1.fullname())
# print(person1)

# Напишите функцию, которая будет делить список чисел пополам, определять суммы чисел в половинах списка и сравнивать их.
# import random
# spisok = random.sample(range(1, 99), random.randint(1, 19))
# print(spisok)
# def sum_comparison_two_halves_list(some_list: list):
#     len_half = len(some_list) // 2
#     summa_1 = sum(some_list[:len_half])
#     summa_2 = sum(some_list[len_half:])
#     return len_half, summa_1, summa_2
# print(sum_comparison_two_halves_list(spisok))

# Напишите функцию, которая будет возвращать количество повторов символов в строке.
# Функция должна считать повторы символов, а не вхождения
# text = 'i like python very much!'
# def count_some_symbol(some_text: str, symbol):
#     counter = 0
#     for letter in some_text.lower():
#         if letter == symbol.lower():
#             counter += 1
#     return counter
# print(count_some_symbol(text, 'Y'))

# Напишите функцию, которая будет находить самое длинное слово в предложении.
# Если будет найдено два и больше слов одинаковой длины, нужно вернуть первое из них.
# text = 'Python — это высокоуровневый язык программирования общего назначения. ' \
#        'Он известен своей удобочитаемостью и понятным синтаксисом, ' \
#        'что делает его отличным языком для начинающих.' \
#        ' Python широко используется в различных областях, ' \
#        'таких как веб-разработка, научные вычисления, ' \
#        'искусственный интеллект и т. д. и многое другое. ' \
#        'Python имеет большое и активное сообщество разработчиков,' \
#        ' а это значит, что доступно множество ресурсов и библиотек. ' \
#        'Независимо от того, новичок вы или опытный программист, ' \
#        'Python — это универсальный язык, который можно использовать для широкого спектра приложений.'
# import string
# translator = str.maketrans('', '', string.punctuation)
# new_text = text.translate(translator)
# print(new_text)
# def largest_word(some_text: str):
#        logest_word = ''
#        max_len_word = 0
#        if len(some_text.split()) == 0:
#               return "Текст не содержит слов"
#        for words in some_text.split():
#               word = words.lower()
#               if len(word) > max_len_word:
#                      max_len_word = len(word)
#                      logest_word = word
#        return logest_word
# print(largest_word(new_text))

# Сиракузская последовательность генерируется следующим образом.
# Берем любое натуральное число n. Если оно четное, то делим его на 2, а если нечетное,
# то умножаем на 3 и прибавляем 1 (получаем 3n + 1).
# def generate_consistency(n):
#     list_out = []
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#             list_out.append(n)
#         elif n % 2 != 0:
#             n = 3 * n + 1
#             list_out.append(n)
#     return list_out
# print(generate_consistency(15))
