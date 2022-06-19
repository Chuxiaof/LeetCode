# Write your MySQL query statement below
SELECT ad_id, IFNULL(ROUND(100*AVG(CASE WHEN action = 'Clicked' THEN 1
                 WHEN action = 'Viewed' THEN 0
                 ELSE NULL END),2),0) AS ctr
                                                         
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id