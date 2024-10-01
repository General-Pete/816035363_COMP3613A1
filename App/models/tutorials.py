from App.database import db

class Tutorials(db.Model):
  __tablename__ ='tutorial'
  id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
  tutor_id = db.Column(db.Integer,db.ForeignKey('tutor.id'))