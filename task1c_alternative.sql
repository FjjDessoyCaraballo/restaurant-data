SELECT s.product_id, s.price
FROM Sales s
JOIN Purchases p ON s.purchase_id = p.purchase_id
JOIN (
    SELECT s.product_id, MAX(p.timestamp_utc) AS latest_timestamp
    FROM Sales s
    JOIN Purchases p ON s.purchase_id = p.purchase_id
    GROUP BY s.product_id
) latest ON s.product_id = latest.product_id
         AND p.timestamp_utc = latest.latest_timestamp;
