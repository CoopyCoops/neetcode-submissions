-- Write your query below
select first_name, last_name, COALESCE(city, NULL) as city, COALESCE(state, NULL) as state
from person p left join address a on p.person_id = a.person_id