-- [Task] Query 2
-- Syntax fit for: SQLite3

SELECT COUNT(*) AS num_active_multi_product_users
FROM (
    SELECT s.User_id
    FROM Sales s
    JOIN Purchases p ON s.Purchase_id = p.Purchase_id -- inner join between sales and purchases
    WHERE s.Timestamp_utc >= datetime('now', '-30 days') -- time frame
    GROUP BY s.User_id
    HAVING COUNT(DISTINCT p.Product_id) > 1 -- at least one purchase in the last 30 days
);
