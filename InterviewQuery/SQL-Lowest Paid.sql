-- https://www.interviewquery.com/questions/lowest-paid


with projemp as 
(
-- emp completed at least 2 projects
select ep.employee_id, count(project_id) as completed_projects
from employee_projects ep 
join projects p
on ep.project_id = p.id
where end_date is not null
group by 1
having completed_projects >= 2)

select completed_projects, e.id as employee_id, e.salary as salary
from employees e join projemp ep
on e.id = ep.employee_id
group by 1,2,3
order by 2
limit 3
