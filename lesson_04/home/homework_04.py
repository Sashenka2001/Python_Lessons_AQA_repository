adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
replaced_text_1 = adwentures_of_tom_sawer.replace("wealth.", " ")
print(replaced_text_1)

# task 02 ==
""" Замініть .... на пробіл
"""
replaced_text_2 = adwentures_of_tom_sawer.replace("....", " ")
print(replaced_text_2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
split_by_space = adwentures_of_tom_sawer.replace("  ", " ")
print(split_by_space)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_amount = adwentures_of_tom_sawer.count("h")
print(h_amount)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
title_words_count = 0
words_list = adwentures_of_tom_sawer.replace("\n", " ").split(" ")
for i in words_list:
    if i.istitle():
        title_words_count = title_words_count + 1
print(title_words_count)
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_position = adwentures_of_tom_sawer.replace("Tom", "Boo",1).find("Tom")
print(tom_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.rstrip(".").replace("....", "").split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i in adwentures_of_tom_sawer_sentences:
    if i.lstrip(" \n").startswith("By the time"):
        print(True)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
words_count = len(adwentures_of_tom_sawer_sentences[-1].split(" "))
print(adwentures_of_tom_sawer_sentences[-1])
print(words_count)