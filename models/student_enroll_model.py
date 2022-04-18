from sqlalchemy import Column, String, Integer, ForeignKey, and_
from sqlalchemy.ext.declarative import declarative_base
from models.subject_model import Subject
from models.student_model import Student

base = declarative_base()

class StudentEnroll(base):
    __tablename__ = 'studentenroll'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Student.student_id))
    subject_id = Column(Integer, ForeignKey(Subject.id))

    def __init__(self, id=None, student_id=None, subject_id=None):
        self.id=id
        self.student_id=student_id
        self.subject_id=subject_id


    def create(self, student_id, subject_id, transaction):

        student = StudentEnroll(student_id=student_id, subject_id=subject_id)
        transaction.add(student)
        transaction.commit()


    def get_by_StudentAdd(self,student_id, transaction):

        student = transaction.query(Subject).outerjoin(StudentEnroll, and_(Subject.id == StudentEnroll.subject_id, StudentEnroll.student_id == student_id)).filter_by(subject_id=None)
        return student

    def get_by_StudentWithdraw(self, student_id, transaction):

        student = transaction.query(Subject).join(StudentEnroll, and_(Subject.id == StudentEnroll.subject_id, StudentEnroll.student_id==student_id))
        return student



    def delete(self, student_id, subject_id, transaction):
        student = transaction.query(StudentEnroll).filter_by(student_id=student_id, subject_id=subject_id).delete()
        transaction.commit()

        return True

student_enroll = StudentEnroll()
