-- https://leetcode.com/problems/find-followers-count/

select user_id , 
count(follower_id) as followers_count
from followers
group by 1
order by 1 asc