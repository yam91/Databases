
-- 1. create Write a SQL statement to create a simple table countries including
-- columns country_id,country_name and region_id.

CREATE TABLE countries (
  country_id INT,
  country_name VARCHAR(50),
  region_id INT
);

-- Doesn't generate error:
INSERT INTO countries VALUES (NULL,'China', 2);


-- 2. Write a SQL statement to create the structure of a table dup_countries
-- similar to countries.

CREATE TABLE dup_countries AS SELECT * FROM countries;

-- 3. Write a SQL statement to create a table countries set a constraint NOT
-- NULL

CREATE TABLE countries1 (
  country_id INT NOT NULL,
  country_name VARCHAR(50) NOT NULL,
  region_id INT NOT NULL
);

-- Generates error:
-- INSERT INTO countries1 VALUES ( NULL,'China', 2);

-- 4. Write a SQL statement to insert a record with your own value into the
-- table countries against each columns.

INSERT INTO countries1 VALUES (0,'China', 2);

-- 5. Write a SQL statement to insert 3 rows by a single insert statement.

INSERT INTO countries1 VALUES (1, 'India', 2), (2, 'USA', 1), 
                                 (3, 'Canada', 1), (4, 'Sweden', 3);
                            
-- 6. Write a SQL statement to insert a record into the table countries to
-- ensure that, a country_id and region_id combination will be entered once in
-- the table

CREATE TABLE countries2 (
  country_id INT NOT NULL UNIQUE,
  country_name VARCHAR(50) NOT NULL,
  region_id INT NOT NULL UNIQUE
);

-- Generates an error every time region_id or country_id are the same for two
-- different entries.
-- INSERT INTO countries2 VALUES (1, 'India', 2), (2, 'USA', 1), 
--                               (3, 'Canada', 3), (4, 'Sweden', 3);