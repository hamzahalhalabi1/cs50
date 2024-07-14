CREATE VIEW RURAL AS
    SELECT
        *
    FROM
        CENSUS
    WHERE
        LOCALITY LIKE '%rural%';