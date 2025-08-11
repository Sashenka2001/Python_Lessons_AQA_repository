# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02  == Виправте назви змінних, щоб текст виводався
hello = "Hello"
world = "world"
print(f"{hello} {world}!")
# ???????

# task 03 == Зробіть так, щоб кількість бананів була
# завжди на чотири штуки більша, ніж яблук
apples = 2
banana = apples + 4


# task 04 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 05 == Порахуйте периметр фігури з task 04
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(perimeter)


"""
    # Задачі 06 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 06
"""
У Оксани було 20 марок із серії «Мистецтво» 
і 7 марок із серії «Звірі».
5 марок із серії «Мистецтво» та
1 марку із серії «Звірі» вона подарувала подружці. 
Скільки марок лишилось у Оксани?
"""
postage_stamp_art_amount = 20
postage_stamp_animals_amount = 7
result = (postage_stamp_art_amount - 5) + (postage_stamp_animals_amount - 1)
print(result)
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
trees_amount = apple_trees + pear_trees + plum_trees
print(trees_amount)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
before_lunch_temperature = 5
after_lunch_temperature = before_lunch_temperature - 10
evening_temperature = after_lunch_temperature + 4
print(evening_temperature)
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_amount = 24
girls_amount = 24/2
boys_today_amount = boys_amount - 1
girls_today_amount = girls_amount - 2
total_children_amount_today = girls_today_amount + boys_today_amount
print(total_children_amount_today)
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1_price = 8
book_2_price = book_1_price + 2
book_3_price = (book_1_price + book_2_price)/2
total_books_price = book_3_price + book_2_price + book_1_price
print(total_books_price)


















