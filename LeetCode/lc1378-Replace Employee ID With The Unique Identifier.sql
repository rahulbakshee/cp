-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/
# Write your MySQL query statement below
SELECT
    UNIQUE_ID,
    NAME
FROM
EMPLOYEES EMP 
LEFT JOIN 
EMPLOYEEUNI UNI
ON EMP.ID=UNI.ID
