CREATE VIEW AVAILABLE AS
    SELECT
        LISTINGS.ID,
        PROPERTY_TYPE,
        HOST_NAME,
        DATE
    FROM
        LISTINGS
        JOIN AVAILABILITIES
        ON AVAILABILITIES.LISTING_ID = LISTINGS.ID
    WHERE
        AVAILABLE IS 'TRUE';