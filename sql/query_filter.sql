-- SQL file to filter data

-- Filter the authors table by last and first name
SELECT *
FROM authors
WHERE  last_name LIKE '%O%' AND first_name LIKE '%J%'