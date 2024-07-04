SELECT
    CITY,
    COUNT(NAME)
FROM
    SCHOOLS
WHERE
    TYPE = 'Public School'
GROUP BY
    CITY
HAVING
    COUNT(NAME) <=3
ORDER BY
count(name) desc, city;