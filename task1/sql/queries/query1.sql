-- [Task] Query 1
-- The last line is in SQLite3, which is less used for bigger databases, but here is used for debugging

SELECT COUNT(*) FROM Users WHERE User_country = 'FIN' 
  AND User_registration_timestamp_utc >= NOW() - INTERVAL '30 days';
  -- AND User_registration_timestamp_utc >= datetime('now', '-30 days') -- DEBUGGING

