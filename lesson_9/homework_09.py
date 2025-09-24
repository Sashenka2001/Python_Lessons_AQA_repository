### Робота з файлами та папками — завдання
from pathlib import Path
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here
with open('hello.txt', 'w') as f:
    f.write('Hello, Python!')
"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with open('hello.txt', 'a') as f:
    f.write('\nLearning file operations')

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content)
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
print(len(content))

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
new_directory = Path("./data")
# Створюємо нову директорію
if not new_directory.is_dir():
    new_directory.mkdir()

with open('data/notes.txt', 'w') as f:
    f.write('My first note.')
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
files = [f for f in new_directory.iterdir() if f.is_file()]

# Виведення списку всіх файлів
for file in files:
    print(file.name)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
with open('data/notes.txt', 'r') as f:
    content = f.read()
with open('data/copy.txt', 'w') as f:
    f.write(content)

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
with open('data/a.txt', 'w') as f:
    f.write('Hello,')
with open('data/a.txt', 'r') as f:
    content_a = f.read()
with open('data/b.txt', 'w') as f:
    f.write('My name is Sasha')
with open('data/b.txt', 'r') as f:
    content_b = f.read()
with open('data/ab.txt', 'w') as f:
    f.write(content_a + content_b)


"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
if not content.find("note") == -1:
    print("Знайдено")
else:
    print("Не знайдено")

