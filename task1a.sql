SELECT COUNT(*) AS num_users_registered
FROM Users
WHERE User_country = 'FIN'
  AND User_registration_timestamp_utc >= NOW() - INTERVAL '30 days';
