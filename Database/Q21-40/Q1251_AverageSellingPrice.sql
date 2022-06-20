# Write your MySQL query statement below
SELECT product_id, ROUND(SUM(S.units*P.price) / SUM(S.units),2) AS average_price
FROM UnitsSold S JOIN Prices P
USING(product_id)
WHERE S.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY product_id
