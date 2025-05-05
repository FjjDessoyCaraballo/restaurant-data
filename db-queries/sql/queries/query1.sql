-- [Task] Query 1
-- This syntax is supported by SQLite3. For postgres and mysql one might change 
-- datetime to "NOW() - INTERVAL '30 days'"

SELECT COUNT(*) FROM Users WHERE User_country = 'FIN' 
  AND User_registration_timestamp_utc >= datetime('now', '-30 days')

