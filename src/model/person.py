from sqlalchemy import Column, String, Integer,Boolean
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from src.model.base_model import BaseModel


class Person(BaseModel):
    __tablename__ = 'person'
    name = Column('name', String(length=100), nullable=False)
    num_doc = Column('num_doc', String(length=50), nullable=False)
    cnpj = Column('cnpj', Boolean, default=False)
    phone = Column('phone', String(length=20), nullable=True)
    id_address = Column('id_address', Integer, ForeignKey('adress.id'), nullable=False)
    address = relationship('address', foreign_keys=[id_address])

    def __init__(self, name: str, num_doc: str, cnpj: bool, phone: str, id_address: int) -> None:
        self.name = name
        self.num_doc = num_doc
        self.cnpj = cnpj
        self.phone = phone
        self.id_address = id_address

