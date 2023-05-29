from flask import Flask
from front_src.app.frontend import app

import pytest

@pytest.mark.parametrize("route, expected_status, expected_content", [
    ("/", 200, "Bienvenido, Hola a todo el mundo")
])

def test_index_route(route, expected_status, expected_content):
    client = app.test_client()
    response = client.get(route)
    assert response.status_code == expected_status
    assert  expected_content.encode('utf-8') in response.data
