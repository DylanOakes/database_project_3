-- ==========================================
-- PROJECT 3: FINAL DATABASE SCHEMA (3NF)
-- ==========================================

-- Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNum VARCHAR(20),
    JoinDate DATE NOT NULL
);

-- Assignment Details Table
CREATE TABLE AssignmentDetails (
    TaskID INT PRIMARY KEY,
    TaskName VARCHAR(255) NOT NULL,
    TaskDesc VARCHAR(500)
);

-- Assignment Status Table
CREATE TABLE AssignmentStatus (
    TaskID INT,
    UserID INT,
    IsComplete VARCHAR(50),
    DueDate DATE,
    PRIMARY KEY (TaskID, UserID),
    FOREIGN KEY (TaskID) REFERENCES AssignmentDetails(TaskID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Team Details Table
CREATE TABLE TeamDetails (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(100) NOT NULL
);

-- Team Membership Table
CREATE TABLE TeamMembership (
    TeamID INT,
    UserID INT,
    TeamJoinDate DATE,
    PRIMARY KEY (TeamID, UserID),
    FOREIGN KEY (TeamID) REFERENCES TeamDetails(TeamID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);