-- SQL file to filter data

-- Filter the authors table by last and first name
SELECT *
FROM authors
WHERE  last = '%O%' AND first = '%J%'