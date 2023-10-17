"""
home page test
"""


def test_homepage_view(client):
    """
    test return homepage status_code 200
    """
    response = client.get("/")
    assert response.status_code == 200
