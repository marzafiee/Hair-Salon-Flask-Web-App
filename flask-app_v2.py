# Import the Flask library to create a web application
import flask
from flask import request, jsonify, render_template
import mysql.connector as mysql
import pymysql
import os
from dotenv import (
    load_dotenv,
)  # Import the load_dotenv function from the python-dotenv library to load environment variables from my .env file
from datetime import datetime

load_dotenv()
app = flask.Flask(__name__)
# Enable debug mode for the Flask app (this provides detailed error messages and auto-reloads the server when code changes)
app.config["DEBUG"] = True
# Define a shortcut for the API base URL (to avoid repeating it in every route)
shortcut = "/api/v1/resources"

# Define the database connection configuration using environment variables
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "boujee_salon"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "auth_plugin": "mysql_native_password",
}


# Define a function to create and return a connection to the MySQL database
def get_db_connection():
    """Create a connection to the MySQL database"""
    conn = mysql.connect(
        **db_config
    )  # Use the db_config dictionary to connect to the database
    return conn


# Define a route for the home page (accessible via HTTP GET requests)
@app.route("/", methods=["GET"])
def home():
    """Home page route that displays all services"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries (dictionary=True means results will be returned as dictionaries)
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch all services and their prices
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        current_year = datetime.now().year

        # Render the index.html template and pass the services data to it
        return render_template("index.html", services=services)
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Define an API route to fetch all services (accessible via HTTP GET requests)
@app.route(shortcut + "/services/all", methods=["GET"])
def api_all():
    """API endpoint to get all services"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch all services
        cursor.execute("SELECT * FROM services")
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Return the services data as a JSON response
        return jsonify(services)
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to fetch a specific service by ID (accessible via HTTP GET requests)
@app.route(shortcut + "/services", methods=["GET"])
def api_id():
    """API endpoint to get a service by ID"""
    # Check if the 'id' parameter is provided in the request URL
    if "id" in request.args:
        id = int(request.args["id"])  # Convert the 'id' parameter to an integer
    else:
        # If 'id' is not provided, return an error message and a 400 status code
        return jsonify({"error": "No id field provided. Please specify an id."}), 400

    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the service with the specified ID
        cursor.execute("SELECT * FROM services WHERE id = %s", (id,))
        # Fetch one row from the query result
        service = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # If a service is found, return it as a JSON response
        if service:
            return jsonify(service)
        else:
            # If no service is found, return an error message and a 404 status code
            return jsonify({"error": "Service not found"}), 404
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to fetch all prices (accessible via HTTP GET requests)
@app.route(shortcut + "/prices/all", methods=["GET"])
def all_prices():
    """API endpoint to get all prices"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch all prices
        cursor.execute("SELECT * FROM prices")
        # Fetch all rows from the query result
        prices = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Return the prices data as a JSON response
        return jsonify(prices)
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to fetch the price of a specific service by service ID (accessible via HTTP GET requests)
@app.route(shortcut + "/serv_prices", methods=["GET"])
def price_id():
    """API endpoint to get a price by service ID"""
    # Check if the 'id' parameter is provided in the request URL
    if "id" in request.args:
        id = int(request.args["id"])  # Convert the 'id' parameter to an integer
    else:
        # If 'id' is not provided, return an error message and a 400 status code
        return jsonify({"error": "No id field provided. Please specify an id."}), 400

    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the price for the specified service ID
        cursor.execute("SELECT * FROM prices WHERE service_id = %s", (id,))
        # Fetch one row from the query result
        price = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # If a price is found, return it as a JSON response
        if price:
            return jsonify(price)
        else:
            # If no price is found, return an error message and a 404 status code
            return jsonify({"error": "Price not found"}), 404
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to fetch the most expensive service (accessible via HTTP GET requests)
@app.route(shortcut + "/expensiveservice", methods=["GET"])
def high_serv():
    """API endpoint to get the most expensive service"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the most expensive service
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price DESC 
            LIMIT 1
        """
        )
        # Fetch one row from the query result
        service = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # If a service is found, return it as a JSON response
        if service:
            return jsonify(service)
        else:
            # If no service is found, return an error message and a 404 status code
            return jsonify({"error": "No services found"}), 404
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to fetch the least expensive service (accessible via HTTP GET requests)
@app.route(shortcut + "/cheapestservice", methods=["GET"])
def low_serv():
    """API endpoint to get the least expensive service"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the least expensive service
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price ASC 
            LIMIT 1
        """
        )
        # Fetch one row from the query result
        service = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # If a service is found, return it as a JSON response
        if service:
            return jsonify(service)
        else:
            # If no service is found, return an error message and a 404 status code
            return jsonify({"error": "No services found"}), 404
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to sort services alphabetically (accessible via HTTP GET requests)
@app.route(shortcut + "/services/sort", methods=["GET"])
def sort_serv():
    """API endpoint to sort services alphabetically"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch services sorted by name in ascending order
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY s.name ASC
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Return the sorted services data as a JSON response
        return jsonify(services)
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define an API route to sort services by price (accessible via HTTP GET requests)
@app.route(shortcut + "/prices/sort", methods=["GET"])
def sort_price():
    """API endpoint to sort services by price"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch services sorted by price in ascending order
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price ASC
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Return the sorted services data as a JSON response
        return jsonify(services)
    except Exception as e:
        # If an error occurs, return a JSON response with the error message and a 500 status code
        return jsonify({"error": str(e)}), 500


# Define a web route to view all services in the browser (accessible via HTTP GET requests)
@app.route("/services", methods=["GET"])
def view_services():
    """Web route to view all services"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch all services and their prices
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the services.html template and pass the services data to it
        return render_template("services.html", services=services)
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Define a web route to view the most expensive service in the browser (accessible via HTTP GET requests)
@app.route("/expensive", methods=["GET"])
def most_expensive():
    """Web route to view the most expensive service"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the most expensive service
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price DESC 
            LIMIT 1
        """
        )
        # Fetch one row from the query result
        service = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the expensive.html template and pass the service data to it
        return render_template("expensive.html", service=service)
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Define a web route to view the least expensive service in the browser (accessible via HTTP GET requests)
@app.route("/cheapest", methods=["GET"])
def least_expensive():
    """Web route to view the least expensive service"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch the least expensive service
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price ASC 
            LIMIT 1
        """
        )
        # Fetch one row from the query result
        service = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the cheapest.html template and pass the service data to it
        return render_template("cheapest.html", service=service)
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Define a web route to view services sorted by name in the browser (accessible via HTTP GET requests)
@app.route("/sort_by_name", methods=["GET"])
def sort_by_name():
    """Web route to view services sorted by name"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch services sorted by name in ascending order
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY s.name ASC
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the sort_name.html template and pass the sorted services data to it
        return render_template("sort_name.html", services=services, sort_type="Name")
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Define a web route to view services sorted by price in the browser (accessible via HTTP GET requests)
@app.route("/sort_by_price", methods=["GET"])
def sort_by_price():
    """Web route to view services sorted by price"""
    try:
        # Create a database connection
        conn = get_db_connection()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)

        # Execute a SQL query to fetch services sorted by price in ascending order
        cursor.execute(
            """
            SELECT s.id, s.name as service, p.price 
            FROM services s 
            JOIN prices p ON s.id = p.service_id 
            ORDER BY p.price ASC
        """
        )
        # Fetch all rows from the query result
        services = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Render the sort_price.html template and pass the sorted services data to it
        return render_template("sort_price.html", services=services, sort_type="Price")
    except Exception as e:
        # If an error occurs, render the error.html template and pass the error message
        return render_template("error.html", error=str(e))


# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
