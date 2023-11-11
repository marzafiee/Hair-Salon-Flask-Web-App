import flask
from flask import request, jsonify
import mysql.connector as mysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True
shortcut = "/api/v1/resources"

# Database connection details
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="boujee_salon",
    port=3306,
    auth_plugin="mysql_native_password",
)

# Create a cursor and initialize it
cursor = mydb.cursor(buffered=True)


# Create a route for the home page
@app.route("/", methods=["GET"])
def home():
    return """<h1>Boujee Salon</h1>
<p>A prototype API for checking hair services and their prices. I think.</p>"""


# Create some test data for our catalog in the form of a list of dictionaries.
services = [
    {"id": 1, "service": "braiding", "price": 120},
    {"id": 2, "service": "washing", "price": 20},
    {"id": 3, "service": "drying", "price": 10},
    {"id": 4, "service": "hair removal", "price": 5},
    {"id": 5, "service": "hair treatment", "price": 50},
]


# Create a route for the services page or V
@app.route(shortcut + "/services/all", methods=["GET"])
def api_all():
    # Create a query to get all the services
    query = "INSERT INTO `customer details` (Customer_id, FirstName, lastName,Email, phone) VALUES (7, 'Hubet','Smith', 'wdijiei@idjf.com', 3245436546)"
    # Execute the query
    cursor.execute(query)
    # Fetch all the results
    results = mydb.commit()
    # Return the results as JSON
    return jsonify(results)


# Create a route for the services page or individual services by id
@app.route(shortcut + "/services", methods=["GET"])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create a query to get the service with the specified ID
    query = "SELECT * FROM services WHERE id = %s"
    # Execute the query
    cursor.execute(query, (id,))
    # Fetch all the results
    results = cursor.fetchall()
    # Return the results as JSON
    return jsonify(results)


# mydb.close()

#    results = []
# for service in services:
# if service["id"] == id:
# results.append(service)

# return jsonify(results)


# Create a route for the prices page
@app.route("/api/v1/resources/prices/all", methods=["GET"])
def all_prices():
    # Create a query to get all the prices
    query = "SELECT * FROM prices"
    # Execute the query
    cursor.execute(query)
    # Fetch all the results
    results = cursor.fetchall()
    # Return the results as JSON
    return jsonify(results)


# mydb.close()


# Create a route for the prices page or # individual prices by id
@app.route(shortcut + "/serv_prices", methods=["GET"])
def price_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create a query to get the price with the specified ID
    query = "SELECT * FROM prices WHERE id = %s"
    # Execute the query
    cursor.execute(query, (id,))
    # Fetch all the results
    results = cursor.fetchall()
    # Return the results as JSON
    return jsonify(results)


# mydb.close()


# function to return key for any value
def get_key(val):
    for i in services:
        if val == i["price"]:
            return i["service"]
    return "key doesn't exist"


prices_list = []


# most expensive service
# @app.route(shortcut + "/expensiveservice", methods=["GET"])
# def high_serv():
#    for i in services:
#        values = []
#        for j in i.values():  # j is the value in the dictionary i
#            values.append(j)
#        prices_list.append(values[2])  #
#    max_serv = max(prices_list)  # max_serv is the max price in the list prices_list
#    final_key = get_key(max_serv)
#    final = {"service": final_key, "price": max_serv}
#    return jsonify(final)


# Get the most expensive service from the database
@app.route(shortcut + "/expensiveservice", methods=["GET"])
def high_serv():
    cursor.execute("SELECT service, price FROM your_table ORDER BY price DESC LIMIT 1")
    result = cursor.fetchone()

    if result:
        service_name = result[0]
        price = result[1]
        final = {"service": service_name, "price": price}
        return jsonify(final)
    else:
        return jsonify({"error": "No services found"})


# mydb.close()

prices_list = []


# least expensive service
@app.route(shortcut + "/cheapestservice", methods=["GET"])
def low_serv():
    for k in services:
        valus = []
        for l in k.values():
            valus.append(l)
        prices_list.append(valus[2])
    min_serv = min(prices_list)
    final_key = get_key(min_serv)
    final = {"service": final_key, "price": min_serv}
    return jsonify(final)


# sorting services alphabetically from smallest to largest
@app.route(shortcut + "/services/sort", methods=["GET"])
def sort_serv():
    return jsonify(sorted(services, key=lambda x: x["service"]))
    # sorting services alphabetically from smallest to largest


# sorting prices from lowest to highest
@app.route(shortcut + "/prices/sort", methods=["GET"])
def sort_price():
    return jsonify(sorted(services, key=lambda x: x["price"]))
    # sorting services alphabetically from smallest to largest


# all prices
# @app.route(shortcut + "/serv_prices/all", methods=["GET"])
# def api_all_serv_prices():
#    return jsonify(services)


# def price_id():
# Check if an ID was provided as part of the URL.
# If ID is provided, assign it to a variable.
# If no ID is provided, display an error in the browser.
#    if "id" in request.args:
#        id = int(request.args["id"])
#    else:
#        return "Error: No id field provided. Please specify an id"

# empty list for resullts
#    price_res = []
#    for x in services:
#        if x["id"] == id:
#            price_res.append(x)
#    return jsonify(price_res)

app.run()
