"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""


def test_add():
    # TODO: додай тести для функції add
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(-1, 0) == -1


"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""


def test_is_even():
    # TODO: додай тести для функції is_even
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(-1) == False



"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""


def test_reverse_string():
    # TODO: додай тести для функції reverse_string
    assert reverse_string ('Sasha') == 'ahsaS'
    assert reverse_string('') == ''
    assert reverse_string('S') == 'S'


"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""


def test_find_min():
    # TODO: додай тести для функції find_min
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([1]) == 1
    assert find_min([-1, -3, -5]) == -5


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""


def test_contains_substring():
    # TODO: додай тести для функції contains_substring
    assert contains_substring('Aleksandra', 'Aleks') == True
    assert contains_substring('Aleksandra', 'dfjsdb') == False
    assert contains_substring('Aleksandra', '') == True


"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""


def test_factorial():
    # TODO: додай тести для функції factorial
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""


def test_divide():
    # TODO: додай тести для функції divide
    assert divide(2, 2) == 1
    assert divide(2, -2) == -1
    assert divide(2, 0) == ZeroDivisionError


"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""


def test_is_palindrome():
    # TODO: додай тести для функції is_palindrome
    assert is_palindrome('anna') == True
    assert is_palindrome('Anna') == False
    assert is_palindrome('') == True

"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""


def test_sum_list():
    # TODO: додай тести для функції sum_list
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([]) == 0
    assert sum_list([-1, -2, -3, -4]) == -10


"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""


def test_to_upper():
    # TODO: додай тести для функції to_upper
    assert to_upper('Simple text') == 'SIMPLE TEXT'
    assert to_upper('SIMPLE TEXT') == 'SIMPLE TEXT'
    assert to_upper('') == ''


