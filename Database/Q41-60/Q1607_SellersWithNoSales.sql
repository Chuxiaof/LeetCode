# Write your MySQL query statement below
SELECT s.seller_name
FROM Seller s
LEFT JOIN Orders o
ON s.seller_id = o.seller_id AND YEAR(sale_date) = '2020'
GROUP BY s.seller_id
HAVING COUNT(customer_id) = 0
ORDER BY s.seller_name