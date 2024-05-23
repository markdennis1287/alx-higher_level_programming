--Lists records in second_table except those without a name value
--Displays score and name in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

