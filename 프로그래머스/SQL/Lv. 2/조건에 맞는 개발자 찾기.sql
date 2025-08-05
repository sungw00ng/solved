select distinct
t.id,
t.email,
t.first_name,
t.last_name
from (
    select d.*, s.code
    from developers as d
    join skillcodes as s
    on s.name='Python' or s.name='C#'
) t
where t.skill_code & t.code != 0
order by t.id
