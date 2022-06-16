# Write your MySQL query statement below
SELECT a.Name AS name, b.bonus AS bonus
FROM Employee a
    LEFT JOIN Bonus b
        ON a.empid = b.empid
    
WHERE b.bonus < 1000 OR b.bonus IS NULL