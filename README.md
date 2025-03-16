# Hair Salon Flask Web Application - The Boujee Salon
![alt text](image.png)

A Flask web application for managing hair salon services and pricing, allowing users to view, search, and sort services. It uses MySQL for data storage and provides a RESTful API for easy access.

## Features

* View all services and prices
* Sort services by name or price
* Find the most and least expensive services
* RESTful API for interacting with services and prices

## Tech Stack

* **Backend**: Flask
* **Database**: MySQL
* **Frontend**: HTML/CSS/JavaScript
* **Tools**: Postman (API testing), XAMPP (for local MySQL database)

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- XAMPP or MySQL server
- pip (Python package manager)

### Database Setup

1. Install XAMPP and start Apache and MySQL from the XAMPP control panel
2. Create a MySQL database called `boujee_salon`
3. Configure the database using the provided schema.sql file:
   ```
   mysql -u root -p boujee_salon < schema.sql
   ```

### Application Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/hairsalon-web-app.git
   cd hairsalon-web-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   # On Windows
   set FLASK_APP=app.py
   set FLASK_ENV=development
   # On macOS/Linux
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. Update the database configuration in `config.py` with your MySQL credentials.

6. Run the application:
   ```
   flask run
   ```

7. Access the application at http://localhost:5000

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/services` | GET | Get all services |
| `/api/services/<id>` | GET | Get service by ID |
| `/api/services` | POST | Add a new service |
| `/api/services/<id>` | PUT | Update a service |
| `/api/services/<id>` | DELETE | Delete a service |
| `/api/services/sort/name` | GET | Get services sorted by name |
| `/api/services/sort/price` | GET | Get services sorted by price |
| `/api/services/most-expensive` | GET | Get the most expensive service |
| `/api/services/least-expensive` | GET | Get the least expensive service |

## Usage Examples

### Web Interface

1. Navigate to http://localhost:5000 to view the main page
2. Click on "Services" to view all available salon services
3. Use the search bar to find specific services
4. Click on column headers to sort by name or price

### API Usage

Example API request using curl:

```
# Get all services
curl -X GET http://localhost:5000/api/services

# Add a new service
curl -X POST http://localhost:5000/api/services \
  -H "Content-Type: application/json" \
  -d '{"name":"Premium Haircut", "price":65.00, "duration":45, "category":"Haircut"}'
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

* Flask documentation
* MySQL documentation
* Bootstrap for responsive design
* FontAwesome for icons