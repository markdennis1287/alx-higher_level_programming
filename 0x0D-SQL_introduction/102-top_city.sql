-- Calculate top 3 cities with highest average temperature during July and August
SELECT city, AVG(temp) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

