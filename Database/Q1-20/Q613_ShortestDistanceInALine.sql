# Write your MySQL query statement below
SELECT
    ABS(p1.x - p2.x) AS shortest
FROM
    point p1
        JOIN
    point p2 
    ON p1.x != p2.x
ORDER BY shortest
LIMIT 1
;


# Write your MySQL query statement below
SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1
        JOIN
    point p2 
    ON p1.x != p2.x
;