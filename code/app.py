from flask import Flask
from flask_restful import Resource, Api

# Resource: data that our api returns

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name): #this resource can only be accessed by get request
        return {'student':name}

api.add_resource(Student, '/student/<string:name>') # student/Ernest

app.run()