with unique_users as (
    select distinct(user_id) from Signups
), total_messages as (
    select user_id, count(*) as total_message from Confirmations group by user_id
), confirm_messages as (
    select user_id, count(*) as confirm_message from Confirmations group by user_id, action having action = 'confirmed'
), final_message as (
    select tm.user_id, case when cm.confirm_message is null then 0 else cm.confirm_message end as confirm_message, tm.total_message from total_messages tm left join confirm_messages cm on tm.user_id = cm.user_id
), output_data as (
    select uu.user_id, case when fm.confirm_message is null then 0 else fm.confirm_message end as confirm_message, case when fm.total_message is null then 0 else fm.total_message end as total_message from unique_users uu left join final_message fm on uu.user_id = fm.user_id
) select user_id, case when total_message = 0 then 0 else round(confirm_message * 1.0 /total_message * 1.0, 2) end as confirmation_rate from output_data;