SELECT
    NAME
FROM
    TEAMS
WHERE
    ID in (
        SELECT
            TEAM_ID
        FROM
            PERFORMANCES
        WHERE
            PLAYER_ID = (
                SELECT
                    ID
                FROM
                    PLAYERS
                WHERE
                    FIRST_NAME IS 'Satchel'
            )
    );

-- it can also be solved with join --
-- SELECT
--     DISTINCT TEAMS.NAME
-- FROM
--     TEAMS
--     JOIN PERFORMANCES
--     ON PERFORMANCES.TEAM_ID = TEAMS.ID
--     JOIN PLAYERS
--     ON PLAYERS.ID = PERFORMANCES.PLAYER_ID
-- WHERE
--     PLAYERS.FIRST_NAME = 'Satchel';