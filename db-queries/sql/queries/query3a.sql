-- [Task] Query 3a

WITH RankedPurchases AS (
    SELECT 
    p.Product_id,
    p.Price,
    s.Timestamp_utc,
    ROW_NUMBER() OVER (PARTITION BY p.Product_id ORDER BY s.Timestamp_utc DESC) as row_num
    FROM Purchases p
    JOIN Sales s ON p.Purchase_id = s.Purchase_id
)
SELECT 
    Product_id,
    Price as most_recent_price,
    Timestamp_utc as price_timestamp
FROM RankedPurchases
WHERE row_num = 1
ORDER BY Product_id;
