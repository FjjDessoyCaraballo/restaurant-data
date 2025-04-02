-- [Task] Query 2

SELECT COUNT(DISTINCT p.User_id) AS num_active_multi_product_users
FROM Purchases p
JOIN Sales s ON p.Purchase_id = s.Purchase_id
WHERE p.Timestamp_utc >= NOW() - INTERVAL '30 days'
GROUP BY p.User_id
HAVING COUNT(DISTINCT s.Product_id) > 1;