-- https://leetcode.com/problems/customers-who-never-order


select c.name as Customers, c.id, o.id
from customers c left  join orders o
on c.id = o.customerid
where o.id is null


# ------------------------------------------------

select name as Customers
from customers
where id not in (select customerid from orders)
