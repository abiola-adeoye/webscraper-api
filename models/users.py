from db import db

class UsersModel(db.Model):
    __tablename__ = "users"

    uuid = db.Column("uuid", db.String(50), primary_key=True)
    email = db.Column("email", db.String(100), nullable=False)
    first_name = db.Column("first_name", db.String(50))
    last_name = db.Column("last_name", db.String(50))
    username = db.Column("username", db.String(50), nullable=False, unique=True)
    date = db.Column("date", db.DateTime)

    def find_by_username(self):
        pass