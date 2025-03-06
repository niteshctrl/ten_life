from datetime import datetime
from sqlalchemy import text, create_engine
from pathlib import Path
from dotenv import load_dotenv
import os


def get_engine():
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(override=True, dotenv_path=str(BASE_DIR) + "/.env")

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    con = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(con)
    
    return engine

def make(member_id, inventory_id):
    engine = get_engine()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    insert_query = text(
        "INSERT INTO bookings (member_id, datetime, inventory_id) VALUES (:member_id, :datetime, :inventory_id)"
    )
    
    inventory_reduce = text(
        "UPDATE inventory SET remaining_count = remaining_count - 1 where index= :inventory_id"
    )

    with engine.connect() as connection:
        connection.execute(insert_query, {"member_id": member_id, "datetime": current_time, "inventory_id": inventory_id})
        connection.execute(inventory_reduce, {"inventory_id": inventory_id})
        connection.commit()

