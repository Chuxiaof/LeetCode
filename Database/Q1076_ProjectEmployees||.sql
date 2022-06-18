# Write your MySQL query statement below
SELECT project_id
FROM project
GROUP BY project_id
HAVING COUNT(project_id) = (
    SELECT COUNT(project_id)
    FROM project
    GROUP BY project_id
    ORDER BY COUNT(project_id) DESC
    LIMIT 1)