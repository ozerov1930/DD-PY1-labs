# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"  # Название входного файла csv
OUTPUT_FILENAME = "output.json"  # Назввание получаемого файла json


def task() -> None:  # Конвертация содержимого csv в json
    with open(INPUT_FILENAME) as f:  # TODO считать содержимое csv файла
        l = [line for line in csv.DictReader(f)]  # Преобразование строк в список

    with open(OUTPUT_FILENAME, "w") as f:  # Открытие файла и сохранение для удобного чтения
        json.dump(l, f, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:  # открываю созданный json файл и вывожу его содержимое построчно
        for line in output_f:
            print(line, end="")