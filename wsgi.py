import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from sqlalchemy.exc import IntegrityError

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)

from App.controllers.course import *
from App.controllers.lecturer import *
from App.controllers.tutor import *
from App.controllers.teaching_assistant import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)









#ADDED COMMANDS HERE 










#CREATE

create_cli = AppGroup('create', help = 'Commands: course, lecturer, ta, tutor')

@create_cli.command("course", help="Parameters: name faculty semester")
@click.argument('name')
@click.argument('faculty')
@click.argument('semester')
def create_new_course(name, faculty, semester):
    create_course(name = name, faculty = faculty, semester = semester)

@create_cli.command("lecturer", help="")
@click.argument('name')
@click.argument('faculty')
@click.argument('employmentyear')
@click.argument('specialty')
def create_new_lecturer(name, faculty, employmentyear, specialty):
    create_lecturer(name, faculty, employmentyear, specialty)

@create_cli.command("tutor", help="")
@click.argument('name')
@click.argument('faculty')
@click.argument('department')
@click.argument('employmentyear')
def create_new_tutor(name, faculty, employmentyear, department):
    create_tutor(name = name, faculty = faculty, employmentYear = employmentyear, department = department)


@create_cli.command("ta", help="")
@click.argument('name')
@click.argument('faculty')
@click.argument('department')
@click.argument('employmentyear')
def create_new_ta(name, faculty, employmentyear, department):
    create_teaching_assistant(name = name, faculty = faculty, employmentYear = employmentyear, department = department)

app.cli.add_command(create_cli) # add the group to the cli





#ASSIGN

assign_cli = AppGroup('assign', help = 'Add staff to courses')

@assign_cli.command("lecturer", help="")
@click.argument('lecturer_id')
@click.argument('course_id')
def create_new_course(lecturer_id, course_id):
    lecturer = get_lecturer(lecturer_id=lecturer_id)
    course = get_course(course_id=course_id)
    
    if course is None:
        print(f"Error: Course with ID {course_id} not found.")
        return
    
    if lecturer is None:
        print(f"Error: Lecturer with ID {lecturer_id} not found.")
        return

    try:
        course.assigned_lecturer = lecturer # Assign the lecturer to the course using the relationship
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(f"Error occurred while assigning lecturer: {str(e)}")
    else:
        print(f"Lecturer {lecturer.name} assigned to course {course.name}.")


@assign_cli.command("tutor", help="Parameters : tutor_id course_id")
@click.argument('tutor_id')
@click.argument('course_id')
def create_new_course(tutor_id, course_id):
    tutor = get_tutor(tutor_id=tutor_id)
    course = get_course(course_id=course_id)
    
    if course is None:
        print(f"Error: Course with ID {course_id} not found.")
        return
    
    if tutor is None:
        print(f"Error: Tutor with ID {tutor_id} not found.")
        return

    try:
        course.assigned_tutor.append(tutor)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(f"Error occurred while assigning tutor: {str(e)}")
    else:
        print(f"Tutor {tutor.name} assigned to course {course.name}.")


@assign_cli.command("ta", help="Parameters : tutor_id course_id")
@click.argument('ta_id')
@click.argument('course_id')
def assign_new_ta(ta_id, course_id):
    ta = get_ta(ta_id)
    course = get_course(course_id=course_id)
    
    if course is None:
        print(f"Error: Course with ID {course_id} not found.")
        return
    
    if ta is None:
        print(f"Error: TA with ID {ta_id} not found.")
        return

    try:
        course.assistant.append(ta)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(f"Error occurred while assigning TA: {str(e)}")
    else:
        print(f"Tutor {ta.name} assigned to course {course.name}.")


app.cli.add_command(assign_cli)





#VIEW

view_cli = AppGroup('view', help = 'View data')

@view_cli.command("courses", help="Displays all courses in the database")
def view_courses():
    try:
        # Fetch all courses from the database
        courses = Course.query.all()

        # Check if there are any courses
        if not courses:
            print("No courses available in the database.")
            return

        # Print each course using its __repr__ method
        for course in courses:
            print(course)

    except IntegrityError as e:
        print(f"Error occurred while fetching courses: {str(e)}")

@view_cli.command("staff", help="Displays all staff assigned to any course in the database. Paremters: course_id")
@click.argument('course_id')
def view_staffs(course_id):
    try:
        # Fetch all courses from the database
        course = Course.query.get(course_id)

        # Check if there are any courses
        if not course:
            print("Invalid course.")
            return

        # Print each course using its __repr__ method
        print(f'Course: {course}')

        lecturer_info = f"Lecturer Info: {course.assigned_lecturer}" if course.assigned_lecturer else "No lecturer assigned"
        print(lecturer_info)

        tutor_info = f"Tutor Info: {course.assigned_tutor}" if course.assigned_tutor else "No tutor assigned"
        print(tutor_info)

        ta_info = f"TA Info: {course.assistant}" if course.assistant else "No TA assigned"
        print(ta_info)

    except IntegrityError as e:
        print(f"Error occurred while fetching course: {str(e)}")

app.cli.add_command(view_cli)