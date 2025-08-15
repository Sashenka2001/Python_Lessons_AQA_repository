
import math
"""
Домашнє завдання: Основи Python

**1.** Створіть три змінні з правильними іменами (англійською мовою): 
одну для збереження віку, 
одну для імені студента, 
одну для позначення чи є особа студентом. 
Додайте коментарі до кожної змінної.
"""
age = 23  # змінна для збереження віку
student_name = "Oleksandra"  # змінна для імені студента
is_student = True  # змінна для позначення чи є особа студентом

"""

**2.** Рзкоментуйте та виправте помилки в наступних назвах змінних.
Поясніть у коментарях, чому початкові назви неправильні:
"""
name = "John"  # не можна називаті змінну починаючи з цифри
user_age = 2  # не можна використовувати тире
price = 100  # не можна використовувати спецсимволи в назві змінних
class1 = "Math"  # не можна називати змінну зарезревованою для оператора назвою
"""
**3.** Створіть змінну з описовим ім'ям для збереження максимальної кількості студентів у групі. 
Присвойте їй значення 30.
"""
max_students_amount = 30

"""
**4.** Створіть змінні для збереження: 
назви курсу, 
кількості годин, 
вартості курсу. 
Використайте правильне іменування змінних.
"""
course_name = "AQA courses"
course_hours_count = 10
course_price_uah = 10000

"""
**5.** Розрхуйте та виведіть Затрати курсу: 
Затрати курсу  = кількість годин / вартість курсу
Використайте правильне іменування змінних.
"""
course_expenses = course_hours_count/course_price_uah

"""
**6.** Створіть змінні з різними способами запису чисел:
- Десяткове число: 42
- Двійкове число: 101010 (в двійковій системі)
- Шістнадцяткове число: 2A (в шістнадцятковій системі)
- Восьмеричне число: 52 (в восьмеричній системі)
"""
decimal_int = 42
binary_int = 0b101010
heximal_int = 0x2a
octal_int = 0o52

"""
**7.** Виконайте всі арифметичні операції (+, -, *, /, //, %, **) з числами 17 та 5. 
Виведіть результати з поясненнями.
"""
addition = 17 + 5
substraction = 17 - 5
multiplication = 17 * 5
division_with_remainder = 17 // 5
division_with_rounding = 17 / 5
remainder_from_division = 17 % 5
exponentiation = 17 ** 5
"""
**8.** Обчисліть площу кола з радіусом 7.5. Використайте значення π = 3.14159.
"""
s_circle = math.pi * 7.5
print(s_circle)
"""
**9.** Обчисліть залишок від ділення будь-якого числа на 7. 
Виведіть результат з числами 50, 33, 14.
"""
result = 200 % 7
numbers_list = [50, 33, 14]

for i in numbers_list:
    remainder = i % 7
    print(remainder)

"""
**10.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_of_the_black_sea = 436402
square_of_the_azov_sea = 37800
squares_sum = square_of_the_azov_sea + square_of_the_black_sea
print("Сума площин Азвоського та Чорного морів дорівнює", squares_sum, "км2")

"""
**11.** Створіть рядок з вашим повним ім'ям та виведіть:
- Перший символ
- Останній символ  
- Довжину рядка
"""
student_name_1 = "Oleksandra Dovha"
first_symbol = student_name_1[0]
last_symbol = student_name_1[-1]
length_of_name = len(student_name_1)

print(first_symbol, last_symbol, length_of_name)

"""
**12.** Створіть рядок "Would you tell me, please, which way I ought to go from here?" 
та отримайте з нього підстрічки:
- Перші 6 символів
- Останні 11 символів
"""
text = "Would you tell me, please, which way I ought to go from here?"
first_6_symbols = text[0:6]
last_11_symbols = text[-11:]
print(first_6_symbols, last_11_symbols)
"""
**13.** Створіть багаторядковий рядок (використовуючи потрійні лапки) зі своїм улюбленим віршем або цитатою.
"""

"""
**13.** 
Ніхто твоїх не заперечить прав.
Так, перший світ осяв твої висоти,
До тебе тислись войовничі готи,
І Данпарштадт із пущі виглядав.
Микола Зеров 1923
Київ — традиція
"""

"""
**14.** Поєднайте два рядки "Hello" та "World" у різні способи (з пробілом, з комою, з новим рядком).
"""
result_1 = "Hello" + " " + "World "
result_2 = "Hello" + "," + "World "
result_3 = "Hello" + "\n" + "World"
total_result = result_1 + result_2 + result_3
print(total_result)

"""
**15.** Створіть рядок з символами, які потребують екранування (лапки, зворотна коса риска).
"""
string = "Would you tell me, \"please\", which way I ought to go from here 2\\2"
print(string)

"""
**16.** Напишіть код, який запитує у користувача його ім'я та вік, 
а потім виводить привітання у форматі: "Привіт, [ім'я]! Тобі [вік] років."
"""
name_1 = input("Please, enter your name\n")
age_2 = input("Please, enter your age\n")
print(f"Привіт, {name_1}! Тобі {age_2} років.")

"""

**17.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_amount = 232
one_page_capacity = 8
required_number_of_pages = photo_amount//one_page_capacity
print("Необхідно", required_number_of_pages, "cторінок, щоб всі фотографії Ігоря вмістились в альбом.")

"""
**18.** Напишіть код який запитує у користувача 
його улюблений колір та число, а потім створює персоналізоване
повідомлення використовуючи f-string форматування.
"""
favourite_color = input("Please, share your favourite color\n")
favourite_number = input("Please, share your favourite number\n")
print(f"Ха,я тепер все про тебе знаю! Твій улюблений колір {favourite_color} та улюблене число {favourite_number }.")

"""
**19.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
silpo_products_amount = 375291
silpo_warehouses_amount = 3
first_and_second_warehouses_products_amount = 250449
third_and_second_warehouses_products_amount = 222950
third_warehouse_products_amount = silpo_products_amount - first_and_second_warehouses_products_amount
second_warehouse_products_amount = third_and_second_warehouses_products_amount - third_warehouse_products_amount
first_warehouses_products_amount = silpo_products_amount - third_and_second_warehouses_products_amount
print(f"На першому складі знаходиться {first_warehouses_products_amount} товарів, на другому складі"
      f" {second_warehouse_products_amount} товарів, на третьому складі {third_warehouse_products_amount} товарів.")

"""
**20.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_repayment_period = 18
credit_repayment_per_month = 1179
pc_cost = credit_repayment_period * credit_repayment_per_month
print("Вартість комп’ютера дорвінює", pc_cost, "грн.")
