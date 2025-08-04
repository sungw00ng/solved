with maxcolony as (
    select 
        YEAR(differentiation_date) as year,
        max(size_of_colony) as maxcolony
    from
        ecoli_data
    group by
        YEAR(differentiation_date)
)

select 
    YEAR(e.differentiation_date) as YEAR,
    m.maxcolony-e.size_of_colony as YEAR_DEV,
    e.id
from ecoli_data as e
join maxcolony as m
on YEAR(e.differentiation_date)=m.year
order by YEAR, YEAR_DEV
