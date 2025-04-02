SELECT COUNT(*) AS num_users_registered
FROM Users
WHERE user_country = 'FIN'
  AND user_registration_timestamp_utc >= NOW() - INTERVAL '30 days';
