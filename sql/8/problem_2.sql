with output_data as (
    select player_id, event_date, dense_rank() over (partition by player_id order by event_date) as dense_rank from Activity 
) select player_id, event_date as first_login from output_data where dense_rank = 1;