# TODO решите задачу
import json

def task() -> float:
    INPUT_FILENAME = "input.json"  # Убедитесь, что имя файла совпадает с вашим

    # Чтение содержимого JSON файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Вычисление суммы произведений "score" и "weight"
    total = sum(item["score"] * item["weight"] for item in data)

    # Возврат значения, округленного до 3 знаков
    return round(total, 3)

# Печать результата
print(task())
