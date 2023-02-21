-- https://leetcode.com/problems/second-highest-salary

select ifnull(
    (select distinct salary
    from employee
    order by 1 desc
    limit 1
    offset 1), NULL)  as SecondHighestSalary