select 
animal_id as ANIMAL_ID,
name as NAME,
    case
    when sex_upon_intake like 'Neutered%' or
    sex_upon_intake like 'Spayed%' then 'O'
    else 'X'
    end as '중성화'
from animal_ins
