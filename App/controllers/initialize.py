from .user import create_user
from .course import populate_courses
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    populate_courses()    #populate courses with data - all unassigned to any staff
