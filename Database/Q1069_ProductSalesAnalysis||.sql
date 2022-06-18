# Write your MySQL query statement below
SELECT
    product_id,
    SUM(quantity) total_quantity
FROM product JOIN sales
USING(product_id)
GROUP BY product_id