-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT teacher_id, COUNT(*) AS grade_a_count
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id
ORDER BY COUNT(*) DESC
LIMIT 1;
