CREATE TABLE Users (
	User_id 						VARCHAR(255) NOT NULL PRIMARY KEY,
	User_country 					Char(3) NOT NULL,
	User_device_id 					VARCHAR(255) NOT NULL,
	User_registration_timestamp_utc	TIMESTAMP NOT NULL,
	User_first_purchase_timestamp	TIMESTAMP,
);

CREATE TABLE Sales (
	Purchase_id 					VARCHAR(255) NOT NULL PRIMARY KEY,
	User_id 						VARCHAR(255) NOT NULL,
	Venue_id						VARCHAR(255) NOT NULL,
	Timestamp_utc 					TIMESTAMP NOT NULL,
	Total_number_units 				INT NOT NULL,
	Value_eur						DECIMAL(10,2) NOT  NULL,
	CONSTRAINT fk_purchase FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

CREATE TABLE Purchases (
	Purchase_id						VARCHAR(255) NOT NULL,
	Product_id						VARCHAR(255) NOT NULL,
	Price  	 						DECIMAL(10,2),
	Quantity						INT NOT NULL,
	PRIMARY KEY (Purchase_id, Product_id),
	CONSTRAINT fk_purchase FOREIGN KEY (Purchase_id) REFERENCES Sales(Purchase_id)
);

