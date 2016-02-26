from . import db

class User(db.Model):
    userid    = db.Column(db.String(9), primary_key=True)
    username  = db.Column(db.String(30), unique=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname  = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(30), nullable=False)
    sex   = db.Column(db.String(6), nullable=False)
    age   = db.Column(db.Integer, nullable=False)
    profile_added_on = db.Column(db.DateTime, nullable=False)
    high_score  = db.Column(db.Integer, nullable=False, default=0)
    tdollars    = db.Column(db.Integer, nullable=False, default=0)
    

    def __init__(self, userid, username, firstname, lastname, image, sex, age, profile_added_on, high_score, tdollars):
        
        self.userid   = userid
        self.username = username
        self.firstname  = firstname
        self.lastname = lastname
        self.image  = image
        self.sex    = sex
        self.age    = age
        self.profile_added_on = profile_added_on
        self.high_score = high_score
        self.tdollars   = tdollars

    def __repr__(self):
        return'<User %r>' % self.username