SELECT
    ROUND(AVG(HEIGHT), 2) AS "Average Height",
    ROUND(AVG(WEIGHT), 2) AS "Average weight"
FROM
    PLAYERS
WHERE
    DEBUT >= '2000-01-01';