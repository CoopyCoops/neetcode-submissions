-- Write your query below
with score_rank as (
    select student_id, exam_id, score,
    ROW_NUMBER() OVER (PARTITION by student_id ORDER by score desc, exam_id asc) as rk
    from exam_results
)

select student_id, exam_id, score
from score_rank
where rk = 1
order by student_id