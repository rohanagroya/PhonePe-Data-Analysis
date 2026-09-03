USE phonepe;

-- 1. Successful vs Failed Payments Count
SELECT Payment_Status, COUNT(*) AS total
FROM transactions
GROUP BY Payment_Status;


-- 2. Top Reasons for Failed Payments
SELECT Reason, COUNT(*) AS total
FROM transactions
WHERE Payment_Status = 'Failed'
GROUP BY Reason
ORDER BY total DESC;


-- 3. Most Used Service by Total Amount
SELECT Service, SUM(Amount) AS total_amount
FROM transactions
GROUP BY Service
ORDER BY total_amount DESC;


-- 4. Failed Payments by Age Group
SELECT Age_Group, COUNT(*) AS failed_count
FROM transactions
WHERE Payment_Status = 'Failed'
GROUP BY Age_Group
ORDER BY failed_count DESC;


-- 5. Month-wise Total Transaction Amount
SELECT Month, SUM(Amount) AS total_amount
FROM transactions
GROUP BY Month
ORDER BY Month;