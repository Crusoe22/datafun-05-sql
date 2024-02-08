'''Using python code implement SQL statements and queries to perform table creation, data insertion, data querying (with filters, 
sorting, and joining tables), data aggregation, and record update and deletion.'''

import sqlite3
import logging


# Configure logging to write to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")

def execute_sql_from_file(db_filepath, sql_file):
    # Python codre to interact with the SQL database and execute SQL commands
    logging.debug("Starting major_function")
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
        logging.debug("Ending major_function")

def main():
    logging.debug("Starting major_function")

    db_filepath = 'project.db'

    # Create database schema and edit data
    execute_sql_from_file(db_filepath, 'sql\\create_tables.sql')
    execute_sql_from_file(db_filepath, 'sql\\insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\update_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql\\query_join.sql')

    logging.info("All SQL operations completed successfully")
    logging.debug("Ending major_function")
    
logging.info("Program ended")

if __name__ == "__main__":
    main()