with oe_data as (
    select *, case when amount % 2 = 0 then amount else 0 end as even_amount, case when amount % 2 = 1 then amount else 0 end as odd_amount from transactions 
), goe_data as (
    select transaction_date, sum(odd_amount) as odd_sum, sum(even_amount) as even_sum from oe_data group by transaction_date
) select * from goe_data order by transaction_date;