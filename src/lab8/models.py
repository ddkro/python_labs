from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация формата даты YYYY-MM-DD
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"birthdate must be in YYYY-MM-DD format, got '{self.birthdate}'")
        
        # Валидация GPA 0 ≤ gpa ≤ 5
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa must be between 0 and 5, got {self.gpa}")

    def age(self) -> int:
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth.year
        # Вычитаем год, если день рождения еще не наступил в этом году
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        # Создаем экземпляр и передаем валидацию через __post_init__
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"])
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f} (возраст: {self.age()})"

# Пример использования
s = Student("Иванов И.И.", "2003-05-15", "SE-01", 4.5)
print(s)  # Иванов И.И., SE-01, GPA: 4.50 (возраст: 22)
print(s.age())  # 22
print(s.to_dict())

# Десериализация
data = {"fio": "Петров П.П.", "birthdate": "2004-12-01", "group": "SE-02", "gpa": 3.8}
s2 = Student.from_dict(data)
print(s2)
