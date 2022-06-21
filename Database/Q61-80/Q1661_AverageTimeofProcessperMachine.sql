# Write your MySQL query statement below
SELECT DISTINCT A1.machine_id, 
ROUND(AVG(ABS(A1.timestamp - A2.timestamp)),3) AS processing_time
FROM Activity A1
JOIN Activity A2
ON A1.machine_id = A2.machine_id 
AND A1.process_id = A2.process_id 
AND A1.activity_type != A2.activity_type
GROUP BY A1.machine_id