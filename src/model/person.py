import sys
sys.path.append('.')
from sqlalchemy import Column, String, Integer,Boolean
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from src.model.base_model import BaseModel
from src.utils.validators import validate_type, validate_len, validate_not_empty, validate_be_greater_than_zero


class Person(BaseModel):
    __tablename__ = 'person'
    name = Column('name', String(length=100), nullable=False)
    num_doc = Column('num_doc', String(length=50), nullable=False)
    cnpj = Column('cnpj', Boolean, default=False)
    phone = Column('phone', String(length=20), nullable=True)
    id_address = Column('id_address', Integer, ForeignKey('address.id'), nullable=False)
    # address = relationship('address', foreign_keys=[id_address])

    def __init__(self, name: str, num_doc: str, cnpj: bool, phone: str, id_address: int) -> None:
        self.name = name
        self.num_doc = num_doc
        self.cnpj = cnpj
        self.phone = phone
        self.id_address = id_address

    @validates('name')
    def validate_name(self, key, name):
        validate_type(name, str, key)
        validate_len(name, 100, key)
        validate_not_empty(name, key)
        return name

    @validates('num_doc')
    def validate_num_doc(self, key, num_doc):
        validate_type(num_doc, str, key)
        validate_len(num_doc, 50, key)
        validate_not_empty(num_doc, key)
        return num_doc

    @validates('cnpj')
    def validate_cnpj(self, key, cnpj):
        validate_type(cnpj, bool, key)
        return cnpj

    @validates('phone')
    def validate_phone(self, key, phone):
        validate_type(phone, str, key)
        validate_len(phone, 20, key)
        validate_not_empty(phone, key)
        return phone

    @validates('id_address')
    def validate_id_address(self, key, id_address):
        validate_type(id_address, int, key)
        validate_be_greater_than_zero(id_address,key)
        return id_address
