list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2  # Поровну дели всех участников на две команды

first_team = list_players[:middle_index]  # Первая половина игроков будет в первой команде
second_team = list_players[middle_index:]  # Вторая половина во второй команде

print(first_team)  # Прописываем имена первой команды
print(second_team)  # Прописываем имена второй команды
