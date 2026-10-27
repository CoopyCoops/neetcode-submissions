-- Write your query below
with distance as (
    select user_id, sum(distance) as distance
    from rides
    group by user_id
)

select u.name, coalesce(d.distance, 0) as travelled_distance
from users u left join distance d on u.id = d.user_id
order by coalesce(d.distance, 0) desc, u.name asc