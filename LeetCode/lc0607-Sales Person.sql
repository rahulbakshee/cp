-- https://leetcode.com/problems/sales-person/


select sp.name from 
salesperson sp where sales_id not in
(select o.sales_id
from company c right join orders o
on c.com_id = o.com_id
where c.name='RED')