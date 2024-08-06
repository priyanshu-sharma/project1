with output_data as (
    select *, dense_rank() over (partition by product_id order by year asc) as rank from Sales
) select product_id, year as first_year, quantity, price from output_data where rank = 1;