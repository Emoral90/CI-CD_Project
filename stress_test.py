# Run in integrated terminal with "py stress_test.py"

import requests
import concurrent.futures
import time

BASE_URL = "http://127.0.0.1:8790"

def make_request(endpoint):
    """Function to send a GET request and return the response status."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

def stress_test_concurrent_requests(endpoint, num_requests=1000):
    """Stress test by making multiple concurrent requests."""
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(make_request, [endpoint] * num_requests))

    end_time = time.time()
    
    # Print summary results
    print(f"Stress Test: {num_requests} requests to {endpoint}")
    print(f"Total Time Taken: {end_time - start_time:.2f} seconds")
    print(f"Successful (200): {results.count(200)}")
    print(f"Not Found (404): {results.count(404)}")
    print(f"Other Errors: {len(results) - results.count(200) - results.count(404)}")

if __name__ == "__main__":
    # Run stress tests on different endpoints
    stress_test_concurrent_requests("/")  # Top-level API
    stress_test_concurrent_requests("/people/1", 2000)  # Valid ID
    stress_test_concurrent_requests("/people/9999", 1000)  # Invalid ID
    stress_test_concurrent_requests("/unknown", 500)  # Invalid endpoint