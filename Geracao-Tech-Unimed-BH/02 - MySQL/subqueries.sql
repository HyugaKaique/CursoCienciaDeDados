-- subqueries
use company;

select * from employee;

select distinct Pnumber from project 
where Pnumber in 
	(
		select distinct Pno from works_on , employee
        where (Essn = Ssn and Fname ='Ramesh'
    ) 
    or
    (
		select Pnumber from project, departament, employee
        where (Mgr_ssn = Ssn and Fname = 'Ramesh' and Dnum= Dnumber)
	)
);

select  distinct * from works_on where (Pno, Hours) in (select Pno, Hours from works_on where Essn='123456789');

-- clausulas com exists e unique
select e.Fname from employee as e 
where exists(select * from dependent as d where e.Ssn = d.Essn and Relationship = 'Daughter');

-- sem dependentes 
select e.Fname from employee as e 
where not exists(select * from dependent as d where e.Ssn = d.Essn);

select e.Fname from employee as e, departament d
where(e.Ssn = d.Mgr_ssn) and exists(select * from dependent as d where e.Ssn = d.Essn);

select Fname from employee where(select count(*) from dependent where Ssn=Essn)>=2;

select distinct Essn, Pno from works_on where Pno in (1,2,3);