# Write your MySQL query statement below
with store_one as (
    select product_id, 'store1' as store, store1 as price from Products
    where store1 is not null
), store_two as (
    select product_id, 'store2' as store, store2 as price from Products
    where store2 is not null
), store_three as (
    select product_id, 'store3' as store, store3 as price from Products
    where store3 is not null
) select * from store_one UNION select * from store_two UNION select * from store_three;