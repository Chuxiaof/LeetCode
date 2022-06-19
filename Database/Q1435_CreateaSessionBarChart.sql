WITH cte(bin, min_duration, max_duration) AS (
    SELECT '[0-5>', 0, 5*60
    UNION ALL
    SELECT '[5-10>', 5*60, 10*60
    UNION ALL
    SELECT '[10-15>', 10*60, 15*60
    UNION ALL
    SELECT '15 or more', 15*60, 2147483647
)
SELECT cte.bin, COUNT(s.session_id) AS total
FROM Sessions s
RIGHT JOIN cte 
		ON s.duration >= min_duration 
        AND s.duration < max_duration				 
GROUP BY cte.bin;