import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def csv_to_DB(members_path, inventory_path, connnection_url):
    '''
        Function to read CSV and push the data to Database
    '''
    members = pd.read_csv(members_path)
    inventory = pd.read_csv(inventory_path)
 
    engine = create_engine(connnection_url)
    with engine.begin() as conn:
        members.to_sql(name='members', con=conn, index=True)
        inventory.to_sql(name='inventory', con=conn, index=True)


if __name__ == "__main__":
    members_file_path = "files/members.csv"
    inventory_file_path = "files/inventory.csv"

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path relative to the script location
    dotenv_path = os.path.join(script_dir, '../../.env')
    load_dotenv(override=True, dotenv_path=dotenv_path)    
    
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    table = os.getenv("DB_TABLE")

    engine_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    csv_to_DB(members_file_path, inventory_file_path, engine_url) 