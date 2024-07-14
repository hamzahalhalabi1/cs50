CREATE TABLE
 temp (
		sentence_number INTEGER,
		starting_char      INTEGER,
		length          INTEGER
	);

INSERT INTO
 temp (sentence_number, starting_char, length)
VALUES
	(14, 98, 4),
	(114, 3, 5),
	(618, 72, 9),
	(630, 7, 3),
	(932, 12, 5),
	(2230, 50, 7),
	(2346, 44, 10),
	(3041, 14, 5);

CREATE VIEW
	message AS
SELECT
	substr (sentence, starting_char, length) AS phrase
FROM
	sentences
	JOIN temp ON temp.sentence_number = sentences.id;