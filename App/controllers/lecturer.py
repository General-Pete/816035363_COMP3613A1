# from App.models import lecturer
from App.models import Lecturer
from App.database import db
from sqlalchemy.exc import IntegrityError


def create_lecturer(name, faculty, employmentYear, specialty):
    newLecturer = Lecturer(name = name, faculty = faculty, employmentYear = employmentYear, specialty = specialty)
    try:
        db.session.add(newLecturer)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('Lecturer already exists.')
    else:
        print(f'{name} added to list of lecturers.')

def get_lecturer(lecturer_id):
    return Lecturer.query.get(lecturer_id)
