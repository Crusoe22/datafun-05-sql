-- SQL query to use INNER JOIN operation

-- Query to combine author and book Information
SELECT *
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;
