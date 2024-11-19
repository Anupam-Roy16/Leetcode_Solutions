# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,  -- Extract the year and month from the transaction date
    country,                                   -- Group by country
    COUNT(*) AS trans_count,            -- Total number of transactions
    SUM(amount) AS trans_total_amount,               -- Total amount for all transactions
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,  -- Count of approved transactions
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount    -- Total amount for approved transactions
FROM Transactions
GROUP BY month, country;                       -- Group by month and country
