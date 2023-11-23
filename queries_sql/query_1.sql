SELECT students.id, students.fullname, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.fullname
ORDER BY avg_grade DESC
LIMIT 5;