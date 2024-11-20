/*
In MySQL Workbench:
- Create a new model.
- File -> import... -> reverse engineer MySQL script.
- Upload script, after this it should create the tables in the script.

To inspect the ERD:
- Create diagram and drag tables into the sheet.
- Can edit relationships to account for 0-or-many, clicking on the links between the tables. 
*/


CREATE TABLE EmployeeStatus (
  EmployeeStatusId INT PRIMARY KEY,
  StatusDecription CHAR
);

/* 
Cardinality between Technician and EmployeeStatus tables:
Technician to EmployeeStatus - one technician can only have one status, therefore 1 and only 1.
EmployeeStatus to Technician - one employeestatus can correspond to 0 or more Technicians.
*/
CREATE TABLE Technician (
  EmployeeId INT PRIMARY KEY,
  FirstName CHAR,
  LastName CHAR,
  EmailAddress CHAR,
  AnnualSalary INT,
  SpecialSkill Char,
  EmployeeStatusId INT,
  FOREIGN KEY (EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)
);

CREATE TABLE ServiceStatus (
  ServiceStatusId INT PRIMARY KEY,
  ServiceDescription CHAR
);


CREATE Table City (
  CityId INT PRIMARY KEY,
  CityName CHAR
);

/* 
Cardinality between City and Building tables:
City to Building - one City can have 0 or more Building.
Building to City - one Building can correspond to 0 or more City. 
*/
CREATE Table Building (
  BuildingId INT PRIMARY KEY,
  CityId INT,
  Floors INT,
  FOREIGN KEY (CityId) REFERENCES City(CityId)
);


CREATE TABLE ElevatorType (
  ElevatorTypeId INT PRIMARY KEY,
  TypeName CHAR
);

/* 
Cardinality between ElevatorModel and ElevatorType tables:
ElevatorModel to ElevatorType - one ElevatorModel can be only one ElevatorType.
ElevatorType to ElevatorModel - one ElevatorType can correspond 0 or more ElevatorModel.
*/

CREATE TABLE ElevatorModel (
  ElevatorModelId INT PRIMARY KEY,
  ModelName INT,
  Speed INT,
  MaxWeight INT,
  PeopleLimit INT,
  ElevatorTypeId INT,
  FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);


/* 
Cardinality between Elevator and Building tables:
Elevator to Building - one Elevator can have one and only one Building.
Building to Elevator - one Building can correspond to 0 or more Elevators.

Cardinality between Elevator and ElevatorModel:
Elevator to ElevatorModel - one Elevator can have one and only one ElevatorModel.
ElevatorModel to Elevator - one ElevatorModel can correspond to 0 or more Elevators.
*/

CREATE TABLE Elevator (
  ElevatorId INT PRIMARY KEY,
  ElevatorModelId INT,
  BuildingId INT,
  InstallationDate DATE,
  FOREIGN KEY (BuildingId) REFERENCES Building(BuildingId),
  FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId)

);


/* 
Cardinality between Technician and ServiceActivity tables:
Technician to ServiceActivity - one technician can have zero or more ServiceActivity.
ServiceActivity to Technician - one ServiceActivity can correspond one, and only one, Technician.

Cardinality between Elevator and ServiceActivity tables:
Elevator to ServiceActivity - one Elevator can correspond to 0 or more ServiceActivity.
ServiceActivity to Elevator - one ServiceActivity can only have one, and only one, Elevator.


Cardinality between ServiceStatus and ServiceActivity tables:
ServiceStatus to ServiceActivity - one ServiceStatus can correspond to 0 or more ServiceActivitiy.
ServiceActivity to ServiceStatus  - one ServiceActivity can have one, and only one, ServiceStatus.
*/

CREATE TABLE ServiceActivity (
  ServiceActivityId INT PRIMARY KEY,
  EmployeeId INT,
  ElevatorId INT,
  ServiceDateTime DATE,
  ServiceDescription CHAR,
  ServiceStatusId INT,
  FOREIGN KEY (EmployeeId) REFERENCES Technician(EmployeeId),
  FOREIGN KEY (ServiceStatusId) REFERENCES ServiceStatus(ServiceStatusId),
  FOREIGN KEY (ElevatorId) REFERENCES Elevator(ElevatorId)
);


