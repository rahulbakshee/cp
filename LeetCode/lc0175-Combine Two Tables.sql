-- https://leetcode.com/problems/combine-two-tables/

select firstname, lastname, city, state
from person p left join address a
on p.personid = a.personid