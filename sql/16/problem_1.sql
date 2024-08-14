with output_data as (
    select p.product_name, s.year, s.price from Sales s inner join Product p on s.product_id = p.product_id
) select * from output_data;