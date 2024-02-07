'''Needs a doc string In your Python file, create a docstring with a brief introduction to your project.'''
'''2. Project Start
In your Python file, create a docstring with a brief introduction to your project.'''

import sqlite3
import pandas as pd
import pathlib
import logging
#from pathlib import Path


'''Logging is recommended for all script and notebook projects. Implement logging to enhance debugging and maintain a record of program execution.

Configure logging to write to a file named log.txt.
Log the start of the program using logging.info().
Log the end of the program using logging.info().
Log exceptions using logging.exception().
Log other major events using logging.info().
Log the start and end of major functions using logging.debug().'''
#Log information
# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

'''5. Database Creation and Schema Design
Create a new SQLite database file. Design a schema with at least two related 
tables, including foreign key constraints. Document the schema design in
your README.md. Keep each SQL statement in a separate file.'''

'''Implement SQL statements and queries to perform table 
creation, data insertion, data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.

Include the following SQL files:

create_tables.sql - create your database schema.
insert_records.sql - insert at least 10 records into each table.
update_records.sql - update 1 or more records in a table.
delete_records.sql - delete 1 or more records from a table.
query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - use WHERE to filter data based on conditions.
query_sorting.sql - use ORDER BY to sort data.
query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.'''


# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    #Mights not need this
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

'''7. Python and SQL Integration
Use Python to interact with the SQL database and execute SQL commands:'''
def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    #create_database()
    #create_tables()
    #insert_data_from_csv()

    db_filepath = 'project.db'

    # Create database schema and populate with data
    #execute_sql_from_file(db_filepath, 'sql\create_tables.sql')
    execute_sql_from_file(db_filepath, 'sql\\insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\update_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_aggregation.sql')
    #execute_sql_from_file(db_filepath, 'sql\query_filter.sql')
    #execute_sql_from_file(db_filepath, 'sql\query_sorting.sql')
    #execute_sql_from_file(db_filepath, 'sql\query_group_by.sql')
    #execute_sql_from_file(db_filepath, 'sql\query_join.sql')

    logging.info("All SQL operations completed successfully")



'''9. Conditional Script Execution
Ensure the main function only executes when the script is run directly, not when 
imported as a module by using standard boilerplate code.'''

if __name__ == "__main__":
    main()