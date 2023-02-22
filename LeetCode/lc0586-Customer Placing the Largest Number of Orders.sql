-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders


select customer_number
from orders
group by 1
order by count(order_number)  desc
limit 1