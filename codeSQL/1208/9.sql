CREATE TABLE jobs(
	job_id		int,
	job_title	varchar(50)	DEFAULT '',
	min_salary	int			DEFAULT 8000,
	max_salary	int 		DEFAULT NULL
);

/*
	Ref: 59 - 5.2. Default Values.
*/