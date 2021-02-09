import pytest
from pytest import raises
from src.model.seller import Seller
from src.model.base_model import BaseModel


@pytest.mark.parametrize('active', 'id_person', [(True, 1), (False, 1)])
def test_instance(active: bool, id_person: int):
    seller = Seller(active, id_person)
    assert isinstance(seller, Seller)
    assert isinstance(seller, BaseModel)
    assert seller.active is active
    assert seller.id_person is id_person


@pytest.mark.parametrize('active', 'id_person', [('random str', 1), (True, 'random str'),
                                                 ('random str', 'random str'), (1, True)])
def test_wrong_type(active: bool, id_person: int):
    with raises(TypeError):
        Seller(active, id_person)
