-- https://www.interviewquery.com/questions/empty-neighborhoods

select n.name
from neighborhoods n left join users u
on n.id = u.neighborhood_id
group by 1
having count(u.id) = 0