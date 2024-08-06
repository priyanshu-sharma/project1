with output_data as (
    select distinct(c.customer_id, c.product_key), c.customer_id, c.product_key from Customer c inner join Product p on c.product_key = p.product_key
) select customer_id from output_data group by customer_id having count(customer_id) = (select count(distinct(product_key)) from Product); 