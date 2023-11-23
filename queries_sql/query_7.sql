SELECT students.fullname, grades.grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
WHERE groups.group_name = ? AND grades.subject_id = 3;
