import os
from dotenv import load_dotenv
from psycopg2 import sql, connect, Error


class CreateDatabase:
    def __init__(self, server_config):
        self.server_config = server_config
        self.db_config = server_config.copy()
    
    def create_db(self, DB_NAME):
        try:
            # Connect to the PostgreSQL server (default database is usually 'postgres')
            conn = connect(**self.server_config)
            conn.autocommit = True  # Enable autocommit to avoid transaction errors
            with conn.cursor() as cur:
                # Create the database
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
                print(f"Database '{DB_NAME}' created successfully.")
            conn.close()  # Close the connection to the default database
            self.db_config["dbname"] = DB_NAME  # Add the new database name to the connection config
        except Error as e:
            print(f"Error: {e}")

    def create_table(self, NAME_TABLE):
        # SQL for creating the 'nav' table
        create_table_query = """
        CREATE TABLE nav (
            scheme_code INT,
            scheme_name VARCHAR(300),
            nav real,
            date date,
            PRIMARY KEY(scheme_code, date)
        );
        """
        with connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(create_table_query)
                print(f"Table '{NAME_TABLE}' created successfully in database.")
        if conn:
            conn.close()


if __name__=="__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path relative to the script location
    dotenv_path = os.path.join(script_dir, '../../.env')
    load_dotenv(override=True, dotenv_path=dotenv_path)


    NAME_DB = os.getenv("DB_NAME")
    NAME_TABLE = os.getenv("DB_TABLE")

    server_config = {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "user": os.getenv("DB_USER"),  # Replace with your PostgreSQL username
        "password": os.getenv("DB_PASSWORD")  # Replace with your PostgreSQL password
    }

    object = CreateDatabase(server_config)
    object.create_db(NAME_DB)
    object.create_table(NAME_TABLE)