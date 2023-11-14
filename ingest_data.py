from py2neo import Graph
graph = Graph("bolt://172.20.0.2:7687", auth=("neo4j", "neo4j123"))

#clear the node
clear_cyp ='''MATCH(n)
DETACH DELETE n'''
graph.run(clear_cyp)

#load Country data
ingest_data = '''LOAD CSV WITH HEADERS FROM "file:///outlets_with_coordinates.csv" AS row
MERGE (s:State {state:"Melaka"})
MERGE (o:Outlet {state:"Melaka",outlet_name:row.outlet_name})
MERGE (o)-[:LOCATED_IN]->(s)
MERGE (o)-[:LOCATED_AT]->(a:Address {outlet_name:row.outlet_name,full_address: row.address, latitude: toFloat(row.Latitude), longitude: toFloat(row.Longitude)})'''

graph.run(ingest_data)
print("data sucessfully ingest")