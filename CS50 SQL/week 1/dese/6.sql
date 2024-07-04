SELECT
    NAME
FROM
    SCHOOLS
WHERE
    ID IN (
        SELECT
            SCHOOL_ID
        FROM
            GRADUATION_RATES
        WHERE
            GRADUATED = 100
    );