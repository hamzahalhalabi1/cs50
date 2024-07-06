-- Subquery to get top 10 players by SALARY/H for the year 2001
WITH top_salary_h AS (
    SELECT
        PLAYERS.FIRST_NAME,
        PLAYERS.LAST_NAME
    FROM
        PLAYERS
    JOIN PERFORMANCES ON PERFORMANCES.PLAYER_ID = PLAYERS.ID
    JOIN SALARIES ON SALARIES.PLAYER_ID = PLAYERS.ID AND PERFORMANCES.YEAR = SALARIES.YEAR
    WHERE
        PERFORMANCES.YEAR = 2001
        AND SALARIES.SALARY / PERFORMANCES.H IS NOT NULL
    ORDER BY
        SALARIES.SALARY / PERFORMANCES.H,
        PLAYERS.FIRST_NAME,
        PLAYERS.LAST_NAME
    LIMIT 10
)

-- Main query to get top 10 players by SALARY/RBI for the year 2001
SELECT
    PLAYERS.FIRST_NAME,
    PLAYERS.LAST_NAME
FROM
    PLAYERS
JOIN PERFORMANCES ON PERFORMANCES.PLAYER_ID = PLAYERS.ID
JOIN SALARIES ON SALARIES.PLAYER_ID = PLAYERS.ID AND PERFORMANCES.YEAR = SALARIES.YEAR
JOIN top_salary_h ON PLAYERS.FIRST_NAME = top_salary_h.FIRST_NAME AND PLAYERS.LAST_NAME = top_salary_h.LAST_NAME
WHERE
    PERFORMANCES.YEAR = 2001
    AND SALARIES.SALARY / PERFORMANCES.RBI IS NOT NULL
ORDER BY
    SALARIES.SALARY / PERFORMANCES.RBI,
    PLAYERS.FIRST_NAME,
    PLAYERS.LAST_NAME
LIMIT 10;
