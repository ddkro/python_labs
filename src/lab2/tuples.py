def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Аргумент должен быть кортежем из 3 элементов")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str) or not (isinstance(gpa, float) or isinstance(gpa, int)):
        raise TypeError("Неверный тип элементов записи")
    fio = fio.strip()
    group = group.strip()
    if not fio:
        raise ValueError("Пустое ФИО")
    if not group:
        raise ValueError("Пустая группа")
    names = fio.split()
    if len(names) < 2 or len(names) > 3:
        raise ValueError("ФИО должно состоять из 2 или 3 слов")
    surname = names[0].capitalize()
    initials = ""
    if len(names) == 2:
        initials = f"{names[1][0].upper()}."
    else:
        initials = f"{names[1][0].upper()}.{names[2][0].upper()}."
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))

print(format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))
