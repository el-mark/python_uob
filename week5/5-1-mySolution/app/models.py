from app import db

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32), nullable=False, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    # CASCADE ALL
    loans = db.relationship('Loan', backref='student', lazy='dynamic', cascade='all, delete')
    # ON DELETE SET NULL
    # loans = db.relationship('Loan', backref='student', lazy='dynamic')

    def __repr__(self):
        return f"student('{self.student_id}', '{self.lastname}', '{self.firstname}' , '{self.email}')"

class Loan(db.Model):
    __tablename__ = 'loans'
    loan_id = db.Column(db.Integer, primary_key=True)
    # CASCADE ALL
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    # ON DELETE SET NULL
    # student_id = db.Column(db.Integer, db.ForeignKey('students.student_id', ondelete="SET NULL"))
    device_id = db.Column(db.Integer, nullable=False)
    borrow_datetime = db.Column(db.DateTime, nullable=False)
    return_datetime = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"loan('{self.device_id}', '{self.borrow_datetime}' , '{self.return_datetime}', '{self.student}')"


