SELECT r.person_id, 
       r.department_id,
       r.salary
FROM
(SELECT e.id AS person_id, 
        d.id  AS department_id, 
        e.salary AS salary, 
        DENSE_RANK() OVER(PARTITION by d.name ORDER BY salary DESC) 
        AS place

    FROM Employee e 
    JOIN Department d
    ON e.departmentId = d.id) 
    AS r
WHERE r.place = 2
