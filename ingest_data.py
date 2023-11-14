from py2neo import Graph
graph = Graph("neo4j://localhost:7687", auth=("neo4j", "qwertyuiop"))

#clear the node
clear_cyp ='''MATCH(n)
DETACH DELETE n'''
graph.run(clear_cyp)

#load Country data
ingest_data = '''load csv with  headers from "file:///outlets_with_coordinates.csv" as row
WITH row WHERE row.outletname is not null
MERGE (o:Outlet{outlet_name:row.outletname}-[:LOCATED_IN]-(s:State{state:"Melaka"})
MERGE (o)-[:LOCATED_AT]-(a:Address{full_address:row.address,latitude:row.latitude,longitude:row.longitude})'''

graph.run(ingest_data)