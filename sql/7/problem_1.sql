with output_data as (
    select *, dense_rank() over (partition by departmentId order by salary desc) as salary_rank from Employee
) select d.name as Department, od.name as Employee, od.salary as Salary from output_data od inner join Department d on od.departmentId = d.id where od.salary_rank = 1;