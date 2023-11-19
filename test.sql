--AGGREGATE     
--count of number of cases which occurred in each area?

select COUNT(*), Location from cases group by Location;

-- count number of cases solved by each Officer
select count(*), OfficerId from cases group by OfficerId;

--STORED FUNCTION

SELECT date_difference(DOC) from ARREST;
--Unions

--Give the list of cases which occurred before 2015 and after 2022.
select * from cases where year (DOC)<2015
UNION
select * from cases where year (DOC)>2022;


-- Join

--Q1.Retrieve the details of all arrests made, including the arrest date and location, the officer's full name, and the associated criminal's name.
SELECT ARREST .DOC, ARREST. Location, OFFICER.FirstName, OFFICER.LastName, CRIMINAL.Name FROM ARREST 
JOIN OFFICER ON ARREST.OfficerId = OFFICER.OfficerId JOIN CRIMINAL ON ARREST.CriminalId  = CRIMINAL.CriminalId;



--Q2 Retrieve the details of all officers along with the number of cases they are assigned to. Using left join

SELECT OFFICER.*, COUNT(cases.CaseId) AS NumberOfCases FROM OFFICER LEFT JOIN CASES ON OFFICER.OfficerId = CASES.OfficerId GROUP BY
OFFICER.OfficerId;