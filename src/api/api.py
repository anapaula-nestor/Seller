from flask import Flask
from flask_restful import Api

from src.resource.person_resource import PersonResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PersonResource, '/api/person', endpoint='person')
api.add_resource(PersonResource, '/api/person/<int:id_>', endpoint='people')


@app.route('/')
def index():
    return 'Hello World!'


app.run(debug=True)
