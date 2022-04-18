from flask_restful import Resource
from flask import Flask, request, make_response
from flask_cors import cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import DATABASE_URL
from models.student_enroll_model import student_enroll

app = Flask(__name__)
db = create_engine(DATABASE_URL)
Session = sessionmaker(db)

class StudentEnrollApi(Resource):

    def post(self):

        session = Session()
        body = request.json

        student_id = body.get('SId')
        subject_id = body.get('SubId')

        try:
            for i in range(len(subject_id)):
                student_enroll.create(student_id=student_id, subject_id=subject_id[i], transaction=session)
            response = make_response({'Message': 'Done'}, 200)
            return response
        except:
            response = make_response({'Message' : 'Enrolled in all Courses.'}, 200)
            return response
        finally:
            session.close()


    def get(self):
        session = Session()
        args = request.args
        action = args.get('Action')
        result = list()

        # if action is enrolled
        if action == 'enroll':
            Student = student_enroll.get_by_StudentAdd(student_id=args.get('id'), transaction=session)

            for item in Student:
                result.append({'id' : item.id, 'name' : item.name})

            header = dict()
            header['Access-Control-Allow-Origin'] = '*'
            try:
                if not result:
                    return make_response({'Error': 'Already Enrolled In all Courses.'}, 200)
                else:
                    response = make_response({'Result': result}, 200)
                    response.headers = header
                    return response
            except:
                return make_response({'Message': 'No Content'}, 204)
            finally:
                session.close()

        # if action is withdraw
        else:
            Student = student_enroll.get_by_StudentWithdraw(student_id=args.get('id'), transaction=session)

            for item in Student:
                result.append({'id' : item.id, 'name' : item.name})

            header = dict()
            header['Access-Control-Allow-Origin'] = '*'
            try:
                if not result:
                    return make_response({'Error': 'Not Enrolled in any Course.'}, 200)
                else:
                    response = make_response({'Result': result}, 200)
                    response.headers = header
                    return response
            except:
                return make_response({'Message': 'No Content'}, 204)
            finally:
                session.close()

    def delete(self):

        session = Session()
        body = request.json

        students_id = body.get('SId')
        subjects_id = body.get('SubId')



        try:
            for i in range(len(subjects_id)):
                delete_student = student_enroll.delete(student_id=students_id,subject_id=subjects_id[i], transaction=session)

            response = make_response(200)

            return response
        except:
            response = make_response({'Error': 'Not Enrolled in the Course.'}, 200)
            return response
        finally:
            session.close()
