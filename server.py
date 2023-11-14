from flask import Flask, render_template, request,make_response
from neo4j_connection import Neo4jConnection
from catchment_calculation import find_intersecting_outlets
from math import radians, sin, cos


neo4j_connection = Neo4jConnection(
    uri="bolt://172.20.0.2:7687",
    user="neo4j",
    password="neo4j123",
    

)

app = Flask(__name__)

def execute_query(query):
    with neo4j_connection._driver.session() as session:
        result = session.run(query)
        output = result.data()
    return output

@app.route("/")
def index():
    
    return render_template("dashboard.html")



@app.route("/map", methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        # Get data from the request
        data = request.form.to_dict()

        # Do something with the values, for example, print them
        print(data)

        outlet_name_query = f"""
        MATCH (o:Outlet)-[:LOCATED_AT]->(a:Address)
        WHERE o.outlet_name = "{data["outletName"]}"
        RETURN o.outlet_name AS outlet_name, a.latitude AS latitude, a.longitude AS longitude
        """
        distance = float(data["CRK"]) * 1000
        specific_outlet = execute_query(outlet_name_query)
    else:
        # Handle the case when the route is accessed via GET without a form submission
        specific_outlet = []
        list_of_outlet =[]
        distance=5000

    all_outlet_query = f"""
    MATCH (o:Outlet)-[:LOCATED_AT]->(a:Address)
    RETURN a.latitude AS latitude, a.longitude AS longitude
    """

    list_of_outlet = execute_query(all_outlet_query)

    intersecting_outlets = find_intersecting_outlets(list_of_outlet, specific_outlet, distance)

    response = make_response(render_template("map.html", outlets_data=intersecting_outlets))
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    return response
