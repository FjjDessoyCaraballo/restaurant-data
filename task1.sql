CREATE TABLE Users (
    user_id                         VARCHAR(255) NOT NULL PRIMARY KEY,
    user_country                    CHAR(3) NOT NULL,
    user_device_id                  VARCHAR(255) NOT NULL,
    user_registration_timestamp_utc TIMESTAMP NOT NULL,
    user_first_purchase_timestamp   TIMESTAMP
);

CREATE TABLE Purchases (
    purchase_id                     VARCHAR(255) NOT NULL PRIMARY KEY,
    user_id                         VARCHAR(255) NOT NULL,
    venue_id                        VARCHAR(255) NOT NULL,
    timestamp_utc                   TIMESTAMP NOT NULL,
    total_number_units              INT NOT NULL,
    value_eur                       DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Sales (
    purchase_id                     VARCHAR(255) NOT NULL,
    product_id                      VARCHAR(255) NOT NULL,
    price                           DECIMAL(10,2) NOT NULL,
    quantity                        INT NOT NULL,
    PRIMARY KEY (purchase_id, product_id),
    CONSTRAINT fk_purchase FOREIGN KEY (purchase_id) REFERENCES Purchases(purchase_id)
);

CREATE INDEX idx_user_country ON Users(user_country);