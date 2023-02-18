-- https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan&id=sql-i

select patient_id, patient_name, conditions
from patients
where conditions like '% DIAB1%' or conditions like 'DIAB1%'
order by patient_id asc