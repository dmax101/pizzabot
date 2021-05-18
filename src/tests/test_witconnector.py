import pytest
from model.witconnector import WitConnector

def test_send_message_response():

    client = WitConnector()

    resp = client.message("quero uma pizza de pepperoni")

    assert isinstance(resp, dict), "The response has to be a dictionary"