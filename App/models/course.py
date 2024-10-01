from App.database import db

class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  faculty = db.Column(db.String(255), nullable=False)
  semester = db.Column(db.String(255), nullable=False)
  lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable=True)
  # tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable = True)
  
  # teachingAssistant = db.Column(db.String(255), nullable=True)      #check to see if needed
  # assignedTutor = db.relationship('Tutor', backref=db.backref('assigned_course', lazy=True))

  def __init__ (self, name, faculty, semester):
    self.name = name
    self.faculty = faculty
    self.semester = semester

  def __repr__(self):
  
    return f'<Course ID: {self.id}, Name: {self.name}, Faculty: {self.faculty}, Semester: {self.semester}>'
