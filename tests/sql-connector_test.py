import pymysql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print environment variables for debugging
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_PORT:", os.getenv("DB_PORT"))

# Database connection details from .env
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "boujee_salon"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "cursorclass": pymysql.cursors.DictCursor,
}

try:
    # Attempt to connect to the database
    print("Connecting to MySQL...")
    conn = pymysql.connect(**db_config)
    print("Connected to MySQL database!")
    conn.close()
except pymysql.Error as e:
    print("MySQL Error:", e)
except Exception as e:
    print("General Error:", e)
