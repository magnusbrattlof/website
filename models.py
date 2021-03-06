from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), index=True, unique=True)
    os = db.Column(db.String(120), index=True, unique=False)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
