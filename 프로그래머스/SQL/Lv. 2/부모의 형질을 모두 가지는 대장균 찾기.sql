select
child.id,
child.genotype,
parent.genotype as PARENT_GENOTYPE
from ecoli_data as parent
join ecoli_data as child
on parent.id = child.parent_id
where (parent.genotype & child.genotype) = parent.genotype
order by child.id;
