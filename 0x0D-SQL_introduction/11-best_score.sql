--Lists records from second_table where score >= 10 by score(top first)--
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

