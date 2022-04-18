from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.subject_model import Subject

base = declarative_base()


class Student(base):
    __tablename__ = 'student'
    student_first =  Column(String)
    student_last = Column(String)
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    role = Column(String)



    def _init_(self, student_id=None, student_first=None,student_last = None, email = None, role=None):
        self.student_id = student_id
        self.student_first = student_first
        self.student_last = student_last
        self.email = email
        self.role= role

    def create(self, student_first, student_last, email, role, transaction):

        student = Student(student_first=student_first, student_last=student_last, email=email, role=role)
        transaction.add(student)
        transaction.commit()




    def get_by_StudentEmail(self, email, transaction):
        student = transaction.query(Student).filter_by(email=email)
        return student


    def get_by_StudentId(self, student_id, email,transaction):
        student = transaction.query(Student).filter_by(student_id=student_id, email=email)
        return student





    def update_by_StudentId(self,student_id, student_first, student_last, email,role, transaction):

        student = transaction.query(Student).filter_by(student_id=student_id).first()
        student.student_first = student_first
        student.student_last = student_last
        student.email= email
        student.role = role

        transaction.commit()

        return True



    def delete_by_StudentId(self, student_id, transaction):
        student = transaction.query(Student).filter_by(student_id=student_id)
        transaction.delete(student)
        transaction.commit()

        return True



student = Student()


