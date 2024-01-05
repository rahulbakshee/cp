-- https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50

-- Write your MySQL query statement below
SELECT
    p.product_name,
    s.year,
    s.price
from 
    sales s
left join
    product p
using (product_id)
