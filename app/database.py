import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS users(UserID TEXT PRIMARY KEY," \
    "UserName TEXT," \
    "email TEXT," \
    "PhoneNum TEXT," \
    "JoinDate DATE)" \
)

con.commit()

cur.execute(
    "CREATE TABLE IF NOT EXISTS a_details(TaskID TEXT PRIMARY KEY," \
    "TaskName TEXT," \
    "TaskDesc TEXT)" \
)

con.commit()

cur.execute(
    "CREATE TABLE IF NOT EXISTS a_status(TaskID TEXT," \
    "UserID TEXT," \
    "isComplete TEXT," \
    "DueDate DATE," \
    "FOREIGN KEY (TaskID) REFERENCES a_details(TaskID)," \
    "FOREIGN KEY(UserID) REFERENCES users(UserID)," \
    "PRIMARY KEY(TaskID, UserID))" \
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS team_det(TeamID TEXT PRIMARY KEY," \
    "TeamName TEXT)" \
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS team_mem(TeamID TEXT," \
    "UserID TEXT," \
    "TeamJoinDate DATE," \
    "FOREIGN KEY(TeamID) REFERENCES team_det(TeamID)," \
    "FOREIGN KEY(UserID) REFERENCES users(UserID)," \
    "PRIMARY KEY(TeamID, UserID))" \
)

cur.execute("""
    INSERT INTO users VALUES
        ('101', 'Dylan', 'dhoakes@shockers.wichita.edu', '316-641-XXXX', '2025-01-21'),
        ('102', 'Michael', 'michael@shockers.wichita.edu', '316-235-XXXX', '2025-02-12'),
        ('103', 'Ashdon', 'ashdon@shockers.wichita.edu', '316-932-XXXX', '2026-06-28'),
        ('104', 'Bob', 'b.smith78@provider.net', '215-123-XXXX', '2023-09-19'),
        ('105', 'Alice', 'alice.johnson@example.com', '123-456-XXXX', '2020-10-13'),
        ('106', 'Dave', 'myemail@site.com', '152-923-XXXX', '2021-05-19')       
""")

cur.execute("""
    INSERT INTO a_details VALUES        
        ('12345', 'Project 2', 'Create tables.'),
        ('40158', 'Weak 10 Report', 'Document your weekly proccess'),
        ('98324', 'Exam 2 Review', 'Submit your work via screenshot'),
        ('42403', 'Artist Date', 'Submit your reflection and pictures'),
        ('32120', 'Gantt Chart', 'Submit your chart as an Excel sheet'),
        ('09876', 'Formal Logic Ch.7 Exercises', 'Submit your work via screenshot') 
""")

cur.execute("""
    INSERT INTO a_status VALUES
        ('12345', '101', 'In Progress', '2026-04-12'),
        ('40158', '102', 'Submitted', '2026-04-05'),
        ('98324', '103', 'Late', '2026-03-28'),
        ('42403', '104', 'In Progress', '2026-04-19'),
        ('32120', '105', 'Submitted', '2026-02-20'),
        ('09876', '101', 'In Progress', '2026-04-21')      
""")


cur.execute("""
    INSERT INTO team_det VALUES
        ('0912', 'Squadro Pamodoro'),
        ('2398', 'Art Club'),
        ('9842', 'WuLug')
""")

cur.execute("""
    INSERT INTO team_mem VALUES
        ('0912', '101', '2026-01-23'),
        ('0912', '102', '2026-01-23'),
        ('0912', '103', '2026-01-23'),
        ('2398', '104', '2024-08-19'),
        ('9842', '105', '2025-03-11')
""")