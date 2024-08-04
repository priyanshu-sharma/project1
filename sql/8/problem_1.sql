with output_data as (
    select *, recordDate - 1 as previous_day from Weather
) select od.id as Id from output_data od inner join Weather w on od.previous_day = w.recordDate where od.temperature > w.temperature;