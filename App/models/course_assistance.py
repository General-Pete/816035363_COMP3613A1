from App.database import db

class CourseAssistance(db.Model):
  __tablename__ ='course_assistants'
  id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
  ta_id = db.Column(db.Integer,db.ForeignKey('teaching_assistant.id'))