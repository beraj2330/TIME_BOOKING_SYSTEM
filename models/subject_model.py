from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Subject(base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def _init_(self, id=None, name=None):
        self.id = id
        self.name = name

    def create(self, id, name, transaction):

        subject = Subject(id=id, name=name)
        transaction.add(subject)
        transaction.commit()


    def get_by_name(self, name, transaction):
        subjects = transaction.query(Subject).filter_by(name=name)
        return subjects

    def get_by_id(self, id, transaction):
        subjects = transaction.query(Subject).filter_by(id=id)
        return subjects

    def update_by_id(self,id, name, transaction):

        subject = transaction.query(Subject).filter_by(id=id).first()
        subject.name = name

        transaction.commit()

        return True

    def delete_by_id(self, id, transaction):
        subject = transaction.query(Subject).filter_by(id=id).one()
        transaction.delete(subject)
        transaction.commit()

        return True





subject = Subject()


