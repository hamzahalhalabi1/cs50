SELECT
    FRIEND_ID
FROM
    FRIENDS
    JOIN USERS
    ON ID = USER_ID
WHERE
    USERNAME = 'lovelytrust487'
    AND FRIEND_ID IN (
        SELECT
            FRIEND_ID
        FROM
            FRIENDS
            JOIN USERS
            ON ID = USER_ID
        WHERE
            USERNAME = 'exceptionalinspiration482'
    );

-- with inner join:
-- SELECT f1.friend_id
-- FROM friends f1
-- INNER JOIN friends f2 ON f1.friend_id = f2.friend_id
-- INNER JOIN users u1 ON u1.id = f1.user_id
-- INNER JOIN users u2 ON u2.id = f2.user_id
-- WHERE u1.username = 'lovelytrust487'
-- AND u2.username = 'exceptionalinspiration482';

