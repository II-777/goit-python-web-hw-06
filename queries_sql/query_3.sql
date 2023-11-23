SELECT groups.group_name, AVG(grades.grade) as avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 3
GROUP BY groups.group_name;
