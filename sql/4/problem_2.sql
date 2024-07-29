-- Write your PostgreSQL query statement below
with output_data as (
    select score, dense_rank() over (order by score desc) as rank from Scores
) select * from output_data;