from flask_restful import Resource
from flask import Flask, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import DATABASE_URL
from models.subject_model import subject

app = Flask(__name__)
db = create_engine(DATABASE_URL)
Session = sessionmaker(db)

class SubjectApi(Resource):
    def post(self):

        session = Session()
        body = request.json

        id = body.get('id')
        name = body.get('name')

        try:
            subject.create(id=id, name=name, transaction=session)
            return make_response({'message': 'done'}, 200)
        except:
            return make_response({'Error' : 'Id already exist'}, 205)
        finally:
            session.close()


    def get(self):
        session = Session()
        args = request.args

        if 'name' in args:
            subjects = subject.get_by_name(name=args.get('name'), transaction=session)

        if 'id' in args:
            subjects = subject.get_by_id(id=args.get('id'), transaction=session)

        session.close()

        result = list()

        for item in subjects:
            result.append({'id': item.id, 'name': item.name})

        try:
            if len(result) == 0:
                return make_response({'Error' : 'Id or name not found'}, 204)
            else:
                return make_response({'Result:': result}, 200)
        except:
            return make_response({'Error' : 'No Result Found'})


    def put(self):
        session = Session()
        args = request.args
        data = request.get_json()

        try:
            if 'name' in data:
                update_subject = subject.update_by_id(id=args.get('id'), name=data.get('name'), transaction=session)
            return make_response({'Result:': update_subject}, 200)

        except:
            return make_response({'Error' : 'Id not found'}, 204)

        finally:
            session.close()




    def delete(self):

        session = Session()
        args = request.args

        try:
            if 'id' in args:
                delete_subject = subject.delete_by_id(id = args.get('id'), transaction=session)
            return make_response({'Result': delete_subject}, 200)
        except:
            return make_response({'Error': 'Id not found'}, 204)
        finally:
            session.close()
