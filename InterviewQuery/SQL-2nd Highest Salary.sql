-- https://www.interviewquery.com/questions/2nd-highest-salary

with employeedepartment (salary)
as(
select salary
from employees e join (select * from departments 
                            where name like '%engineering%')d
on e.department_id=d.id
)
select max(salary) as salary
from employeedepartment
where salary < (select max(salary) from employeedepartment)