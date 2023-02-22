-- https://www.interviewquery.com/questions/employee-salaries


select 
d.name as department_name, 
count(e.id) as number_of_employees,

sum(case 
    when salary > 100000 then 1 
    else 0
end)/ count(salary) as percentage_over_100k

from employees e join departments d
on e.department_id = d.id
group by 1
having number_of_employees >=10