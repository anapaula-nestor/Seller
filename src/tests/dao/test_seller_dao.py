import pytest
import sys

sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.seller_dao import SellerDao
from src.model.seller import Seller


@pytest.fixture
def create_instance():
    return Seller(True, 1)


def test_instance():
    seller_dao = SellerDao()
    assert isinstance(seller_dao, SellerDao)


def test_save(create_instance):
    seller_saved = SellerDao().save(create_instance)
    assert seller_saved.id_ is not None
    SellerDao().delete(seller_saved)


def test_not_save():
    with pytest.raises(UnmappedInstanceError):
        SellerDao().save('seller')


def test_read_by_id(create_instance):
    seller_saved = SellerDao().save(create_instance)
    seller_read = SellerDao().read_by_id(seller_saved.id_)
    assert isinstance(seller_read, Seller)
    SellerDao().delete(seller_read)


def test_not_read_by_id():
    with pytest.raises(TypeError):
        SellerDao().read_by_id('seller.id_')


def test_read_all():
    seller_read = SellerDao().read_all()
    assert isinstance(seller_read, list)


def test_delete(create_instance):
    seller_saved = SellerDao().save(create_instance)
    seller_read = SellerDao().read_by_id(seller_saved.id_)
    SellerDao().delete(seller_read)
    seller_read = SellerDao().read_by_id(seller_saved.id_)
    assert seller_read is None


def test_not_delete():
    with pytest.raises(UnmappedInstanceError):
        SellerDao().delete('seller_read')
