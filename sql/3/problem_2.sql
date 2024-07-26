with output_data as (
    select requester_id as id, count(*) as num from RequestAccepted group by requester_id
), formatted_data as (
    select accepter_id as id, count(*) as num from RequestAccepted group by accepter_id
), final_data as (select * from formatted_data UNION ALL select * from output_data ) 
select id, sum(num) as num from final_data group by id order by num desc limit 1;