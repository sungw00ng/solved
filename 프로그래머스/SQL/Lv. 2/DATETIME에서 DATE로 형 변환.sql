select
animal_id as ANIMAL_ID,
name as NAME,
date_format(datetime,"%Y-%m-%d") as '날짜'
from animal_ins
order  by animal_id;
