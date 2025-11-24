"""
strings-AND_LISTS
"""

# str = "text123/!"
# list = ["text", str, 1234]
# print(id(list))
# list[2] = 5678
# print(id(list))
# list2 = list[:]
# print(f"копия{id(list2)}")
# list2[0] = "new text in list2"
# print(list)
# print(list2)
#
# # Операции со списками
list3 = list + list2
# #Объединение списков
# print(f"третий список {list3}")
# # Умножение списков
# print(list3 * 3)
# # Проверка вхождения
# print("text" in list3)
# # Вложенные списки
# included_list = [[1, 2, 3, 4]], ["текст1", "текст2"]
# for i in included_list:
#     for subject in i:
#         print(subject)

"""
Методы списков
"""
# Добавление списка
# my_list = [1, 2]
# my_list.append("Мы учим Python")
# print(my_list)
# # Расширение списка
# my_list.extend([1, 2, 3, 4])
# print(my_list)
# # Вставка по индексу
# my_list.insert(0, "Сегодня")
# print(my_list)
# # Удаление объекта
# my_list.remove(1)
# print(my_list)
# # Удаление по индексу
# my_list.pop(0)
# print(my_list)
# # Очистка списка
# my_list.clear()
# print(my_list)
# # Подчёт вхождений элемента в списке
# val = my_list.count(1)
# print(val)
# # Сортировка списка
# my_list1 = [1, 5, 6, 7, 455, 323, 11, 146]
# my_list1.sort(reverse=False)
# print(my_list1)
# # Перевернуть список
# my_list1.reverse()
# print(my_list1)
#
# counter = 0
# while counter < len(my_list1):
#     val = my_list1[counter]
#     if val == 323:
#         print("Мы нашли число 323")
#         break
#     print(my_list1[counter])
#     counter += 1