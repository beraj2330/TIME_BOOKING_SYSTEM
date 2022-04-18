from flask_restful import Resource
from flask import Flask, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import DATABASE_URL
from models.ta_model import ta

app = Flask(__name__)
db = create_engine(DATABASE_URL)
Session = sessionmaker(db)

class TaApi(Resource):
    def post(self):

        session = Session()
        body = request.json


        ta_id = body.get('TaId')
        subject_id = body.get('SubId')


        try:
            ta.create(ta_id = ta_id, subject_id=subject_id, transaction=session)

            return make_response({'message': 'Done'}, 200)
        except:
            return make_response({'Error' : 'Id already exist'}, 205)
        finally:
            session.close()

    def get(self):
        session = Session()
        args = request.args
        action = args.get('Action')
        result = list()

        if action == 'withdraw':
            Ta = ta.get_by_TaWithdraw(ta_id=args.get('id'), transaction=session)

            session.close()

            for item in Ta:
                result.append({'SubId': item.subject_id})

            try:
                if len(result) == 0:
                    return make_response({'Error': 'Id not found'}, 204)
                else:
                    return make_response({'Result:': result}, 200)
            except:
                return make_response({'Error': 'No Result Found'})

    def delete(self):

        session = Session()
        args = request.args

        try:

            delete_ta = ta.delete(ta_id=args.get('TaId'), subject_id=args.get('SubId'),transaction=session)
            return make_response({'Result': delete_ta}, 200)
        except:
            return make_response({'Error': 'Id not found'}, 204)
        finally:
            session.close()
