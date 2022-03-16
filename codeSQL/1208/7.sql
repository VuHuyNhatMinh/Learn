CREATE TABLE countries (
	country_id		int,
	country_name 	varchar(80)	CHECK (country_name = 'Italy' OR country_name = 'India' or country_name = 'China'),
	region_id 		int
);

/*
	Ref: 61 - 5.4.1. Check Constraints.
*/