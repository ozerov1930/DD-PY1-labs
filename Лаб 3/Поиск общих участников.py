# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, delimiter=","): #  Находит общих участников среди двух групп.

    participants1 = set(group1.split(delimiter))  # Разбиваем строки участников на списки
    participants2 = set(group2.split(delimiter))  # Разбиваем строки участников на списки

    common_participants = participants1 & participants2  # Находим пересечение

    return sorted(common_participants)   # Возвращаем список общих участников и сортируем его

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
  # Проверяем функцию с другим разделителем
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")

print("Общие участники:", common)


# TODO Провеьте работу функции с разделителем отличным от запятой
