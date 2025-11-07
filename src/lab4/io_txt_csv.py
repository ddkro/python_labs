def read_text(path, encoding="utf-8"):
    """
    Открывает файл на чтение с указанной кодировкой и возвращает его содержимое как одну строку.
    Можно задать кодировку, например: encoding="cp1251"
    """
    with open(path, "r", encoding=encoding) as f:
        return f.read()

def ensure_parent_dir(path):
    """
    Проверяет, есть ли родительская папка пути, и если нет — создаёт её.
    """
    import os
    parent = os.path.dirname(path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent)

def write_csv(rows, path, header=None):
    """
    Запускает запись CSV (разделитель: запятая) без модуля csv.
    Проверяет длину строк. Если есть header — пишет заголовок.
    """
    # Проверка длины строк
    if header is not None:
        n = len(header)
        for row in rows:
            if len(row) != n:
                raise ValueError("Длина строки не соответствует заголовку")
    elif len(rows) > 0:
        n = len(rows[0])
        for row in rows:
            if len(row) != n:
                raise ValueError("Строки разной длины")

    ensure_parent_dir(path)

    with open(path, "w", encoding="utf-8") as f:
        if header is not None:
            f.write(",".join(map(str, header)) + "\n")
        for row in rows:
            f.write(",".join(map(str, row)) + "\n")
