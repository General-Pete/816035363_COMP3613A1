from App.models import Tutor
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_tutor(name, faculty, employmentYear, department):
    newTutor = Tutor(name = name, faculty = faculty, employmentYear = employmentYear, department= department)
    try:
        db.session.add(newTutor)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('Tutor already exists.')
    else:
        print(f'{name} added to list of tutors.')

def get_tutor(tutor_id):
    return Tutor.query.get(tutor_id)