SELECT
    YEAR,
    SALARY
FROM
    SALARIES
WHERE
    PLAYER_ID = (
        SELECT
            ID
        FROM
            PLAYERS
        WHERE
            FIRST_NAME IS 'Cal'
            AND LAST_NAME IS 'Ripken'
    )
ORDER BY
    YEAR DESC;