-- https://leetcode.com/problems/game-play-analysis-i/description/

select
player_id, min(event_date) as first_login 
from activity
group by 1
order by 1