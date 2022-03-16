CREATE TABLE job_history(
	employee_id			int	UNIQUE,
	start_date			varchar(80),
	end_date			varchar(80),
	job_id				int	REFERENCES jobs (job_id) ,
	department_id		int
);

/*
	Ref: 66 - 5.4.5. Foreign Keys.
*/

