import sqlite3
import random
from datetime import datetime, timedelta
import uuid

# Create a connection to the database
conn = sqlite3.connect('wolt_mock.db')
cursor = conn.cursor()

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    User_id TEXT PRIMARY KEY,
    User_country TEXT,
    User_device_id TEXT,
    User_registration_timestamp_utc TEXT,
    User_first_purchase_timestamp_utc TEXT
)
''')

# Create Sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    Purchase_id TEXT PRIMARY KEY,
    User_id TEXT,
    Venue_id TEXT,
    Timestamp_utc TEXT,
    Total_number_units INTEGER,
    Value_eur REAL,
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
)
''')

# Create Purchases table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Purchases (
    Purchase_id TEXT,
    Product_id TEXT,
    Price REAL,
    Quantity INTEGER,
    PRIMARY KEY (Purchase_id, Product_id),
    FOREIGN KEY (Purchase_id) REFERENCES Sales(Purchase_id)
)
''')

# Sample data generation
countries = ['Finland', 'Sweden', 'Denmark', 'Germany', 'Estonia', 'Poland', 'Italy', 'Spain']
venues = [f'venue_{i}' for i in range(1, 21)]  # 20 venues
products = [f'product_{i}' for i in range(1, 101)]  # 100 products

# Generate random datetime between two dates
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Generate 500 users
users = []
for i in range(500):
    user_id = str(uuid.uuid4())
    country = random.choice(countries)
    device_id = str(uuid.uuid4())
    
    # Registration date between 2020-01-01 and 2024-12-31
    reg_date = random_date(datetime(2020, 1, 1), datetime(2024, 12, 31))
    reg_date_str = reg_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # 80% of users have made a purchase
    if random.random() < 0.8:
        # First purchase date after registration date but within 90 days
        max_purchase_date = min(reg_date + timedelta(days=90), datetime(2025, 4, 1))
        first_purchase_date = random_date(reg_date, max_purchase_date)
        first_purchase_date_str = first_purchase_date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        first_purchase_date_str = None
    
    users.append((user_id, country, device_id, reg_date_str, first_purchase_date_str))
    
# Insert users
cursor.executemany('INSERT INTO Users VALUES (?, ?, ?, ?, ?)', users)

# Generate 1000 sales
sales = []
# Keep track of users who have made purchases
users_with_purchases = [user[0] for user in users if user[4] is not None]

for i in range(1000):
    purchase_id = str(uuid.uuid4())
    user_id = random.choice(users_with_purchases)
    venue_id = random.choice(venues)
    
    # Find user's first purchase date
    cursor.execute('SELECT User_first_purchase_timestamp_utc FROM Users WHERE User_id = ?', (user_id,))
    first_purchase_date_str = cursor.fetchone()[0]
    first_purchase_date = datetime.strptime(first_purchase_date_str, '%Y-%m-%d %H:%M:%S')
    
    # Purchase date after first purchase date
    timestamp = random_date(first_purchase_date, datetime(2025, 4, 1))
    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    # Random number of units between 1 and 10
    total_units = random.randint(1, 10)
    
    # Random value between 5 and 200 euros
    value_eur = round(random.uniform(5, 200), 2)
    
    sales.append((purchase_id, user_id, venue_id, timestamp_str, total_units, value_eur))

# Insert sales
cursor.executemany('INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?)', sales)

# Generate purchase details
purchases = []
for sale in sales:
    purchase_id = sale[0]
    num_products = random.randint(1, 5)  # Number of different products in this purchase
    
    # Ensure total quantity matches total_number_units in Sales
    total_units = sale[4]
    remaining_units = total_units
    
    selected_products = random.sample(products, num_products)
    
    for i, product_id in enumerate(selected_products):
        if i == num_products - 1:  # Last product
            quantity = remaining_units
        else:
            max_quantity = remaining_units - (num_products - i - 1)
            if max_quantity <= 0:
                continue
            quantity = random.randint(1, max_quantity)
            remaining_units -= quantity
        
        # Random price between 3 and 50 euros
        price = round(random.uniform(3, 50), 2)
        
        purchases.append((purchase_id, product_id, price, quantity))

# Insert purchases
cursor.executemany('INSERT INTO Purchases VALUES (?, ?, ?, ?)', purchases)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database 'wolt_mock.db' has been created successfully with sample data!")