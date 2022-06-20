# Write your MySQL query statement below
SELECT DISTINCT b.title
FROM TVProgram a
JOIN Content b
ON a.content_id = b.content_id
WHERE b.Kids_content = 'Y' 
    AND (a.program_date BETWEEN '2020-06-01' AND '2020-06-30') 
    AND b.content_type = 'Movies'