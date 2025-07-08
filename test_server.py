# Run server.py in CMD by cd into dir with server, with "pytest server.py"

# HTTP codes
# 200 OK
# 201 Created
# 204 No content
# 301 Moved permanently
# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not found
# 405 Method not allowed
# 500 Internal server error

import pytest
import requests

BASE_URL = "http://127.0.0.1:8790"

@pytest.fixture
def server_url():
    return BASE_URL

def test_top_level_url(server_url):
    """Test root URL structure matches individual category URLs"""
    response = requests.get(server_url + "/")
    assert response.status_code == 200
    data = response.json()
    expected_keys = ["people", "planets", "films", "species", "vehicles", "starships"]
    for key in expected_keys:
        assert key in data
        assert data[key].startswith(server_url)

def test_valid_people_entry():
    """Test retrieving a valid person entry (assuming 'people1' exists in data.txt)."""
    response = requests.get(f"{BASE_URL}/people/1")
    assert response.status_code == 200 
    data = response.json()
    assert isinstance(data, dict)
    assert "name" in data  # Assuming people objects have a "name" key

def test_invalid_people_entry():
    """Test retrieving an invalid person entry (not in data.txt)."""
    response = requests.get(f"{BASE_URL}/people/9999")
    assert response.status_code == 404

def test_invalid_category():
    """Test accessing an invalid category (not in API)."""
    response = requests.get(f"{BASE_URL}/unknown/")
    assert response.status_code == 404

def test_non_numeric_id():
    """Test non-numeric ID in a valid category."""
    response = requests.get(f"{BASE_URL}/people/abc")
    assert response.status_code == 404

def main():
    base_url = server_url()
    test_top_level_url(base_url)
    test_valid_people_entry()
    test_invalid_people_entry()
    test_invalid_category()
    test_non_numeric_id()

if __name__ == "__main__":
    main()