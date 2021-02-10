from src.dao.base_dao import BaseDao
from src.model.seller import Seller


class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)
