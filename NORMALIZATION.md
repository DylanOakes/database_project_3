# Project 2 - Database

## Users Table

| UserID (PK, FK) | UserName | Email | PhoneNum | JoinDate |
|--------|----------|-------|----------|-----------|
| 101 | Dylan | dhoakes@shockers.wichita.edu | 316-641-XXXX | 2025-01-21 |
| 102 | Michael | michael@shockers.wichita.edu | 316-235-XXXX | 2025-02-12 |
| 103 | Ashdon | ashdon@shockers.wichita.edu | 316-932-XXXX | 2026-06-28 |
| 104 | Bob | b.smith78@provider.net | 215-123-XXXX | 2023-09-19 |
| 105 | Alice | alice.johnson@example.com | 123-456-XXXX | 2020-10-13 |
| 106 | Dave | myemail@site.com | 152-923-XXXX | 2021-05-19 |

### Users Functional Dependencies & Anomalies
UserID --> Everything else
No need to check if it is in 1NF because the table doesn't have a composite key.
Already in 3rd Normal Form
An insertion anomaly occurs if an entry is added with UserID set to null as a user must be assigned a UserID.

---

## Assignments Table (1NF)

| TaskID (PK, FK) | UserID (PK, FK) | TaskName | TaskDesc | IsComplete | DueDate |
|--------|--------|-----------|-----------|-------------|----------|
| 12345 | 101 | Project 2 | Create tables. | In Progress | 2026-04-12 |
| 40158 | 102 | Weak 10 Report | Document your weekly proccess | Submitted | 2026-04-05 |
| 98324 | 103 | Exam 2 Review | Submit your work via screenshot | Late | 2026-03-28 |
| 42403 | 104 | Artist Date | Submit your reflection and pictures | In Progress | 2026-04-19 |
| 32120 | 105 | Gantt Chart | Submit your chart as an Excel sheet | Submitted | 2026-02-20 |
| 09876 | 101 | Formal Logic Ch.7 Exercises | Submit your work via screenshot | In Progress | 2026-04-21 |

### Assignments Functional Dependencies & Anomalies
PK --> Everything else
TaskID --> TaskName, TaskDesc
    *Violates 2NF because TaskName and TaskDesc only depends on TaskID

---

# Updated Assignment Tables

## Assignment Status Table (2NF / 3NF)

| TaskID (PK, FK) | UserID (PK, FK) | IsComplete | DueDate |
|--------|--------|-------------|----------|
| 12345 | 101 | In Progress | 2026-04-12 |
| 40158 | 102 | Submitted | 2026-04-05 |
| 98324 | 103 | Late | 2026-03-28 |
| 42403 | 104 | In Progress | 2026-04-19 |
| 32120 | 105 | Submitted | 2026-02-20 |
| 09876 | 101 | In Progress | 2026-04-21 |

### Assignment Status Functional Dependencies
PK --> Everything else
No transitive dependencies exist so it is already in 3NF form


## Assignment Details Table

| TaskID (PK, FK) | TaskName | TaskDesc |
|--------|-----------|-----------|
| 12345 | Project 2 | Create tables. |
| 40158 | Weak 10 Report | Document your weekly proccess |
| 98324 | Exam 2 Review | Submit your work via screenshot |
| 42403 | Artist Date | Submit your reflection and pictures |
| 32120 | Gantt Chart | Submit your chart as an Excel sheet |
| 09876 | Formal Logic Ch.7 Exercises | Submit your work via screenshot |

### Assignment Details Functional Dependencies
PK --> Everything else
No transitive dependencies exist, so it is already in 3NF form.

---

## Teams Table

| TeamID (PK) | UserID (PK, FK) | TeamName | TeamJoinDate |
|--------|--------|-----------|---------------|
| 0912 | 101 | Squadro Pamodoro | 2026-01-23 |
| 0912 | 102 | Squadro Pamodoro | 2026-01-23 |
| 0912 | 103 | Squadro Pamodoro | 2026-01-23 |
| 2398 | 104 | Art Club | 2024-08-19 |
| 9842 | 105 | WuLug | 2025-03-11 |

### Teams Functional Dependencies
TeamID, UserID --> Everything Else
TeamID --> TeamName
    *Violates 2NF because TeamName only depends on TeamID

---

# Updated Teams Tables

## Team Membership Table (2NF / 3NF)

| TeamID (PK, FK) | UserID (PK, FK) | TeamJoinDate |
|--------|--------|---------------|
| 0912 | 101 | 2026-01-23 |
| 0912 | 102 | 2026-01-23 |
| 0912 | 103 | 2026-01-23 |
| 2398 | 104 | 2024-08-19 |
| 9842 | 105 | 2025-03-11 |

### Team Membership Functional Dependencies
PK --> Everything else
No transitive dependencies exist, so it is already in 3NF form.

## Team Details Table (2NF / 3NF)

| TeamID (PK, FK) | TeamName |
|--------|-----------|
| 0912 | Squadro Pamodoro |
| 2398 | Art Club |
| 9842 | WuLug |

### Team Details Functional Dependencies (2NF / 3NF)
PK --> Everything else
No transitive dependencies exist, so it is already in 3NF form.

---