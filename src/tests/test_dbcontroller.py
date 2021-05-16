# import pytest
# import os

# from ..controller.dbcontroller import DbController
# from ..model.dbconnector import DbConnector

# @pytest.fixture(scope="function")
# def dbConector_db_collection():
#     cn = {
#         "user": "pizzabot",
#         "password": os.environ["DB_PASSWORD"],
#         "database": "pizzabot",
#     }

#     client = DbConnector(cn["user"], cn["password"], cn["database"])

#     db = client.connect()
#     collection = db.order

#     return collection
