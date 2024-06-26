SELECT
    FIRST_NAME AS FIRSTNAME,
    LAST_NAME  AS LASTNAME,
    DEBUT
FROM
    PLAYERS
WHERE
    BATS = 'L'
    AND THROWS = 'R'
ORDER BY
    DEBUT ASC;