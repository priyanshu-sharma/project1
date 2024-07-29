CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    with output_data as (
        select *, dense_rank() over (order by Employee.salary desc) as rank from Employee
    ) select distinct(output_data.salary) from output_data where rank = N
  );
END;