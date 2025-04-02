-- [Task] Query 3a

SELECT product_id, price
FROM (
    SELECT s.Product_id, s.Price,
           ROW_NUMBER() OVER (PARTITION BY s.Product_id ORDER BY p.Timestamp_utc DESC) AS rn
    FROM Sales s
    JOIN Purchases p ON s.Purchase_id = p.Purchase_id
) sub
WHERE rn = 1;


