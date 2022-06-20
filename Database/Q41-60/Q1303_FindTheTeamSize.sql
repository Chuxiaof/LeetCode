# Write your MySQL query statement below
SELECT employee_id, 
(SELECT COUNT(employee_id) 
    FROM Employee e1
    WHERE e1.team_id = e2.team_id
) team_size
FROM Employee e2