-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/

select activity_date as day, count(distinct user_id) as active_users
from activity
group by 1
having datediff('2019-07-27', activity_date) < 30  and datediff('2019-07-27', activity_date) >=0