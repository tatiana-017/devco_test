import pytest

from assingApp.models import assing

#Test #1 formulario asignación de dotación prueba de cada campo

@pytest.mark.django_db
def test_assing():
    newAssing = assing.objects.create_assing(
        serial =120,
        name = 'Asus',
        typeProduc = 'laptop',
        system = 'windows',
        ownerName = 'Tatiana',
        ownerEmail = 'tr384@gmail.com',
        date = 12/8/22
    )

    assert newAssing.serial == 120
    assert newAssing.name == 'Asus'
    assert newAssing.typeProduc == 'laptop'
    assert newAssing.system == 'windows'
    assert newAssing.ownerName == 'Tatiana'
    assert newAssing.ownerEmail == 'tr384@gmail.com'
    assert newAssing.date == 12/8/22

#Test #2 prueba del requerimiento de datos
@pytest.mark.django_db
def test_assing_two():
    new_Assing = assing.objects.create_assing(
        name = 'Asus',
        typeProduc = 'laptop',
        system = 'windows',
        date = 12/8/22
    )

    assert new_Assing.name=='Asus'

