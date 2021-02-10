import pytest
import sys

sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.seller_dao import SellerDao
from src.model.seller import Seller


@pytest.fixture
def create_instance():
    return Seller(True, 1)


@pytest.fixture
def create_dao():
    return SellerDao()


def test_instance(create_dao):
    seller_dao = create_dao
    assert isinstance(seller_dao, SellerDao)


def test_save(create_instance, create_dao):
    seller_saved = create_dao.save(create_instance)
    assert seller_saved.id_ is not None
    create_dao.delete(seller_saved)


def test_not_save(create_dao):
    with pytest.raises(UnmappedInstanceError):
        create_dao.save('seller')


def test_read_by_id(create_instance, create_dao):
    seller_saved = create_dao.save(create_instance)
    seller_read = create_dao.read_by_id(seller_saved.id_)
    assert isinstance(seller_read, Seller)
    create_dao.delete(seller_read)


def test_not_read_by_id(create_dao):
    with pytest.raises(TypeError):
        create_dao.read_by_id('seller.id_')


def test_read_all(create_dao):
    seller_read = create_dao.read_all()
    assert isinstance(seller_read, list)


def test_delete(create_instance, create_dao):
    seller_saved = create_dao.save(create_instance)
    seller_read = create_dao.read_by_id(seller_saved.id_)
    create_dao.delete(seller_read)
    seller_read = create_dao.read_by_id(seller_saved.id_)
    assert seller_read is None


def test_not_delete(create_dao):
    with pytest.raises(UnmappedInstanceError):
        create_dao.delete('seller_read')
