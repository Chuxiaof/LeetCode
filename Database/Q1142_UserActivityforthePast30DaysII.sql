# Write your MySQL query statement below
SELECT 
IFNULL(ROUND((COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id)),2),0.00)
AS average_sessions_per_user
FROM Activity
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'


# Write your MySQL query statement below
SELECT IFNULL(ROUND(AVG(c), 2),0.00)
AS average_sessions_per_user
FROM
(
    SELECT COUNT(DISTINCT session_id) as c
    FROM Activity
    WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27' 
    GROUP BY user_id
) A