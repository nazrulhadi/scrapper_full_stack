from neo4j import GraphDatabase

# Neo4j connection settings
uri = "bolt://172.18.0.2:7687"
username = "neo4j"
password = "neo4j123"



# Load person data
cypher_query = '''
LOAD CSV WITH HEADERS FROM "file:///outlets_with_coordinates.csv" AS row
MERGE (s:State {state:"Melaka"})
MERGE (o:Outlet {state:"Melaka",outlet_name:row.outlet_name})
MERGE (o)-[:LOCATED_IN]->(s)
MERGE (o)-[:LOCATED_AT]->(a:Address {outlet_name:row.outlet_name,full_address: row.address, latitude: toFloat(row.Latitude), longitude: toFloat(row.Longitude)})
'''

class Neo4jLoader:
    def __init__(self, uri, username, password):
        self._uri = uri
        self._username = username
        self._password = password
        self._driver = None

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._username, self._password))

    def load_data(self):
        with self._driver.session() as session:
            session.run(cypher_query)

if __name__ == "__main__":
    loader = Neo4jLoader(uri, username, password)

    try:
        loader.connect()
        # Load data
        loader.load_data()

        print("Data loaded successfully!")

    finally:
        loader.close()
