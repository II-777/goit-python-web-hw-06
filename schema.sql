-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE [groups] (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  group_name STRING UNIQUE
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  fullname STRING 
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  fullname STRING ,
  group_id REFERENCES [groups] (id)
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  
  name STRING,
  teacher_id REFERENCES teachers (id)
 );

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  subject_id REFERENCES subjects (id),
  student_id REFERENCES students (id),
  grade INTEGER,
  grade_date DATE
  );
