from flask_restful import Resource
from flask import Flask, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import DATABASE_URL
from models.student_model import student

app = Flask(__name__)
db = create_engine(DATABASE_URL)
Session = sessionmaker(db)

class StudentApi(Resource):
    def post(self):

        session = Session()
        body = request.json

        student_id = body.get('Sid')
        student_first = body.get('FirstName')
        student_last = body.get('LastName')
        email = body.get('Email')
        role = body.get('Role')


        try:
            student.create(student_first = student_first, student_last=student_last, email=email,role = role, transaction=session)
            return make_response({'message': 'Done'}, 200)
        except:
            return make_response({'Error' : 'Id or email already exist'}, 205)
        finally:
            session.close()


    def get(self):
        session = Session()
        args = request.args

        if 'Sid' in args:
            Student = student.get_by_StudentId(student_id=args.get('Sid'), email=args.get('email'),transaction=session)

        session.close()

        result = dict()

        for item in Student:
            result.update({'FirstName': item.student_first,'LastName' : item.student_last,'Sid': item.student_id, 'Email': item.email, 'Role': item.role})

        header = dict()
        header['Access-Control-Allow-Origin'] = '*'
        try:
            if len(result) == 0:
                return make_response({'Error' : 'Id or name not found'}, 204)
            else:
                response = make_response(result, 200)
                response.headers = header
                return response
        except:
            return make_response({'Error' : 'No Result Found'})


    def put(self):
        session = Session()
        args = request.args
        data = request.get_json()


        try:
            if 'Sid' in args:
                update_student = student.update_by_id(student_id=args.get('Sid'), student_first=data.get('FirstName'), student_last=data.get('LastName'),email=data.get('Email'),role=data.get('Role'),transaction=session)
                return make_response({'Result:': update_student}, 200)
        except:
            return make_response({'Error': 'Id not found'}, 204)


        session.close()




    def delete(self):

        session = Session()
        args = request.args

        try:
            if 'Sid' in args:
                delete_student = student.delete_by_id(student_id = args.get('Sid'), transaction=session)
                return make_response({'Result': delete_student}, 200)
        except:
            return make_response({'Error': 'Id not found'}, 204)
        finally:
            session.close()
