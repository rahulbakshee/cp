-- https://leetcode.com/problems/duplicate-emails/

select email
from person
group by email
having count(*) > 1