SELECT
    COUNT(*)
FROM
    PLAYERS
WHERE
    (THROWS = 'L'
    AND BATS = 'R')
    OR (THROWS = 'R'
    AND BATS = 'L');