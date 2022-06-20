# Write your MySQL query statement below
SELECT a.project_id, ROUND(AVG(b.experience_years), 2) AS average_years
FROM Project a JOIN Employee b
USING(employee_id)
GROUP BY a.project_id
