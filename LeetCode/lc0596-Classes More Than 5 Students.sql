-- https://leetcode.com/problems/classes-more-than-5-students/description/

select class
from courses
group by 1
having count(*) >= 5