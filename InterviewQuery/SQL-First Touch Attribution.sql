-- https://www.interviewquery.com/questions/first-touch-attribution

with rankedsessions as
(select us.user_id, channel,  
rank() over(partition by user_id order by created_at asc) as rnk,
sum(conversion) over(partition by user_id) >0 as converted
from 
attribution a join user_sessions us
on a.session_id = us.session_id
)

select channel , user_id
from rankedsessions
where rnk = 1 and converted = True
group by 1,2
order by 1,2