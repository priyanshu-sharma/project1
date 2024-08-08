with output_data as (
    select id, state, amount, to_char(trans_date, 'YYYY-MM') as month, case when country is null then 'a' else country end as country from Transactions
), total_transaction as (
    select month, country, count(*) as trans_count, sum(amount) as trans_total_amount from output_data group by month, country
), final_data as (
    select * from output_data
    where state = 'approved'  
), approved_transaction as (
    select month, country, count(*) as approved_count, sum(amount) as approved_total_amount from final_data group by month, country
) select tt.month, case when tt.country = 'a' then null else tt.country end , tt.trans_count, case when ap.approved_count is null then 0 else ap.approved_count end, tt.trans_total_amount, case when ap.approved_total_amount is null then 0 else ap.approved_total_amount end from total_transaction tt left join approved_transaction ap on tt.month = ap.month and tt.country = ap.country;