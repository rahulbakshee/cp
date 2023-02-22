-- https://www.interviewquery.com/questions/comments-histogram

with usercomments as (
select u.id, 
sum(case when user_id is null then 0 else 1 end) as comment_count
from 
users u 
left join 
    (select user_id, created_at 
    from comments
    where created_at between '2020-01-01' and '2020-01-31') c
on u.id=c.user_id
group by 1
)
select comment_count, count(*) as frequency
from usercomments
group by 1
order by 1 asc


