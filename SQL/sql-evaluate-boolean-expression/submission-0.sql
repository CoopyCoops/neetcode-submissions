-- Write your query below
select e.left_operand, e.operator, e.right_operand,
case when operator = '>' and vl.value > vr.value then 'true'
    when operator = '<' and vl.value < vr.value then 'true'
    when operator = '=' and vl.value = vr.value then 'true'
    else 'false' end as value
from expressions e
join variables vl on e.left_operand = vl.name
join variables vr on e.right_operand = vr.name