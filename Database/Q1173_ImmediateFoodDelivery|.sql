# Write your MySQL query statement below
SELECT ROUND(100 * imediate / total, 2) AS immediate_percentage
FROM
(
    SELECT COUNT(*) AS imediate
    FROM Delivery
    WHERE order_date = customer_pref_delivery_date
) AS A, 
(
    SELECT COUNT(*) AS total
    FROM Delivery
) AS B
;


# Write your MySQL query statement below
SELECT ROUND(100 * AVG(order_date = customer_pref_delivery_date), 2) 
AS immediate_percentage
FROM Delivery





