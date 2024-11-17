# Hair Salon Web Application

## Project Description:
A Flask web app for managing hair salon services and pricing, allowing users to view, search, and sort services. It uses MySQL for data storage and provides an API for easy access.

## Features:
- View all services and prices
- Sort services by name or price
- Find the most and least expensive services
- API for interacting with services and prices

## Tech Stack:
- **Backend**: Flask
- **Database**: MySQL
- **Frontend**: HTML (rendered with Flask)
- **Tools**: Postman (API testing), XAMPP (for local MySQL database)

## Setup and Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hairsalon-web-app.git
   cd hairsalon-web-app
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database using XAMPP:
   - Install XAMPP and start Apache and MySQL from the XAMPP control panel.
   - Create a MySQL database called `boujee_salon` and configure the necessary tables (`services`, `prices`).

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Access the app locally at `http://localhost:5000`.

## Deployment Options:
You can deploy the app using either:

- **GitHub Pages** (for static content only):
  - Host the front-end (HTML, CSS, JS) on GitHub Pages. 
  - The backend API would need to be hosted elsewhere (e.g., using Heroku or a cloud provider).

- **ngrok** (for local development and testing):
  - Use ngrok to expose your local Flask app to the internet for testing.
  - Install ngrok and run `ngrok http 5000` to get a publicly accessible URL.

## API Testing with Postman:
Use Postman to test the API endpoints. Import the following collection or manually create requests for:
- **GET /api/v1/resources/services/all**: Fetch all services.
- **GET /api/v1/resources/services?id=<id>**: Fetch a service by ID.
- **GET /api/v1/resources/prices/all**: Fetch all prices.
- **GET /api/v1/resources/serv_prices?id=<id>**: Fetch a price by ID.
- **GET /api/v1/resources/expensiveservice**: Fetch the most expensive service.
- **GET /api/v1/resources/cheapestservice**: Fetch the least expensive service.
- **GET /api/v1/resources/services/sort**: Sort services alphabetically.
- **GET /api/v1/resources/prices/sort**: Sort services by price.

## Future Features:
- User authentication
- Online booking and payment system

## License:
This project is licensed under the MIT License.
