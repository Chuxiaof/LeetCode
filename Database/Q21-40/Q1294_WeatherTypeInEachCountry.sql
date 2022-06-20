# Write your MySQL query statement below
SELECT a.country_name,
CASE 
WHEN AVG(weather_state)<=15 THEN "Cold"
WHEN AVG(weather_State)>=25 THEN "Hot"
ELSE "Warm"
END
AS weather_type 
FROM Countries AS a
JOIN Weather AS b
ON a.country_id = b.country_id
WHERE MONTH(b.day) = 11
GROUP BY a.country_id