-- https://leetcode.com/problems/bank-account-summary-ii

select name,
coalesce(sum(amount), 0) as balance    
from users u left join transactions t
using(account)
group by account
having balance > 10000
order by name
