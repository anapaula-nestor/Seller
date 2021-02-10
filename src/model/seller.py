from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from src.model.base_model import BaseModel
from src.model.person import Person
from src.utils.validators import validate_type


class Seller(BaseModel):
    __tablename__ = 'seller'
    active = Column('active', Boolean, default=True)
    id_person = Column('id_person', Integer, ForeignKey('person.id'), nullable=False)
    person = relationship('Person', foreign_keys=[id_person])

    def __init__(self, active: bool, id_person: int) -> None:
        self.active = active
        self.id_person = id_person

    @validates('active')
    def validate_active(self, key, active):
        validate_type(active, bool, key)
        return active

    @validates('id_person')
    def validate_id_person(self, key, id_person):
        validate_type(id_person, int, key)
        return id_person
