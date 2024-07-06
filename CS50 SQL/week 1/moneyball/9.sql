SELECT
    NAME,
    ROUND(AVG(SALARY), 2) AS 'average salary'
FROM
    SALARIES
    JOIN TEAMS
    ON TEAMS.ID = SALARIES.TEAM_ID
    where salaries.year = 2001
GROUP BY
    NAME
ORDER BY
    AVG(SALARY) asc limit 5;