# URL Storage DB

Storage is a simple Python script that allows you to manage URL addresses in an SQLite database for example DBeaver. The project enables creating a table in the database, adding new URLs, and displaying a list of links based on categories.

## Requirements

- Python 3.x
- Libraries:
  - `python-dotenv` - for loading environment variables from the `.env` file
  - `sqlite3` - for interacting with the SQLite database

## Installation

1. Clone or copy the repository to your device.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt

3. Create a .env file in the project root directory and define the DB_NAME environment variable with the SQLite database file name, e.g.:

    ```bash
    DB_NAME=storage_database.db
   
Usage
1. Creating the database table
To create a table in the database, use the following command:

    ```bash
    python main.py setup

This command will create the urls table in the database with the following structure:

    ```bash
    CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    category TEXT, 
    url TEXT
    );
2. Adding new URL addresses
To add a new URL to the database, use the command:

    ```bash
    python main.py add <category> <url>
Example:

    python main.py add Technology https://www.webszyk.pl
3. Displaying links from a specific category
To display all links from a specific category, use the following command:

    ```bash
    python main.py list <category>
Example:

    python main.py list Technology
The script will display all URLs assigned to the Technology category.

Dependencies
The project uses the following libraries:

- python-dotenv – for loading environment variables from the .env file
- sqlite3 – for interacting with the SQLite database

Install the dependencies by running:

    pip install python-dotenv

Project Structure:

- main.py – the main application script that handles all database operations.
- .env – configuration file to store environment variables (e.g. database name).
- database.py – module to interact with the SQLite database (contains the Database class).