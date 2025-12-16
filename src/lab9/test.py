import sys
sys.path.append(r'C:\Users\User\Desktop\python_labs\src')

from lab8.models import Student
from lab9.group import Group

group = Group("data/lab09/group.csv")

# Добавляем студентов
s1 = Student("Иванов И.И.", "2003-05-15", "SE-01", 4.5)
s2 = Student("Петров П.П.", "2004-12-01", "SE-02", 3.8)
group.add(s1)
group.add(s2)

print("Все студенты:", [str(s) for s in group.list()])
print("Поиск 'иван':", [str(s) for s in group.find("иван")])
print("Удалено:", group.remove("Иванов И.И."))
group.update("Петров П.П.", gpa=4.2)
print("После обновления:", [str(s) for s in group.list()])
