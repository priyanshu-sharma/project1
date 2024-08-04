with output_data as (
    select c.id as cid, c.name as name, o.id as o_id, o.customerId as ocid from Customers c left join Orders o on c.id = o.customerId
) select name as Customers from output_data where o_id is null;