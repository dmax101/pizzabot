from pymongo import MongoClient
from utils.log import log
import time

class DbConnector:
    # Construtor da conexão
    def __init__(self, user, pw, database) -> None:
        self.user = user
        self.password = pw
        self.database = database

    # Conexão MongoDB
    def connect(self):
        while True:
            try:
                log("Connecting...",location=[self])
                self.client = MongoClient(
                    "mongodb+srv://{}:{}@cluster0.vmhbw.mongodb.net/{}?retryWrites=true&w=majority"
                        .format(
                            self.user,
                            self.password,
                            self.database
                        )
                    )

                log("Done...",location=[self])
                return self.client[self.database]
            except:
                log("Something wrong happens! Retrying in 5 seconds",location=[self], type_of="error")
                time.sleep(5)