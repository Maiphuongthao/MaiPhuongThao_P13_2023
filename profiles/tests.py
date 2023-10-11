"""
Test module
"""
from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from .models import Profile

@pytest.mark.django_db
def test_profiles_list_view(client):
    """
    Test desplay profiles
    return code 200
    """
    response = client.get('/profiles/')
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_detail_profile_view(client):
    """
    Test detail of a profile
    status code 2000
    expect content
    """
    user = User.objects.create_user('test')
    Profile.objects.create(
        user=user,
        favorite_city="Hanoi",
    )
    breakpoint()
    path = reverse("profile",  kwargs={'username': "test"})

    response = client.get(path)
    expected_content = "test"
    assert response.status_code==200
    assert expected_content in response.content.decode()
    assertTemplateUsed(response, "profile.html")
