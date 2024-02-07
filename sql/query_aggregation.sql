-- SQL file to use aggregation functions including COUNT, AVG, MIN, and MAX

-- Aggregation query on the 'books' table, to gain insights about the years published 

SELECT 
    COUNT(year_published),
    AVG(year_published),
    MIN(year_published),
    MAX(year_published)
    FROM books; 