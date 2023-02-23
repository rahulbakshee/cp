-- https://www.interviewquery.com/questions/exam-scores

SELECT 
student_name, 
sum(case 
    when exam_id = 1 then score else NULL 
end) as exam_1,

sum(case 
    when exam_id = 2 then score else NULL 
end) as exam_2,

sum(case 
    when exam_id = 3 then score else NULL 
end) as exam_3,

sum(case 
    when exam_id = 4 then score else NULL 
end) as exam_4

FROM exam_scores
group by 1
