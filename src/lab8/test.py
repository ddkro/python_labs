from models import Student
from serialize import students_from_json, students_to_json

student1 = Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.7)
student2 = Student("Петрова Анна Сергеевна", "2001-08-22", "AI-02", 3.8)

student_data = {
    "fio": "Петрова Анна Сергеевна",
    "birthdate": "2001-08-22",
    "group": "AI-02",
    "gpa": 4.2,
}
print(student1)
print(f"Возраст: {student1.age()} лет")
print(f"Данные в виде словаря: {student1.to_dict()}")
print(Student.from_dict(student_data))

students = students_from_json("data/lab08/students_input.json")
students_to_json(students, "data/lab08/students_output.json")
