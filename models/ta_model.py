from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.subject_model import Subject
from models.student_model import Student

base = declarative_base()


class Ta(base):

    # necessary information about database
    __tablename__ = 'ta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ta_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey(Subject.id))


    # constructor created
    def _init_(self, ta_id=None, id=None, subject_id=None):
        self.ta_id = ta_id
        self.id = id
        self.subject_id = subject_id

    # creating table name ta
    def create(self, ta_id, subject_id, transaction):
        Ta = ta(student_id=ta_id, subject_id=subject_id)
        transaction.add(Ta)
        transaction.commit()


    # get method to return information requested
    def get_by_TaWithdraw(self, ta_id, transaction):
        withdraw = transaction.query(Ta).filter_by(ta_id=ta_id)
        return withdraw


    # deleting a specific row by id
    def delete(self, ta_id, subject_id, transaction):
        withdraw = transaction.query(Ta).filter_by(ta_id=ta_id, subject_id=subject_id).delete()
        transaction.commit()
        return True

# created object of class Ta
ta = Ta()


