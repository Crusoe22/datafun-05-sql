-- SQL file to use aggregation functions including COUNT, AVG, SUM

-- Aggregation query on the 'rentals' table, to gain insights about the rental 
-- periods of VCRs. Calculate the total number of rentals, the average rental period, and the sum of all rental periods in days.
SELECT 
    COUNT(year_published),
    AVG(year_published),
    MIN(year_published),
    MAX(year_published)
    FROM books; 