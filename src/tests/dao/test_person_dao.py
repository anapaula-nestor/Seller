import pytest
import sys

sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.person_dao import PersonDao
from src.model.person import Person


@pytest.fixture
def create_instance():
    return Person('name', '123456789', False, '6574-8765', 1)


@pytest.fixture
def create_dao():
    return PersonDao()


def test_instance(create_dao):
    person_dao = create_dao
    assert isinstance(person_dao, PersonDao)


def test_save(create_instance, create_dao):
    person_saved = create_dao.save(create_instance)
    assert person_saved.id_ is not None
    create_dao.delete(person_saved)


def test_not_save(create_dao):
    with pytest.raises(UnmappedInstanceError):
        create_dao.save('person')


def test_read_by_id(create_instance, create_dao):
    person_saved = create_dao.save(create_instance)
    person_read = create_dao.read_by_id(person_saved.id_)
    assert isinstance(person_read, Person)
    create_dao.delete(person_read)


def test_not_read_by_id(create_dao):
    with pytest.raises(TypeError):
        create_dao.read_by_id('person.id_')


def test_read_all(create_dao):
    person_read = create_dao.read_all()
    assert isinstance(person_read, list)


def test_delete(create_instance, create_dao):
    person_saved = create_dao.save(create_instance)
    person_read = create_dao.read_by_id(person_saved.id_)
    create_dao.delete(person_read)
    person_read = create_dao.read_by_id(person_saved.id_)
    assert person_read is None


def test_not_delete(create_dao):
    with pytest.raises(UnmappedInstanceError):
        create_dao.delete('person_read')
