import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
import os
from sqlalchemy import create_engine

def inventory():
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(override=True, dotenv_path=str(BASE_DIR) + "/.env")

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    con = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(con)

    query = f"""SELECT * FROM inventory"""

    with engine.begin() as connection:
        return pd.read_sql(query, connection)
    
