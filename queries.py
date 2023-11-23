import sqlite3
import random
from main import NUMBER_STUDENTS, NUMBER_TEACHERS

DATABASE_NAME = 'university.db'

def execute_query(query, params=None):
    with sqlite3.connect(DATABASE_NAME) as conn:
        c = conn.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        result = c.fetchall()
        return result

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
query_1 = """
    SELECT students.id, students.fullname, AVG(grades.grade) as avg_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id, students.fullname
    ORDER BY avg_grade DESC
    LIMIT 5;
"""

result_1 = execute_query(query_1)
print("Query 1 Result:", result_1)
print("#" + '-' * 48)

# Знайти студента із найвищим середнім балом з певного предмета.
subject_id = 1
query_2 = """
    SELECT students.id, students.fullname, AVG(grades.grade) as avg_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    WHERE grades.subject_id = ?
    GROUP BY students.id, students.fullname
    ORDER BY avg_grade DESC
    LIMIT 1;
"""

result_2 = execute_query(query_2, (subject_id,))
print("Query 2 Result:", result_2)
print("#" + '-' * 48)

# Знайти середній бал у групах з певного предмета.
subject_id = 1
query_3 = """
    SELECT groups.group_name, AVG(grades.grade) as avg_grade
    FROM groups
    JOIN students ON groups.id = students.group_id
    JOIN grades ON students.id = grades.student_id
    WHERE grades.subject_id = ?
    GROUP BY groups.group_name;
"""

result_3 = execute_query(query_3, (subject_id,))
print("Query 3 Result:", result_3)
print("#" + '-' * 48)

# Знайти середній бал на потоці (по всій таблиці оцінок).
query_4 = """
    SELECT AVG(grade) as avg_grade
    FROM grades;
"""

result_4 = execute_query(query_4)
print("Query 4 Result:", result_4)
print("#" + '-' * 48)

# Знайти які курси читає певний викладач.
teacher_id = random.randint(1, NUMBER_TEACHERS)
query_5 = """
    SELECT subjects.name
    FROM subjects
    WHERE subjects.teacher_id = ?;
"""

result_5 = execute_query(query_5, (teacher_id,))
print("Query 5 Result:", result_5)
print("#" + '-' * 48)

# Знайти список студентів у певній групі.
group_name = 'group1'
query_6 = """
    SELECT students.fullname
    FROM students
    JOIN groups ON students.group_id = groups.id
    WHERE groups.group_name = ?;
"""

result_6 = execute_query(query_6, (group_name,))
print("Query 6 Result:", result_6)
print("#" + '-' * 48)

# Знайти оцінки студентів у окремій групі з певного предмета.
group_name = 'group1'
subject_id = 1
query_7 = """
    SELECT students.fullname, grades.grade
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    WHERE groups.group_name = ? AND grades.subject_id = ?;
"""

result_7 = execute_query(query_7, (group_name, subject_id))
print("Query 7 Result:", result_7)
print("#" + '-' * 48)

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
teacher_id = 3
query_8 = """
    SELECT AVG(grades.grade) as avg_grade
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.teacher_id = ?;
"""

result_8 = execute_query(query_8, (teacher_id,))
print("Query 8 Result:", result_8)
print("#" + '-' * 48)

# Знайти список курсів, які відвідує студент.
student_id = 1
query_9 = """
    SELECT subjects.name
    FROM subjects
    JOIN grades ON subjects.id = grades.subject_id
    WHERE grades.student_id = ?;
"""

result_9 = execute_query(query_9, (student_id,))
print("Query 9 Result:", result_9)
print("#" + '-' * 48)

# Список курсів, які певному студенту читає певний викладач.
student_id = random.randint(1, NUMBER_STUDENTS)
teacher_id = random.randint(1, NUMBER_TEACHERS)
query_10 = """
    SELECT subjects.name
    FROM subjects
    JOIN grades ON subjects.id = grades.subject_id
    WHERE grades.student_id = ? AND subjects.teacher_id = ?;
"""

result_10 = execute_query(query_10, (student_id, teacher_id))
print("Query 10 Result:", result_10)
print("#" + '-' * 48)

if __name__ == '__main__':
    pass