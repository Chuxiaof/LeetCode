# Write your MySQL query statement below
SELECT contest_id, 
ROUND(100 * COUNT(DISTINCT user_id)/(SELECT COUNT(*) FROM Users),2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY 2 DESC, contest_id
