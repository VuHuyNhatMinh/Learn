CREATE TABLE jobs(
	job_id		int,
	job_title	varchar(50),
	min_salary	int,
	max_salary	int CHECK (max_salary > 25000)
);

/*
	Ref: 61 - 5.4.1. Check Constraints.
*/