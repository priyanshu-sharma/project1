with gm as (
    select u.user_id, u.name as results, count(*) from Users u inner join MovieRating mr on u.user_id = mr.user_id group by u.user_id, u.name order by count desc, u.name asc limit 1
), fv as (
    select m.movie_id, m.title, mr.rating, mr.created_at from Movies m inner join MovieRating mr on m.movie_id = mr.movie_id where mr.created_at > '2020-01-31' and mr.created_at < '2020-03-01'
), ha as (
    select movie_id, title as results, avg(rating) as average from fv group by movie_id, title order by average desc, results asc limit 1) select results from gm union all select results from ha;