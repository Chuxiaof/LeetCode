# Write your MySQL query statement below
SELECT a.name
FROM SalesPerson a
WHERE
    a.sales_id NOT IN (
    SELECT c.sales_id
        FROM Orders c
        LEFT JOIN Company b
        ON b.com_id = c.com_id

        WHERE b.name = 'RED')
;
