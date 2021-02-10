from flask import Flask
from flask_restful import Api

from src.resource.person_resource import PersonResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PersonResource, '/api/person', endpoint='people')
api.add_resource(PersonResource, '/api/person/<int:id_>', endpoint='person')
api.add_resource(PersonResource, '/api/seller', endpoint='sellers')
api.add_resource(PersonResource, '/api/seller/<int:id_>', endpoint='seller')


@app.route('/')
def index():
    return 'Hello World!'


app.run(debug=True)
