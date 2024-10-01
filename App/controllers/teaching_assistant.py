from App.models import Teaching_assistant
from App.database import db
from sqlalchemy.exc import IntegrityError


def create_teaching_assistant(name, faculty, employmentYear, department):
    newTA = Teaching_assistant(name = name, faculty = faculty, employmentYear = employmentYear, department= department)
    try:
        db.session.add(newTA)
        db.session.commit()
    except InterityError as e:                     
        db.session.rollback()
        print('TA already exists.')               
    else:
        # print(newTA.id)                   #for debugging - to remove
        print(f'{name} added to list of TAs.')
    
    
def get_ta(ta_id):
    return Teaching_assistant.query.get(ta_id)    

def list_all_tas():
    tas = Teaching_assistant.query.all()
    if tas:
        for ta in tas:
            print(f"TA ID: {ta.id}, Name: {ta.name}")
    else:
        print("No Teaching Assistants found.")
