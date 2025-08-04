select
    case
    when month(differentiation_date) between 1 and 3 then '1Q'
    when month(differentiation_date) between 4 and 6 then '2Q'
    when month(differentiation_date) between 7 and 9 then '3Q'
    when month(differentiation_date) between 10 and 12 then '4Q'
    end as QUARTER,
    count(*) as ECOLI_COUNT
from ecoli_data
group by QUARTER
order by QUARTER;
