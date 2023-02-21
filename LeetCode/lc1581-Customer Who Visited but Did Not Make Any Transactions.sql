-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions

select customer_id, count(visit_id) as count_no_trans 
from visits
where visit_id not in (select visit_id from transactions)
group by 1
order by 1



select customer_id, count(v.visit_id) as count_no_trans
from visits v left join transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by 1