# Write your MySQL query statement below
SELECT class 
FROM Courses
GROUP BY Class
HAVING COUNT(Class) >=5

# WHERE Clause can be used without GROUP BY Clause	
# HAVING Clause cannot be used without GROUP BY Clause