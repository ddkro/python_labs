import csv
from pathlib import Path
from typing import List, Dict, Any
import sys
sys.path.append(r'C:\Users\User\Desktop\python_labs\src')
from lab8.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Создает файл с заголовком, если его нет."""
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")

    def _read_all(self) -> List[Dict[str, str]]:
        """Читает все строки из CSV в список словарей."""
        students = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Валидация заголовков
                if not all(h in reader.fieldnames for h in ['fio', 'birthdate', 'group', 'gpa']):
                    raise ValueError("CSV must have headers: fio,birthdate,group,gpa")
                
                for row in reader:
                    try:
                        # Валидация через Student
                        Student.from_dict(row)
                        students.append(row)
                    except (ValueError, KeyError, TypeError):
                        continue  # Пропускаем некорректные строки
        except FileNotFoundError:
            pass
        return students

    def list(self) -> List[Student]:
        """Возвращает всех студентов в виде списка Student."""
        rows = self._read_all()
        return [Student.from_dict(row) for row in rows]

    def add(self, student: Student) -> None:
        """Добавляет нового студента в CSV."""
        rows = self._read_all()
        rows.append(student.to_dict())
        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        """Находит студентов по подстроке в fio."""
        rows = self._read_all()
        return [Student.from_dict(r) for r in rows if substr.lower() in r["fio"].lower()]

    def remove(self, fio: str) -> int:
        """Удаляет запись(и) с данным fio. Возвращает количество удаленных."""
        rows = self._read_all()
        initial_count = len(rows)
        rows = [r for r in rows if r["fio"].lower() != fio.lower()]
        final_count = len(rows)
        self._write_all(rows)
        return initial_count - final_count

    def update(self, fio: str, **fields) -> bool:
        """Обновляет поля существующего студента. Возвращает True если обновлено."""
        rows = self._read_all()
        updated = False
        for row in rows:
            if row["fio"].lower() == fio.lower():
                # Валидация обновленных полей
                for key, value in fields.items():
                    if key in ['fio', 'birthdate', 'group', 'gpa']:
                        row[key] = str(value)
                        # Дополнительная валидация GPA если обновляется
                        if key == 'gpa':
                            try:
                                Student.from_dict(row)
                            except ValueError:
                                raise ValueError(f"Invalid gpa value: {value}")
                updated = True
        if updated:
            self._write_all(rows)
        return updated

    def _write_all(self, rows: List[Dict[str, Any]]) -> None:
        """Записывает все строки в CSV."""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
                writer.writerows(rows)
            else:
                f.write("fio,birthdate,group,gpa\n")
