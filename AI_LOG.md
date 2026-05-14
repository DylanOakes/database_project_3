# Usage 1
## I used ChatGPT to convert the tables I created for Project 2 to be suitable for the normalization markdown file.

---

## Prompts Used:
make table in a markdown file from the following code.
CREATE TABLE Users (
    UserID VARCHAR(50) PRIMARY KEY,
    UserName VARCHAR(100),
    Email VARCHAR(100), -- Unique constraint not applied here because it will be added in DML
    PhoneNum VARCHAR(50),
    JoinDate DATE -- Metadata that describes when the user join
);

-- This table stores information regarding assignments assigned to users
CREATE TABLE Assignments (
    TaskID VARCHAR(50),
    UserID VARCHAR(50),
    TaskName VARCHAR(100),
    TaskDesc VARCHAR(200),
    IsComplete VARCHAR(50), -- Metadata that describes the task's submission status
    DueDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    PRIMARY KEY (TaskID, UserID)
);

-- This table stores information regarding teams certain users are assigned to
CREATE TABLE Teams (
    TeamID VARCHAR(50),
    UserID VARCHAR(50),
    TeamName VARCHAR(50),
    TeamJoinDate DATE, -- Metadata that describes when a team was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    PRIMARY KEY (TeamID, UserID)
);
---
From the table above fill it with the following entries
INSERT INTO Users(UserID, UserName, Email, PhoneNum, JoinDate) VALUES
('101', 'Dylan', 'dhoakes@shockers.wichita.edu', '316-641-XXXX', '2025-01-21'),
('102', 'Michael', 'michael@shockers.wichita.edu', '316-235-XXXX', '2025-02-12'),
('103', 'Ashdon', 'ashdon@shockers.wichita.edu', '316-932-XXXX', '2026-06-28'),
('104', 'Bob', 'b.smith78@provider.net', '215-123-XXXX', '2023-09-19'),
('105', 'Alice', 'alice.johnson@example.com', '123-456-XXXX', '2020-10-13'),
('106', 'Dave', 'myemail@site.com', '152-923-XXXX', '2021-05-19');

-- Fills the Assignments table with data
INSERT INTO Assignments(TaskID, UserID, TaskName, TaskDesc, IsComplete, DueDate) VALUES
('12345', '101', 'Project 2', 'Create tables.', 'In Progress', '2026-04-12'),
('40158', '102', 'Weak 10 Report', 'Document your weekly proccess', 'Submitted', '2026-04-05'),
('98324', '103', 'Exam 2 Review', 'Submit your work via screenshot', 'Late', '2026-03-28'),
('42403', '104', 'Artist Date', 'Submit your reflection and pictures', 'In Progress', '2026-04-19'),
('32120', '105', 'Gantt Chart', 'Submit your chart as an Excel sheet', 'Submitted', '2026-02-20'),
('09876', '101', 'Formal Logic Ch.7 Exercises', 'Submit your work via screenshot', 'In Progress', '2026-04-21');

-- Fills the Teams table with data
INSERT INTO Teams(TeamID, UserID, TeamName, TeamJoinDate) VALUES
('0912', '101', 'Squadro Pamodoro', '2026-01-23'),
('0912', '102', 'Squadro Pamodoro', '2026-01-23'),
('0912', '103', 'Squadro Pamodoro', '2026-01-23'),
('2398', '104', 'Art Club', '2024-08-19'),
('9842', '105', 'WuLug', '2025-03-11');
---
For the teams assignments table above, split it into two tables. For table 1, remove TaskName and TaskDesc. For table 2, only have TaskID, TaskName, and TaskDesc.
---
For the teams table above, split it into two tables. For table 1, remove TeamName. For table 2, only have TeamID and TeamName

---

## AI Output:
To prevent this file from getting too long, I'll just say the table found in NORMALIZATION.md are exactly the same as the ones provided by ChatGPT.

---

## My Modifification:
Everything else done in the normalization report was done by me.
In the tables, I added labels to the Primary and Foreign Keys
I was able to determine all of the functional dependencies by myself and decompose all tables into 3NF.

---