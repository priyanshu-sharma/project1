-- Write your PostgreSQL query statement below
with output_data as (
    select * from Orders where order_date > '2018-12-31' and order_date < '2020-01-01'
), formatted_data as (
    select buyer_id, count(*) as orders_in_2019 from output_data group by buyer_id 
) select u.user_id as buyer_id, u.join_date, CASE WHEN f.orders_in_2019 is NULL THEN 0 ELSE f.orders_in_2019 END as orders_in_2019 from Users u left join formatted_data f on u.user_id = f.buyer_id;