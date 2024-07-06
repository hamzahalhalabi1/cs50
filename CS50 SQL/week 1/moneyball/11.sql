SELECT
    FIRST_NAME,
    LAST_NAME,
    SALARY/H AS 'dollars per hit'
FROM
    PLAYERS
    JOIN PERFORMANCES
    ON PERFORMANCES.PLAYER_ID = PLAYERS.ID
    JOIN SALARIES
    ON SALARIES.PLAYER_ID = PLAYERS.ID
WHERE
    PERFORMANCES.YEAR = 2001
    AND SALARY/H IS NOT NULL
ORDER BY
    SALARY/H,
    FIRST_NAME,
    LAST_NAME LIMIT 10;