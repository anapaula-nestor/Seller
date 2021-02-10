import sys
sys.path.append('.')

from src.dao.base_dao import BaseDao
from src.model.person import Person


class PersonDao(BaseDao):
    def __init__(self):
        super().__init__(Person)
