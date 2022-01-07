"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*typles_convert_to_list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    list_of_data = []
    for i in typles_convert_to_list:
        if type(i) == int:
            data = i ** 2
            list_of_data.append(data)
    return list_of_data


# Constants
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_odd_num(num):
    if (num % 2) == 0:
        return True
    else:
        return False


def filter_even_num(num):
    if (num % 2) != 0:
        return True
    else:
        return False


def is_prime(n):
    if n == 0 or n == 1:  # 1 - не принято считать простым числом
        return False
    if n % 2 == 0:
        return n == 2  # True
    d = 3  # будем перебирать только нечетные делители, если число не делится на два.
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n  # True


def filter_numbers(list_of_int_num, operation):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    list_of_output_data = []
    for i in list_of_int_num:
        if type(i) == int:
            if operation == "odd":
                list_of_output_data = list(filter(filter_even_num, list_of_int_num))
            elif operation == "even":
                list_of_output_data = list(filter(filter_odd_num, list_of_int_num))
            elif operation == "prime":
                list_of_output_data = list(filter(is_prime, list_of_int_num))
            return list_of_output_data
        return False
