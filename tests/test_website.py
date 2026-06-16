import pytest
import requests
import time

BASE_URL = "http://135.235.194.128"

def test_home_page_loads():
    """Home page 200 status return check"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_api_health():
    """Backend API running- check"""
   
    time.sleep(10)
    response = requests.get(f"{BASE_URL}:5000/api/products", timeout=30)
    assert response.status_code == 200