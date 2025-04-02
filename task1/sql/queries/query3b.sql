-- [Task] Query 3b

SELECT s.Product_id, s.Price
FROM Sales s
JOIN Purchases p ON s.Purchase_id = p.Purchase_id
JOIN (
    SELECT s.Product_id, MAX(p.Timestamp_utc) AS latest_timestamp
    FROM Sales s
    JOIN Purchases p ON s.Purchase_id = p.Purchase_id
    GROUP BY s.Product_id
) latest ON s.Product_id = latest.Product_id
         AND p.Timestamp_utc = latest.latest_timestamp;