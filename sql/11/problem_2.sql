with low_data as (
    select 'Low Salary' as category, count(case when income < 20000 then 1 else null end) as accounts_count from Accounts
), average_data as (
    select 'Average Salary' as category, count(case when income >= 20000 and income <= 50000 then 1 else null end) as accounts_count from Accounts
), high_data as (
    select 'High Salary' as category, count(case when income > 50000 then 1 else null end) as accounts_count from Accounts
) select * from low_data union all select * from average_data union all select * from high_data;