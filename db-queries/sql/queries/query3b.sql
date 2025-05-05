-- [Task] Query 3b

SELECT p.Product_id, p.Price
FROM Purchases p
JOIN Sales s ON p.Purchase_id = s.Purchase_id
INNER JOIN (
    SELECT p2.Product_id, MAX(s2.Timestamp_utc) AS latest_time
    FROM Purchases p2
    JOIN Sales s2 ON p2.Purchase_id = s2.Purchase_id
    GROUP BY p2.Product_id
) latest ON p.Product_id = latest.Product_id AND s.Timestamp_utc = latest.latest_time
GROUP BY p.Product_id;