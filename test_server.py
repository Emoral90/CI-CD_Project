import pytest
import requests

BASE_URL = "http://127.0.0.1:8790"

"""
Run server.py in CMD by cd into
"C:\Users\moral\OneDrive\Desktop\School\cse499\CI-CD_Project>" with "py server.py"
"""

@pytest.fixture
def server_url():
    return BASE_URL

def test_top_level_url(server_url):
    response = requests.get(server_url + "/")
    assert response.status_code == 200
    data = response.json()
    expected_keys = ["people", "planets", "films", "species", "vehicles", "starships"]
    for key in expected_keys:
        assert key in data
        assert data[key].startswith(server_url)