from conftest import client
import pytest
from flask import Flask
import pytest_mock


def test_index(client: Flask):
    response = client.get("/")
    assert b"<p>Hello, World!</p>" in response.data
    assert response.status_code == 200


@pytest.mark.Mock
def test_mock_hello(mocker):
    def hello():
        return "<p>Hello, Kristell!</p>"
    mocker.patch('test_flask.test_index', hello)
    assert "Hello, Kristell" in test_index()

@pytest.mark.Success
@pytest.mark.parametrize("param", ["/", "/other"])
def test_routes(client, param):
    response = client.get(param)
    assert response.status_code == 200

@pytest.mark.Failed
@pytest.mark.parametrize("param", [2.4, "/toto"])
def test_wrong_routes(client, param):
    response = client.get(str(param))
    assert response.status_code == 404


@pytest.mark.Route
@pytest.mark.parametrize("param", ["Toto"])
def test_exception(client, param):
    with pytest.raises(ValueError):
        client.get("exp?value=" + str(param))
    
