# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
set_from_list = set(small_list)
print(set_from_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average_sum = sum(small_list) / len(small_list)
print(average_sum)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
set_from_list = set(big_list)
if len(big_list) != len(set_from_list):
    print("В списку big_list наявні дублікати")

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_value = sorted(list(add_dict.values()), reverse=True)[0]
print(max_value)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
new_dict = dict(zip(base_dict.values(), base_dict.keys()))
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict | add_dict
print(sum_dict)
print(set(base_dict.keys()), set(add_dict.keys()))
logical_intersection = set(base_dict.keys()) & set(add_dict.keys())
print(logical_intersection)
for i in logical_intersection:
    sum_dict[i] = str(base_dict[i]) + str(add_dict[i])
    print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_elements = sum(set_1 ^ set_2)
print(sum_elements)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
set_one = {1, 2, 3, 4, 5}
set_two = {4, 6, 5, 10}
my_set = set_one ^ set_two
print(my_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

my_dict = dict(person_list)
new_dict_2 = dict(zip(my_dict.values(), my_dict.keys()))
print(new_dict_2)
