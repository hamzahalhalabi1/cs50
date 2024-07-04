SELECT
    NAME
FROM
    SCHOOLS
WHERE
    DISTRICT_ID = (
        SELECT
            ID
        FROM
            DISTRICTS
        WHERE
            NAME IS 'Cambridge'
    );