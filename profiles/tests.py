"""
Test module
"""
import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
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
    path = reverse("profiles:profile",  kwargs={'username': "test"})

    response = client.get(path)
    expected_content = "test"
    assert response.status_code==200
    assert expected_content in response.content.decode()
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_model():
    """
    return test profile
    """
    user = User.objects.create_user('test')
    profile = Profile.objects.create(
        user=user,
        favorite_city="Hanoi",
    )
    expected = "test"
    assert str(profile)==expected
    assert User.objects.count() == 1