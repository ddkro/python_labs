import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте плюс дополнительные ключи в алфавитном порядке.
    """
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    with json_path.open(encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list) or len(data) == 0 or not all(isinstance(d, dict) for d in data):
        raise ValueError("JSON должен быть непустым списком словарей")

    fieldnames = list(data[0].keys())  
    all_keys = set(fieldnames)
    for d in data[1:]:
        all_keys.update(d.keys())
    new_keys = sorted(all_keys.difference(fieldnames))
    fieldnames.extend(new_keys)

    with csv_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            row = {key: entry.get(key, '') for key in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    JSON сохраняется с ensure_ascii=False и отступами.
    """
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    with csv_path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV файл должен содержать заголовок")

        data = list(reader)

    if len(data) == 0:
        raise ValueError("CSV файл пустой")

    with json_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")