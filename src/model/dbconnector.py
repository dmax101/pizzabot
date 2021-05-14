from pymongo import MongoClient

class DbConnector:
    # Construtor da conexão
    def __init__(self, user, pw, database) -> None:
        self.user = user
        self.password = pw
        self.database = database

    # Conexão MongoDB
    def connect(self):
        self.client = MongoClient(
            "mongodb+srv://{}:{}@cluster0.vmhbw.mongodb.net/{}?retryWrites=true&w=majority"
                .format(
                    self.user,
                    self.password,
                    self.database
                )
            )

        return self.client[self.database]