from flask import Flask
from flask_restful import Resource, Api

# Resource: collection of data that our api returns

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource): 
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return{"item": None}, 404 #a valid json when object is not fount
d
    def post(self, name):
        item = {"name":name, "price": 12.00}
        items.append(item)
        return item

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Ernest

app.run(debug = True)