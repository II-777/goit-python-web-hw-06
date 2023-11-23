SELECT students.fullname
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.group_name = 3;

