import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
services = [
    {"id": 1, "service": "braiding", "price": 120},
    {"id": 2, "service": "washing", "price": 20},
    {"id": 3, "service": "drying", "price": 10},
    {"id": 4, "service": "hair removal", "price": 5},
    {"id": 5, "service": "hair treatment", "price": 50},
]


@app.route("/", methods=["GET"])
def home():
    return """<h1>The Boujee Salon :)</h1>
<p>A prototype API for checking hair services and their prices. I think.</p>"""


shortcut = "/api/v1/resources"


@app.route(shortcut + "/services/all", methods=["GET"])
def api_all_serivces():
    return jsonify(services)


@app.route(shortcut + "/services", methods=["GET"])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for service in services:
        if service["id"] == id:
            results.append(service)

    return jsonify(results)


@app.route(shortcut + "/serv_prices/all", methods=["GET"])
def api_all_serv_prices():
    return jsonify(services)


@app.route(shortcut + "/serv_prices", methods=["GET"])
def price_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: No id field provided. Please specify an id"

    # empty list for resullts
    price_res = []
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for x in services:
        if x["id"] == id:
            price_res.append(x)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(price_res)


max_serv = 0
index = 0


@app.route(shortcut + "/expensiveservice", methods=["GET"])
def high_serv():
    for i in services:
        if i["price"] > max_serv:
            max_serv = i["price"]
            index = i
    return jsonify(max_serv)


@app.route(shortcut + "/cheapestservice", methods=["GET"])
def low_serv():
    for j in services:
        min_serv = {key: value for key, value in services.items() if value == min_serv}
    return jsonify(min_serv)


app.run()
