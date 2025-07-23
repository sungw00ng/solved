select 
animal_type as ANIMAL_TYPE,
ifnull(name,'No name') as NAME,
sex_upon_intake as SEX_UPON_INTAKE
from animal_ins
