SELECT
    YEAR,
    HR
FROM
    PERFORMANCES
WHERE
    PLAYER_ID = (
        SELECT
            ID
        FROM
            PLAYERS
        WHERE
            FIRST_NAME = 'Ken'
            AND LAST_NAME = 'Griffey'
            AND BIRTH_YEAR = 1969
    )
ORDER BY
    YEAR DESC;