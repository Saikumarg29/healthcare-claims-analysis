-- Create claims table
CREATE TABLE claims (
    ClaimID INT,
    PatientID VARCHAR(10),
    Provider VARCHAR(50),
    ClaimType VARCHAR(20),
    ClaimAmount DECIMAL(10,2),
    ClaimDate DATE
);

-- Average claim by type
SELECT ClaimType, AVG(ClaimAmount) as AvgAmount
FROM claims
GROUP BY ClaimType;

-- Monthly claim cost trend
SELECT DATE_TRUNC('month', ClaimDate) as Month, SUM(ClaimAmount) as MonthlyTotal
FROM claims
GROUP BY Month
ORDER BY Month;
