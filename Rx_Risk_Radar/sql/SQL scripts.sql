
SELECT * FROM faers_2020q4 LIMIT 11;


SELECT pt, COUNT(*) AS total_reports
FROM faers_2020q4
GROUP BY pt
ORDER BY total_reports DESC
LIMIT 10;



SELECT sex, pt, COUNT(*) AS count
FROM faers_2020q4
GROUP BY sex, pt
ORDER BY count DESC
LIMIT 10;


SELECT sex, pt, COUNT(*) AS count
FROM faers_2020q4
GROUP BY sex, pt
ORDER BY count DESC 
LIMIT 10;


SELECT drugname, COUNT(*) as cases
FROM faers_2020q4
GROUP BY drugname 
ORDER BY cases DESC 
LIMIT 10;


SELECT DISTINCT(age_cod) FROM faers_2020q4


SELECT age, age_cod, sex, pt, COUNT(*) as cases 
FROM faers_2020q4
WHERE age_cod = 'YR' AND age >= '65'
GROUP BY age 
ORDER BY age, cases DESC 
LIMIT 10;

--
SELECT sex, pt, COUNT(*) as cases
FROM faers_2020q4 
WHERE sex != 'NULL'
GROUP BY pt, sex
ORDER BY cases DESC;


SELECT COUNT(*) AS missing_age_count
FROM  faers_2020q4
WHERE age IS NULL;










































