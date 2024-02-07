-- SQL query to use GROUP BY clause

-- Query to Count Rentals per VCR
SELECT year_published, COUNT(*) AS published_books
FROM books
GROUP BY year_published
ORDER BY published_books DESC; 