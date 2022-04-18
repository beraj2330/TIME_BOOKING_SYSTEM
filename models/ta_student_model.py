from sqlalchemy import Column, String, Integer, ForeignKey, and_
from sqlalchemy.ext.declarative import declarative_base
from models.subject_model import Subject
from models.ta_model import Ta
from models.student_model import Student


base = declarative_base()


class TaStudent(base):

    # necessary information about database
    __tablename__ = 'tastudent'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    ta_id = Column(Integer, ForeignKey(Ta.ta_id))
    ta_email = Column(String, ForeignKey(Ta.email))
    student_id = Column(Integer, ForeignKey(Student.student_id))
    student_email = Column(String, ForeignKey(Student.email))
    ta_subject_id = Column(Integer, ForeignKey(Subject.id))
    ta_subject_name = Column(String, ForeignKey(Subject.name))
    student_subject_id = Column(Integer, ForeignKey(Subject.id))
    student_subject_name = Column(String, ForeignKey(Subject.name))


    # constructor created
    def _init_(self, id=None, email=None, ta_id=None, ta_email=None, student_id = None, student_email=None, ta_subject_id=None, ta_subject_name = None, student_subject_id=None, student_subject_name = None):

        self.id = id
        self.email = email
        self.ta_id = ta_id
        self.ta_email = ta_email
        self.ta_subject_id = ta_subject_id
        self.ta_subject_name = ta_subject_name
        self.student_id = student_id
        self.student_email = student_email
        self.student_subject_id = student_subject_id
        self.student_subject_name = student_subject_name


    # creating table name ta
    def createTA(self, id, email, ta_id, ta_email, ta_subject_id, ta_subject_name, transaction):

        taStudent = TaStudent(id=id, email= email, ta_id=ta_id, ta_email=ta_email, ta_subject_id=ta_subject_id, ta_subject_name=ta_subject_name)
        transaction.add(taStudent)
        transaction.commit()


    def createSTUDENT(self, id, email, student_id, student_email, student_subject_id, student_subject_name, transaction):

        taStudent = TaStudent(id=id, email= email, student_id=student_id,student_email=student_email,student_subject_id=student_subject_id,student_subject_name=student_subject_name)
        transaction.add(taStudent)
        transaction.commit()

    def createTa(self, id, ta_id, ta_email, ta_subject_id, ta_subject_name, transaction):

        taStudent = TaStudent(id=id, ta_id=ta_id, ta_email=ta_email, ta_subject_id=ta_subject_id, ta_subject_name=ta_subject_name)
        transaction.add(taStudent)
        transaction.commit()

    def createStudent(self,id, student_id, student_email, student_subject_id, student_subject_name, transaction):

        taStudent = TaStudent(id = id,student_id=student_id, student_email=student_email, student_subject_id=student_subject_id, student_subject_name=student_subject_name)
        transaction.add(taStudent)
        transaction.commit()





    # get method to return information requested
    def get_by_email(self, email, transaction):
        taStudent = transaction.query(TaStudent).filter_by(email=email)
        return taStudent

    def get_by_id(self, id, transaction):
        taStudent = transaction.query(TaStudent).filter_by(id=id)
        return taStudent

    def get_by_STUDENTid(self, student_id, student_subject_id, transaction):
        taStudent = transaction.query(TaStudent).filter_by(and_(student_id=student_id, student_subject_id=student_subject_id))
        return taStudent

    def get_by_STUDENTemail(self, student_email, student_subject_id,transaction):
        # print("5")
        taStudent = transaction.query(TaStudent).filter(TaStudent.student_email==student_email,TaStudent.student_subject_id==student_subject_id)
        # print("6")
        return taStudent




    # deleting a specific row by id
    def delete_by_TaId(self, ta_id, ta_subject_id,ta_subject_name, transaction):
        taStudent = transaction.query(TaStudent).filter_by(ta_id=ta_id, ta_subject_id=ta_subject_id, ta_subject_name =ta_subject_name).one()
        transaction.delete(taStudent)
        transaction.commit()
        return True

    def delete_by_StudentId(self,id, transaction):
        print("8")
        taStudent = transaction.query(TaStudent).filter_by(id=id).one()
        print("9")
        # student_subject_id, student_subject_name,
        transaction.delete(taStudent)
        print("10")
        transaction.commit()
        print("11")
        return True
        # , student_subject_id = student_subject_id, student_subject_name = student_subject_name



    def delete_by_TaEmail(self, ta_email, ta_subject_id,ta_subject_name, transaction):
        taStudent = transaction.query(TaStudent).filter_by(ta_email=ta_email, ta_subject_id=ta_subject_id, ta_subject_name =ta_subject_name).one()
        transaction.delete(taStudent)
        transaction.commit()
        return True

    def delete_by_StudentEmail(self,student_email, transaction):
        taStudent = transaction.query(TaStudent).filter_by(student_email=student_email).one()
        transaction.delete(taStudent)
        transaction.commit()
        return True


# created object of class TaStudent
taStudent = TaStudent()


