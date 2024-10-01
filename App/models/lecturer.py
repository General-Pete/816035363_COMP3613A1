from App.database import db

class Lecturer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  faculty = db.Column(db.String(255), nullable=False)
  employmentYear = db.Column(db.Integer, nullable=False)
  specialty = db.Column(db.String(255), nullable=False)
  assignedCourses = db.relationship('Course', backref=db.backref('assigned_lecturer', lazy=True))

  def __init__ (self, name, faculty, employmentYear, specialty):
    self.name = name
    self.faculty = faculty
    self.employmentYear = employmentYear
    self.specialty = specialty

  def __repr__(self):
    return f'<Lecturer: {self.name} - ID: {self.id}>'
