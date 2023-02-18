-- https://leetcode.com/problems/fix-names-in-a-table/

select user_id, 
concat(upper(substr(name, 1 , 1)), lower(substr(name, 2, length(name))))  as name 
from users
order by user_id asc