with output_data as (
    select sp.name from Orders o inner join SalesPerson sp on o.sales_id = sp.sales_id inner join Company c on o.com_id = c.com_id where c.name = 'RED'
) select sp.name from SalesPerson sp left join output_data od on sp.name = od.name where od.name is null;