"""
Test module
"""
from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

@pytest.mark.django_db
def test_profiles_list_view(client):
    """
    Test desplay profiles
    return code 200
    """
    response = client.get('/profiles/')
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


