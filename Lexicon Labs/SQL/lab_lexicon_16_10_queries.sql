USE clinic;
-- Assignment 2:
-- before select:
SELECT *
FROM employees
ORDER BY salary;

-- select
SELECT id, concat(first_name, ' ', last_name) AS full_name, job_title, salary
FROM employees 
WHERE salary > 1000.00
ORDER BY id;

-- Assignment 3:
-- before update:
SELECT first_name, last_name, salary
FROM employees
WHERE job_title = 'Dentist'
ORDER BY salary ASC;

-- update salaries of dentists:
UPDATE employees
SET salary = 1.1 * salary
WHERE job_title = 'Dentist'
SELECT job_title, salary;

-- after update:
SELECT first_name, last_name, salary
FROM employees
WHERE job_title = 'Dentist'
ORDER BY salary ASC;

-- show all salaries after update in ascending order:
SELECT salary
FROM employees
ORDER BY salary ASC;

-- Assignment 4:

-- before delete:
SELECT *
FROM employees
ORDER BY department_id;

-- delete:
DELETE FROM employees
WHERE department_id BETWEEN 3 AND 4;

-- after delete:
SELECT *
FROM employees
ORDER BY department_id;