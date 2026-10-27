-- Write your query below
select distinct customer_id, customer_name
from customers
where customer_id NOT IN (select distinct customer_id from orders where product_name = 'C')
AND customer_id IN (select distinct customer_id from orders where product_name = 'A')
AND customer_id IN (select distinct customer_id from orders where product_name = 'B')
order by customer_name