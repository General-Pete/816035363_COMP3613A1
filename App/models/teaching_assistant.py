from App.database import db


class Teaching_assistant(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)               
  faculty = db.Column(db.String(255), nullable=False)
  employmentYear = db.Column(db.Integer, nullable=True)
  department = db.Column(db.String(255), nullable=True)
  assignedCourses = db.relationship('Course', secondary='course_assistants', backref=db.backref('assistant', lazy=True))

  def __init__ (self, name, faculty, employmentYear, department):
    self.name = name
    self.faculty = faculty
    self.employmentYear = employmentYear
    self.department = department

  def __repr__(self):
    return f'<TeachingAssistant: {self.name} - ID: {self.id}>'