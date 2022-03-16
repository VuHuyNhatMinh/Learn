CREATE TABLE countries (
	country_id		int 	UNIQUE,
	country_name 	varchar(80),
	region_id 		int
);

/*
	Ref: Pg 64 - 5.4.3. Unique Constraints.
	Table vs Column constraint.
*/
