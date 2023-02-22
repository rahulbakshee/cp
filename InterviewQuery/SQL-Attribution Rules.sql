-- https://www.interviewquery.com/questions/attribution-rules

with attributed as 
(select user_id, 
sum(case 
    when lower(channel) = 'google' or lower(channel) = 'facebook' 
    then 1 else 0 
end) as visited
from user_sessions us join attribution a
on us.session_id = a.session_id
group by 1
)

select  
case when visited > 0 then 'paid' else 'organic'
end as  attribute, user_id
from attributed
group by 1,2
order by 2
