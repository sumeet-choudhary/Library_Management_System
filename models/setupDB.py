import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Modify these with your MySQL credentials
hostname = os.getenv("DB_HOST")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# SQL script for creating the databases and tables
sql_scripts = [
    '''
    CREATE DATABASE IF NOT EXISTS librarydb;
    ''',
    '''
    USE librarydb;
    ''',
    '''
    CREATE TABLE IF NOT EXISTS books (
        id INT(11) NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        average_rating FLOAT NULL,
        isbn VARCHAR(10) NOT NULL,
        isbn13 VARCHAR(13) NOT NULL,
        language_code VARCHAR(3) NOT NULL,
        num_pages INT(5) NOT NULL,
        ratings_count INT(11) NOT NULL,
        text_reviews_count INT(11) NOT NULL,
        publication_date DATE NOT NULL,
        publisher VARCHAR(255) NOT NULL,
        total_quantity INT(11) NOT NULL,
        available_quantity INT(11) NOT NULL,
        rented_count INT(11) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB;
    ''',
    '''
    CREATE DATABASE IF NOT EXISTS librarytestdb;
    ''',
    '''
    USE librarytestdb;
    ''',
    '''
    CREATE TABLE IF NOT EXISTS books (
        id INT(11) NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        average_rating FLOAT NULL,
        isbn VARCHAR(10) NOT NULL,
        isbn13 VARCHAR(13) NOT NULL,
        language_code VARCHAR(3) NOT NULL,
        num_pages INT(5) NOT NULL,
        ratings_count INT(11) NOT NULL,
        text_reviews_count INT(11) NOT NULL,
        publication_date DATE NOT NULL,
        publisher VARCHAR(255) NOT NULL,
        total_quantity INT(11) NOT NULL,
        available_quantity INT(11) NOT NULL,
        rented_count INT(11) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB;
    '''
]

try:
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Execute each SQL script
        for sql_script in sql_scripts:
            cursor.execute(sql_script)

        print("Databases and tables created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
