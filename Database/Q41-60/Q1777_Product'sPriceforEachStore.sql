# Write your MySQL query statement below
SELECT product_id, 
       AVG(CASE WHEN store='store1' THEN price END) AS store1,
       AVG(CASE WHEN store='store2' THEN price END) AS store2,
       AVG(CASE WHEN store='store3' THEN price END) AS store3
FROM Products
GROUP BY product_id