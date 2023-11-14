from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        
        self._driver = None
        self._connect()

    def _connect(self):
        config = {"max_transaction_retry_time": 30.0} 
        # self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password),database=self._database)
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def close(self):
        if self._driver is not None:
            self._driver.close()