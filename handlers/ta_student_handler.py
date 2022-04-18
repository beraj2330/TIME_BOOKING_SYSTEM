from flask_restful import Resource
from flask import Flask, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import DATABASE_URL
from models.ta_student_model import taStudent

app = Flask(__name__)
db = create_engine(DATABASE_URL)
Session = sessionmaker(db)

class TaStudentApi(Resource):
    def post(self):

        session = Session()
        body = request.json

        id = body.get('id')
        email = body.get('email')
        ta_id = body.get('TaId')
        ta_email = body.get('TaEmail')
        ta_subject_id = body.get('TaSubId')
        ta_subject_name = body.get('TaSubName')
        student_id = body.get('StudId')
        student_email = body.get('StudEmail')
        student_subject_id = body.get('StudSubId')
        student_subject_name = body.get('StudSubName')

        # taStudent.createStudent(id = id, student_id=student_id, student_email=student_email, student_subject_id=student_subject_id, student_subject_name=student_subject_name, transaction=session)

        if id == ta_id and email == ta_email:
            try:
                taStudent.createTA(id=id,email=email, ta_id = ta_id, ta_email = ta_email, ta_subject_id=ta_subject_id, ta_subject_name=ta_subject_name, transaction=session)
                return make_response({'message': 'Done'}, 200)
            except:
                return make_response({'Error' : 'Id or name or email already exist'}, 205)
        else:
            try:
                taStudent.createSTUDENT(id=id, email=email, student_id=student_id, student_email=student_email, student_subject_id=student_subject_id, student_subject_name=student_subject_name, transaction=session)
                return make_response({'message': 'Done'}, 200)
            except:
                return make_response({'Error': 'Id or name or email already exist'}, 205)

        session.close()


    def get(self):
        session = Session()
        args = request.args

        if 'id' in args:
            TaStudent = taStudent.get_by_STUDENTid(student_id=args.get('id'), transaction=session)
        else:
            TaStudent = taStudent.get_by_STUDENTemail(student_email=args.get('email'), transaction=session)

        result = list()

        for item in TaStudent:
            result.append({'StudentId': item.student_id, 'StudentEmail': item.student_email,
                           'StudentSubId': item.student_subject_id, 'StudentSubName': item.student_subject_name})
        try:
            if len(result) == 0:
                return make_response({'Error' : 'Error'}, 204)
            else:
                return make_response({'Result:': result}, 200)
        except:
            print()














    # student course addition
    def put(self):

        session = Session()
        args = request.args
        data = request.get_json()


        # try:
        #     if 'id' in args:
        #         id = args.get('id')
        #         get_taStudent = taStudent.get_by_id(id, transaction=session)
        #
        #         for item in get_taStudent:
        #             if id == item.student_id:
        #                 taStudent.createStudent(id = item.student_id+100000, student_id=item.student_id, student_email=item.student_email, student_subject_id=data.get('SubId'), student_subject_name=data.get('SubName'), transaction=session)
        #                 return make_response({'message': 'Done'}, 200)
        #     else:
        #         email = args.get('email')
        #         get_taStudent = taStudent.get_by_id(email, transaction=session)
        #
        #         for item in get_taStudent:
        #             if email == item.student_email:
        #                 taStudent.createStudent(student_id=item.student_id, student_email=item.student_email,student_subject_id=data.get('SubId'),student_subject_name=data.get('SubName'))
        #                 return make_response({'message': 'Done'}, 200)
        # except:
        #     return make_response({'Error': 'Id or name or email already exist'}, 205)
        # finally:
        #     session.close()

        try:
            if 'id' in args:
                print("1")
                id = args.get('id')
                print("2")
                get_taStudent = taStudent.get_by_id(id, transaction=session)
                print("3")

                for item in get_taStudent:
                    print("4")
                    # print(item.student_email)
                    # print(data.get('SubId'))
                    get_student = taStudent.get_by_STUDENTid(student_id=id, student_subject_id=data.get('SubId'))

                    for ban in get_student:
                        print("student_email ", item.id)
                        print("7")
                        delete_student = taStudent.delete_by_StudentId(id=ban.item.email, transaction=session)
                        print("12")
                        return make_response({'message': delete_student}, 200)

                    # print("4")
                    # print(id)
                    # print(item.student_id)
                    # if id == item.student_id:
                    # print("5")
                    # delete_student = taStudent.delete_by_StudentId(id=id,transaction=session)
                    # print("10")
                    # return make_response({'message': delete_student}, 200)
                    # , student_subject_id = data.get('SubId'), student_subject_name = data.get('SubName')

                    # elif id == item.ta_id:
                    #     delete_ta = taStudent.delete_by_TaId(ta_id=item.ta_id, ta_subject_id=data.get('SubId'), ta_subject_name=data.get('SubName'),transaction=session)
                    #     return make_response({'message': delete_ta}, 200)

            else:
                email = args.get('email')
                get_taStudent = taStudent.get_by_id(email, transaction=session)

                for item in get_taStudent:
                    # if email == item.student_email:
                    delete_student = taStudent.delete_by_StudentEmail(student_email=email, transaction=session)

                    return make_response({'message': delete_student}, 200)
                # elif id == item.ta_id:
                #     delete_ta = taStudent.delete_by_TaEmail(ta_id = item.ta_id, ta_subject_id = data.get('SubId'), ta_subject_name = data.get('SubName'),
                #     transaction = session)
                #
                #     return make_response({'message': delete_ta}, 200)
        except:
            return make_response({'Error': 'Id or name or email already exist'}, 205)
        finally:
            session.close()







    def delete(self):

        session = Session()
        args = request.args
        data = request.get_json()

        try:
            if 'id' in args:
                print("1")
                id = args.get('id')
                print("2")
                get_taStudent = taStudent.get_by_id(id, transaction=session)
                print("3")

                for item in get_taStudent:
                    print("4")
                    # print(item.student_email)
                    # print(data.get('SubId'))
                    get_student = taStudent.get_by_STUDENTid(student_id=id, student_subject_id=data.get('SubId'))

                    for ban in get_student:
                        print("student_email " , item.id)
                        print("7")
                        delete_student = taStudent.delete_by_StudentId(id=ban.item.email,transaction=session)
                        print("12")
                        return make_response({'message': delete_student}, 200)


                    # print("4")
                    # print(id)
                    # print(item.student_id)
                    # if id == item.student_id:
                    # print("5")
                    # delete_student = taStudent.delete_by_StudentId(id=id,transaction=session)
                    # print("10")
                    # return make_response({'message': delete_student}, 200)
                    # , student_subject_id = data.get('SubId'), student_subject_name = data.get('SubName')


                    # elif id == item.ta_id:
                    #     delete_ta = taStudent.delete_by_TaId(ta_id=item.ta_id, ta_subject_id=data.get('SubId'), ta_subject_name=data.get('SubName'),transaction=session)
                    #     return make_response({'message': delete_ta}, 200)

            else:
                email = args.get('email')
                get_taStudent = taStudent.get_by_id(email, transaction=session)

                for item in get_taStudent:
                    # if email == item.student_email:
                        delete_student = taStudent.delete_by_StudentEmail(student_email = email, transaction = session)

                        return make_response({'message': delete_student}, 200)
                    # elif id == item.ta_id:
                    #     delete_ta = taStudent.delete_by_TaEmail(ta_id = item.ta_id, ta_subject_id = data.get('SubId'), ta_subject_name = data.get('SubName'),
                    #     transaction = session)
                    #
                    #     return make_response({'message': delete_ta}, 200)
        except:
            return make_response({'Error': 'Id or name or email already exist'}, 205)
        finally:
            session.close()
