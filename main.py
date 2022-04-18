import flask_restful
from flask import Flask
from flask_cors import cross_origin, CORS

from handlers.student_handler import StudentApi
from handlers.subject_handler import SubjectApi
from handlers.ta_handler import TaApi
from handlers.student_enroll_handler import StudentEnrollApi

app = Flask(__name__)
cors = CORS(app)
cross_origin()

api = flask_restful.Api(app)
api.add_resource(SubjectApi, '/subject')
api.add_resource(TaApi, '/ta')
api.add_resource(StudentApi, '/student')
api.add_resource(StudentEnrollApi, '/student/enroll')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
