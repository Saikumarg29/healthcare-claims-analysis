
-- SQL to create claims table
CREATE TABLE claims (
    ClaimID INT,
    PatientID VARCHAR(10),
    Provider VARCHAR(50),
    ClaimType VARCHAR(20),
    ClaimAmount DECIMAL(10,2),
    ClaimDate DATE
);

-- Query to find average claim amount by type
SELECT ClaimType, AVG(ClaimAmount) as AvgAmount
FROM claims
GROUP BY ClaimType;
