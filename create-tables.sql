PRAGMA foreign_keys=ON;
-- Create Table to store Server/Guild Information
CREATE TABLE Servers(sid INT PRIMARY KEY,
name VARCHAR(100));
-- Create Table to store Member information
CREATE TABLE Members(name VARCHAR(100),
sid REFERENCES Servers(sid),
optin INT,
PRIMARY KEY(name, sid));