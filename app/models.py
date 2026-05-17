from .extensions import db
from datetime import date

class users(db.Model):
    UserID = db.Column(db.String(50), primary_key=True)
    UserName = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(200), nullable=False)
    PhoneNum = db.Column(db.String(50), nullable=False)
    JoinDate = db.Column(db.Date, nullable=False)

    assignments = db.relationship('a_status', backref='user', cascade='all, delete')
    teams = db.relationship('team_mem', backref='user', cascade='all, delete')
    
    def __repr__(self):
        return f"<User: {self.UserName}>"
    

class a_details(db.Model):
    TaskID = db.Column(db.String(50), primary_key=True)
    TaskName = db.Column(db.String(100), nullable=False)
    TaskDesc = db.Column(db.String(300), nullable=False)

    status = db.relationship('a_status', backref='assignment', cascade='all, delete')

    def __repr__(self):
        return f"<Task: {self.TaskName}>"
    

class a_status(db.Model):
    TaskID = db.Column(db.String(50), db.ForeignKey('a_details.TaskID'), primary_key=True)
    UserID = db.Column(db.String(50), db.ForeignKey('users.UserID'), primary_key=True)
    isComplete = db.Column(db.String(50), nullable=False)
    DueDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Status: {self.TaskID} for User {self.UserID}>"
    

class team_det(db.Model):
    TeamID = db.Column(db.String(50), primary_key=True)
    TeamName = db.Column(db.String(80), nullable=False)

    members = db.relationship('team_mem', backref='team', cascade='all, delete')

    def __repr__(self):
        return f"<Team: {self.TeamName}>"
    

class team_mem(db.Model):
    TeamID = db.Column(db.String(50), db.ForeignKey('team_det.TeamID'), primary_key=True)
    UserID = db.Column(db.String(50), db.ForeignKey('users.UserID'), primary_key=True)
    TeamJoinDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Team Member: User {self.UserID} in Team {self.TeamID}>"
    
