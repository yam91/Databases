/*
Task:
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically 
and displayed underneath its corresponding Occupation. 

The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

A pivot table is a table of values which are aggregations of groups of individual values from 
a more extensive table within one or more discrete categories. 
The aggregations or summaries of the groups of the individual terms might include sums, averages, 
counts, or other statistics. 
*/

CREATE TABLE occupations (
  Name VARCHAR(50),
  occupation VARCHAR(50)
);

INSERT INTO occupations VALUES 
('Dana', 'Actor'),
('Noah', 'Professor'),
('Shai', 'Singer'),
('Jesper', 'Professor'),
('Eva', 'Actor'),
('Larry', 'Doctor'),
('Max', 'Professor'),
('Peter', 'Actor'),
('Emma', 'Singer'),
('Dan', 'Actor'),
('Andreas', 'Doctor'),
('Lorenzo', 'Doctor'),
('Zoe', 'Actor');

select tbl1.doctor,tbl2.professor, tbl3.singer, tbl4.actor from
(select row_number() over(order by o.name) idx,o.name as doctor from occupations o where o.occupation='Doctor') tbl1 
FULL OUTER JOIN
(select row_number() over(order by o.name) idx ,o.name as professor from occupations o where o.occupation='Professor') tbl2 
on tbl1.idx = tbl2.idx
FULL OUTER JOIN
(select row_number() over(order by o.name) idx ,o.name as singer from occupations o where o.occupation='Singer') tbl3 
on tbl2.idx = tbl3.idx
FULL OUTER JOIN
(select row_number() over(order by o.name) idx ,o.name as actor from occupations o where o.occupation='Actor') tbl4 
on tbl3.idx = tbl4.idx;

/*
New things:
1. ROW_NUMBER() OVER PARTITION BY : an SQL function that assigns a unique sequential 
    number to each row within a specific partition: 
        SELECT ROW_NUMBER() OVER(ORDER BY table_name.column_name) idx
    will result in a list of indexed ordered column entries.

2. Partition of a table:
        SELECT row_number() over(order by table_alias.column_name) idx, table_alias.column_name 
        AS part1 FROM table_name table_alias
    can be accessed then from the table itself by:
        table_alias.part1
    and will contain two columns; idx and column_name.

3. We already saw LEFT and RIGHT OUTER JOINs that can produce rows with missing entries
   for columns of no match. FULL OUTER JOIN allows no mtach for columns from either table.
   The missing entries are inserted as NULL.
   * We can think of LEFT/RIGHT OUTER JOIN as constricting the presence of entries in the 
   columns of the LEFT/RIGHT table respectively.
   * Remember: JOINS are about uniting columns !
*/


/*
Generate the following two result sets:
1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the 
   first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). 
   For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).

2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, 
   and output them in the following format:
   
   There are a total of [occupation_count] [occupation]s.

   where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is 
   the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be 
   ordered alphabetically.

Note: There will be at least two entries in the table for each type of occupation.
*/

--Solution:
SELECT CONCAT(Name, '(', SUBSTRING(Occupation,1,1), ')') AS name
FROM Occupations
ORDER BY name;
SELECT CONCAT('There are a total of ', COUNT(*), ' ',LOWER(Occupation),'s.') as result
FROM Occupations
GROUP BY Occupation
ORDER BY result ASC;

-- Using UNION, column must have the same name and type!
SELECT CONCAT(Name, '(', SUBSTRING(Occupation,1,1), ')') AS name
FROM Occupations
union
SELECT CONCAT('There are a total of ', COUNT(*), ' ',LOWER(Occupation),'s.') as name
FROM Occupations
GROUP BY Occupation
ORDER BY name ASC;
-- Will break down if a name start with a letter after T.