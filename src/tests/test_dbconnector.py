import pytest
import os
import pprint as pp
from datetime import datetime
import warnings

from model.dbconnector import DbConnector

@pytest.fixture(scope="function")
def initial():
    client = DbConnector("pizzabot", os.environ["DB_PASSWORD"], "test")

    db = client.connect()
    test_db = db.test

    return test_db

@pytest.mark.filterwarnings("ignore:.*U.*mode is deprecated:DeprecationWarning")
def test_insert_one(initial):
    warnings.simplefilter('always')

    post = {"test": datetime.now()}

    post_id = initial.insert_one(post).inserted_id

    pp.pprint(post_id)