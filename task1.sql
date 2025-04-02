-- Table creation

CREATE TABLE Users (
    User_id                         VARCHAR(255) NOT NULL PRIMARY KEY,
    User_country                    CHAR(3) NOT NULL,
    User_device_id                  VARCHAR(255) NOT NULL,
    User_registration_timestamp_utc TIMESTAMP NOT NULL,
    User_first_purchase_timestamp   TIMESTAMP
);

CREATE TABLE Purchases (
    Purchase_id                     VARCHAR(255) NOT NULL PRIMARY KEY,
    User_id                         VARCHAR(255) NOT NULL,
    Venue_id                        VARCHAR(255) NOT NULL,
    Timestamp_utc                   TIMESTAMP NOT NULL,
    Total_number_units              INT NOT NULL,
    Value_eur                       DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- choose between VARCHAR and INT

CREATE TABLE Sales (
    Purchase_id                     VARCHAR(255) NOT NULL,
    Product_id                      VARCHAR(255) NOT NULL,
    Price                           DECIMAL(10,2) NOT NULL,
    Quantity                        INT NOT NULL,
    PRIMARY KEY (Purchase_id, Product_id),
    CONSTRAINT fk_purchase FOREIGN KEY (Purchase_id) REFERENCES Purchases(Purchase_id)
);

CREATE INDEX idx_user_country ON Users(User_country);

-- [Task] Query 1

SELECT COUNT(*) AS num_users_registered
FROM Users
WHERE User_country = 'FIN'
  AND User_registration_timestamp_utc >= NOW() - INTERVAL '30 days';

-- [Task] Query 2

SELECT COUNT(DISTINCT p.User_id) AS num_active_multi_product_users
FROM Purchases p
JOIN Sales s ON p.Purchase_id = s.Purchase_id
WHERE p.Timestamp_utc >= NOW() - INTERVAL '30 days'
GROUP BY p.User_id
HAVING COUNT(DISTINCT s.Product_id) > 1;

-- [Task] Query 3a

SELECT product_id, price
FROM (
    SELECT s.Product_id, s.Price,
           ROW_NUMBER() OVER (PARTITION BY s.Product_id ORDER BY p.Timestamp_utc DESC) AS rn
    FROM Sales s
    JOIN Purchases p ON s.Purchase_id = p.Purchase_id
) sub
WHERE rn = 1;

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
