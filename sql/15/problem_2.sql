with odd_data as (
    select * from Seat where id % 2 = 1
), even_data as (
    select * from Seat where id % 2 = 0
), odd as (
    select od.id, ed.student from odd_data od left join even_data ed on od.id + 1 = ed.id where ed.id is not null
), even as (
    select ed.id, od.student from even_data ed left join odd_data od on ed.id - 1 = od.id where od.id is not null
), complete_data as (
    select * from odd union select * from even
) select s.id as id, case when cd.student is null then s.student else cd.student end as student from Seat s left join complete_data cd on s.id = cd.id;