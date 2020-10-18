PRAGMA foreign_keys=ON;
CREATE TABLE Servers(sid INT PRIMARY KEY,
name VARCHAR(100));
CREATE TABLE Members(name VARCHAR(100),
sid REFERENCES Servers(sid),
optin INT,
PRIMARY KEY(name, sid));