"""
Test Case for lettings views
"""
import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from .models import Letting, Address

@pytest.mark.django_db
def test_lettings_list_view(client):
    """
    test show list of lettings
    status code 200
    """
    response = client.get('/lettings/')
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()

@pytest.mark.django_db
def test_lettings_details(client):
    """
    test show letting detail
    example address and letting then call endpoint with letting id
    return status_code 200
    """
    address = Address.objects.create(
        number=12,
        street="Nord street",
        city="LA",
        state="GA",
        zip_code=12345,
        country_iso_code="USA",
    )

    Letting.objects.create(
        title = "New letting",
        address = address
    )
    path = reverse('letting', kwargs={'letting_id':1})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response,'letting.html')

@pytest.mark.django_db
def test_letting_model():
    """
    return test letting
    """
    address = Address.objects.create(
        number=12,
        street="Nord street",
        city="LA",
        state="GA",
        zip_code=12345,
        country_iso_code="USA",
    )

    letting = Letting.objects.create(
        title = "New letting",
        address = address
    )
    expected = "New letting"
    assert str(letting)==expected
    assert Letting.objects.count() == 1


@pytest.mark.django_db
def test_address_model():
    """
    return test letting
    """
    address = Address.objects.create(
        number=12,
        street="Nord street",
        city="LA",
        state="GA",
        zip_code=12345,
        country_iso_code="USA",
    )

    expected = "12 Nord street"
    assert str(address)==expected
    assert Address.objects.count() == 1