import sqlite3
from faker import Faker

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 40

CREATE_DB_SQL = 'schema.sql'
DATABASE_NAME = 'university.db'

INSERT_GROUP_SQL = 'INSERT INTO groups (group_name) VALUES (?);'
INSERT_TEACHER_SQL = 'INSERT INTO teachers (fullname) VALUES (?);'
INSERT_SUBJECT_SQL = 'INSERT INTO subjects (name, teacher_id) VALUES (?, ?);'
INSERT_STUDENT_SQL = 'INSERT INTO students (fullname, group_id) VALUES (?, ?);'
INSERT_GRADE_SQL = 'INSERT INTO grades (subject_id, student_id, grade, grade_date) VALUES (?, ?, ?, ?);'

def create_db():
    with open(CREATE_DB_SQL, 'r') as f:
        sql = f.read()

    with sqlite3.connect(DATABASE_NAME) as con:
        c = con.cursor()
        c.executescript(sql)

def populate_data():
    fake = Faker()
    Faker.seed(0)

    groups = ['group1', 'group2', 'group3']
    teachers = [fake.first_name() + ' ' + fake.last_name() for _ in range(NUMBER_TEACHERS)]
    subjects = [
        "Algorithms",
        "Computer Networks",
        "Cybersecurity",
        "Python Programming Level II",
        "Relational Databases",
    ]

    with sqlite3.connect(DATABASE_NAME) as conn:
        c = conn.cursor()

        for group in groups:
            c.execute(INSERT_GROUP_SQL, (group,))

        for teacher in teachers:
            c.execute(INSERT_TEACHER_SQL, (teacher,))

        for subject in subjects:
            teacher_id = fake.random_int(min=1, max=NUMBER_TEACHERS)
            c.execute(INSERT_SUBJECT_SQL, (subject, teacher_id))

        students = [
            (fake.first_name() + ' ' + fake.last_name(), fake.random_int(min=1, max=len(groups)))
            for _ in range(NUMBER_STUDENTS)
        ]

        c.executemany(INSERT_STUDENT_SQL, students)

        for student_id in range(1, NUMBER_STUDENTS + 1):
            for subject_id in range(1, len(subjects) + 1):
                grade = fake.random_int(min=1, max=12)
                grade_date = fake.date_between(start_date='-1y', end_date='today')
                c.execute(INSERT_GRADE_SQL, (subject_id, student_id, grade, grade_date))

        conn.commit()

if __name__ == "__main__":
    create_db()
    populate_data()