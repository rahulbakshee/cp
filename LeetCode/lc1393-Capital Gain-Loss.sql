-- https://leetcode.com/problems/capital-gainloss/

select
stock_name,
sum(case 
    when operation='Buy' then -1*price
    else price
end) as capital_gain_loss 
from stocks
group by 1
order by 1 