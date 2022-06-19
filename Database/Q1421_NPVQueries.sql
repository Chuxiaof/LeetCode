# Write your MySQL query statement below
SELECT q.id, q.year, IFNULL(v.npv,0) AS npv
FROM Queries q
LEFT JOIN NPV v
ON q.id = v.id AND q.year = v.year