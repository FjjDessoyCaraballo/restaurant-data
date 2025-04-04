-- -- [Task] Query 1

SELECT COUNT(*) FROM Users WHERE User_country = 'FIN' 
  -- AND User_registration_timestamp_utc >= datetime('now', '-30 days')
  -- AND User_registration_timestamp_utc >= NOW() - INTERVAL '30 days';

