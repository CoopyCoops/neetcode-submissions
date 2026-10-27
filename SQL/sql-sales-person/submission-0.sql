-- Write your query below
with crimson as (
    select com_id
    from company
    where name = 'CRIMSON'
)

select distinct name
from sales_person s
where sales_id NOT IN (
    select distinct o.sales_id
    from orders o
    join crimson c on o.com_id = c.com_id
)