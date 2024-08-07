with output_data as (
    select *, CASE WHEN order_date = customer_pref_delivery_date THEN 'Immediate' ELSE 'Scheduled' END as order_type from Delivery
), formatted_data as ( 
    select *, dense_rank() over (partition by customer_id order by order_date) as rank from output_data ),
    immediate_orders as (select count(*) as total_immediate from formatted_data where rank = 1 and order_type = 'Immediate'), total_orders as (
        select count(*) as total_order from formatted_data where rank = 1
    ) select ROUND(immediate_orders.total_immediate * 100.00 / total_orders.total_order * 1.00, 2) as immediate_percentage  from immediate_orders, total_orders;