# Write your MySQL query statement below
SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Product p ON p.product_id = o.product_id
GROUP BY customer_id
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', o.quantity, 0) * p.price) >= 100 
AND SUM(IF(LEFT(order_date, 7) = '2020-07', o.quantity, 0) * p.price) >= 100 