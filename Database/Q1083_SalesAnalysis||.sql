# Write your MySQL query statement below
SELECT buyer_id
FROM Sales JOIN Product
USING(product_id)
GROUP BY buyer_id
HAVING SUM(product_name = 'S8') > 0 and SUM(product_name = 'iPhone') = 0
    