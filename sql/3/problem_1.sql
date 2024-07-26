with output_data as (
    select * from Employee where managerId is not null
), formatted_data as (select managerid, count(*) from output_data group by managerid ), final_data as (select managerid from formatted_data where count >= 5 ) select e.name as name from final_data fd inner join Employee e on fd.managerid = e.id;