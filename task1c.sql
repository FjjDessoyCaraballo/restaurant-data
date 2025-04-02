SELECT product_id, price
FROM (
    SELECT s.product_id, s.price,
           ROW_NUMBER() OVER (PARTITION BY s.product_id ORDER BY p.timestamp_utc DESC) AS rn
    FROM Sales s
    JOIN Purchases p ON s.purchase_id = p.purchase_id
) sub
WHERE rn = 1;
