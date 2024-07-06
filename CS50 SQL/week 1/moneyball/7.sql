SELECT
    FIRST_NAME,
    LAST_NAME
FROM
    PLAYERS
    JOIN SALARIES
    ON SALARIES.PLAYER_ID = PLAYERS.ID
ORDER BY
    SALARY DESC LIMIT 1;