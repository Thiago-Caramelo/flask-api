import mock
from app import create_app
from flask import Flask


def test_create_app():
    result = create_app(None)
    assert type(result) is Flask
