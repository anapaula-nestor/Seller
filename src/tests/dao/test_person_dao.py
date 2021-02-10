import pytest
import sys

sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.person_dao import PersonDao
from src.model.person import Person


@pytest.fixture
def create_instance():
    return Person('name', '123456789', False, '6574-8765', 1)


def test_instance():
    person_dao = PersonDao()
    assert isinstance(person_dao, PersonDao)


def test_save(create_instance):
    person_saved = PersonDao().save(create_instance)
    assert person_saved.id_ is not None
    PersonDao().delete(person_saved)


def test_not_save():
    with pytest.raises(UnmappedInstanceError):
        PersonDao().save('person')


def test_read_by_id(create_instance):
    person_saved = PersonDao().save(create_instance)
    person_read = PersonDao().read_by_id(person_saved.id_)
    assert isinstance(person_read, Person)
    PersonDao().delete(person_read)


def test_not_read_by_id():
    with pytest.raises(TypeError):
        PersonDao().read_by_id('person.id_')


def test_read_all():
    person_read = PersonDao().read_all()
    assert isinstance(person_read, list)


def test_delete(create_instance):
    person_saved = PersonDao().save(create_instance)
    person_read = PersonDao().read_by_id(person_saved.id_)
    PersonDao().delete(person_read)
    person_read = PersonDao().read_by_id(person_saved.id_)
    assert person_read is None


def test_not_delete():
    with pytest.raises(UnmappedInstanceError):
        PersonDao().delete('person_read')
