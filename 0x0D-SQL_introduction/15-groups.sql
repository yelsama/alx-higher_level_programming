-- lis all numbers or records with the same score
SELECT score, COUNT(score) AS number FROM second_table ORDER BY score DESC;
