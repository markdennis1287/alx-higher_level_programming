-- Calculate max temperature of each state ordered by State name
SELECT state, MAX(temp) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

