import sys
sys.path.append('.')
import pytest
from src.model.person import Person


@pytest.fixture
def create_instance():
    return Person('Ana', '687.795.349-41', False, '12346789',1)


@pytest.mark.parametrize(
    'name,num_doc,cnpj,phone,id_address', [
        ('nome'*300, '623523556', True, '1189865432', 12),
        ('nome aleatorio', '42342342342' *200, False, '42342525245', 1),
        ('nome aleatorio2', '42342342342', True, '42342525245'*200, 1),
        ('nome aleatorio2', '42342342342', True, '42342525245', -1)

    ]
)
def test_person_wrong_values(name, num_doc, cnpj, phone, id_address):
    with pytest.raises(ValueError):
        Person(name, num_doc, cnpj, phone, id_address)


@pytest.mark.parametrize(
    'name,num_doc,cnpj,phone,id_address', [
        (1, '623523556', True, '1189865432', 12),
        ('nome aleatorio', 12, False, '42342525245', 1),
        ('nome aleatorio2', '42342342342', 'True', '42342525245', 1),
        ('nome aleatorio2', '42342342342', True, 42342525245, 1),
        ('nome aleatorio2', '42342342342', True, '42342525245', '1')
    ]
)
def test_person_wrong_type(name, num_doc, cnpj, phone, id_address):
    with pytest.raises(TypeError):
        Person(name, num_doc, cnpj, phone, id_address)


@pytest.mark.parametrize(
    'name,num_doc,cnpj,phone,id_address', [
        ('nome', '623523556', True, '1189865432', 12),
        ('nome aleatorio', '42342342342', False, '42342525245', 1)
    ]
)
def test_person_values(name, num_doc, cnpj, phone, id_address):
    per = Person(name, num_doc, cnpj, phone, id_address)

    assert per.name == name
    assert per.num_doc == num_doc
    assert per.cnpj == cnpj
    assert per.phone == phone
    assert per.id_address == id_address


def test_person_instance(create_instance):
    assert isinstance(create_instance, Person)
