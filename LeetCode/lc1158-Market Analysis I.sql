-- https://leetcode.com/problems/market-analysis-i/

select
u.user_id as buyer_id,
u.join_date as join_date,
coalesce(count(o.order_id),0) as orders_in_2019

from users u left join orders o 
on u.user_id = o.buyer_id
and year(order_date) = 2019

group by user_id
order by user_id
------------------------------------------------------
select
u.user_id as buyer_id,
u.join_date,
coalesce(count(o.order_id),0) as orders_in_2019

from users u left join (select * from orders where year(order_date) = 2019) o
on u.user_id = o.buyer_id

group by user_id
order by user_id
