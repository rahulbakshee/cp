-- interviewquery.com/questions/upsell-transactions

select count(distinct t1.user_id) as num_of_upsold_customers
from transactions t1 join transactions t2
using(user_id)
where t1.created_at <> t2.created_at
and t1.product_id <> t2.product_id
-- and t1.quantity <> 0
-- and t2.quantity <> 0
-- and t1.quantity + t2.quantity >= 2