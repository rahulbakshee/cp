-- https://leetcode.com/problems/sales-analysis-iii

select p.product_id, p.product_name
from 
product p join sales s
on p.product_id  = s.product_id 
group by 1,2
having  min(sale_date) >= date('2019-01-01') and max(sale_date) <= date('2019-03-31')