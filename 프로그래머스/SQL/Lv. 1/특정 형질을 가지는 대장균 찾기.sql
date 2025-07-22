select count(*) as COUNT
from ecoli_data
where genotype & 0b0010 = 0 
and genotype & 0b0101 > 0
