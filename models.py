from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
    db.app = app
    db.init_app(app)


# # MODELS GO BELOW!
class User(db.Model):
    """Site user."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True) 

    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)   

    image_url = db.Column(db.String, 
                    nullable=True,
                    unique=True,
                    default=DEFAULT_IMAGE_URL)  

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"   

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)                     