from App.database import db
from App.models import Course
from sqlalchemy.exc import IntegrityError


def populate_courses():
    # 20-25 UWI-style courses from various faculties without lecturer and tutor assignments
    courses = [
        # Faculty of Science and Technology
        {"name": "COMP 3607 Object Oriented Programming II", "faculty": "Faculty of Science and Technology", "semester": "Semester 1"},
        {"name": "COMP 3615 Artificial Intelligence", "faculty": "Faculty of Science and Technology", "semester": "Semester 2"},
        {"name": "MATH 2401 Advanced Calculus", "faculty": "Faculty of Science and Technology", "semester": "Semester 2"},
        {"name": "PHYS 1001 Introduction to Physics I", "faculty": "Faculty of Science and Technology", "semester": "Semester 1"},

        # Faculty of Social Sciences
        {"name": "ECON 1001 Introduction to Microeconomics", "faculty": "Faculty of Social Sciences", "semester": "Semester 1"},
        {"name": "MGMT 2001 Principles of Management", "faculty": "Faculty of Social Sciences", "semester": "Semester 2"},
        {"name": "SOCI 1002 Introduction to Sociology", "faculty": "Faculty of Social Sciences", "semester": "Semester 1"},
        {"name": "PSYC 2005 Developmental Psychology", "faculty": "Faculty of Social Sciences", "semester": "Semester 2"},

        # Faculty of Medical Sciences
        {"name": "MEDS 1010 Anatomy and Physiology I", "faculty": "Faculty of Medical Sciences", "semester": "Semester 1"},
        {"name": "MEDS 2020 Pathophysiology", "faculty": "Faculty of Medical Sciences", "semester": "Semester 2"},

        # Faculty of Humanities and Education
        {"name": "LITS 1001 Introduction to Literature", "faculty": "Faculty of Humanities and Education", "semester": "Semester 1"},
        {"name": "HIST 2003 Caribbean History", "faculty": "Faculty of Humanities and Education", "semester": "Semester 2"},
        {"name": "EDUC 1001 Foundations of Education", "faculty": "Faculty of Humanities and Education", "semester": "Semester 1"},

        # Faculty of Engineering
        {"name": "ENGR 1001 Introduction to Engineering", "faculty": "Faculty of Engineering", "semester": "Semester 1"},
        {"name": "CIVL 2001 Structural Engineering", "faculty": "Faculty of Engineering", "semester": "Semester 2"},
        {"name": "ELEC 3005 Electrical Power Systems", "faculty": "Faculty of Engineering", "semester": "Semester 2"},

        # Faculty of Law
        {"name": "LAW 2010 Law of Torts", "faculty": "Faculty of Law", "semester": "Semester 1"},
        {"name": "LAW 2020 Constitutional Law", "faculty": "Faculty of Law", "semester": "Semester 2"}
    ]

    # Add courses to the database without lecturer and tutor
    for course_data in courses:
        course = Course(
            name=course_data["name"],
            faculty=course_data["faculty"],
            semester=course_data["semester"]
        )
        db.session.add(course)

    db.session.commit()
    print("Courses populated without lecturers and tutors/TAs.")

def create_course(name, faculty, semester):
    newCourse = Course(name = name, faculty = faculty, semester = semester)
    try:
        db.session.add(newCourse)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('Course already exists.')
    else:
        print(f'{name} added to list of courses.')


def get_course(course_id):
    return Course.query.get(course_id)