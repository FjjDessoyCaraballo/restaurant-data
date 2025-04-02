SELECT COUNT(DISTINCT p.user_id) AS num_active_multi_product_users
FROM Purchases p
JOIN Sales s ON p.purchase_id = s.purchase_id
WHERE p.timestamp_utc >= NOW() - INTERVAL '30 days'
GROUP BY p.user_id
HAVING COUNT(DISTINCT s.product_id) > 1;
