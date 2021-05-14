import pytest
import os
import pprint as pp

from ..model.dbconnector import DbConnector

@pytest.fixture(scope="function")
def initial():
    cn = {
        "user": "pizzabot",
        "password": os.environ["DB_PASSWORD"],
        "database": "pizzabot",
    }

    client = DbConnector(cn["user"], cn["password"], cn["database"])

    db = client.connect()
    order_db = db.order

    return order_db

def post(initial):
    try:
        post = {"nome": "Danilo"}

        post_id = initial.find_one(post)

        pp.pprint(post_id)
    except Exception as e:
        # Lidando com possíveis erros de comunicação
        print("Oops! {} ocorrido".format(e.__class__))
        pp.pprint(e)