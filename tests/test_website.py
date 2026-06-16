import pytest
import requests

BASE_URL = "http://135.235.194.128"

def test_home_page_loads():
    """Home page 200 status return பண்றதான்னு check"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_api_health():
    """Backend API running-ஆ இருக்கான்னு check"""
    response = requests.get(f"{BASE_URL}:5000/api/products")
    assert response.status_code == 200