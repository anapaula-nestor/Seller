import sys
sys.path.append('.')

from flask_restful import fields, marshal_with
from src.dao.person_dao import PersonDao
from src.model.person import Person
from src.resource.base_resource import BaseResource


class PersonResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "num_doc": fields.String,
        "cnpj": fields.Boolean,
        "phone": fields.String,
        "id_address": fields.Integer
    }

    def __init__(self):
        self.__dao = PersonDao()
        self.__model_type = Person

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id_=None):
        return super().get(id_)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id_):
        return super().put(id_)

    @marshal_with(fields)
    def delete(self, id_):
        return super().delete(id_)
