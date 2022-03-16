CREATE TABLE countries (
	country_id		int,
	country_name 	varchar(80),
	region_id 		int,
	UNIQUE (country_id, region_id)
);

/*
	Ref: Pg 64 - 5.4.3. Unique Constraints.
*/
	