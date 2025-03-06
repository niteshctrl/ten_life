from .database_engine import get_engine
from datetime import datetime
from sqlalchemy import text

def make(member_id, inventory_id):
    engine = get_engine()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    insert_query = text("INSERT INTO booking (member_id, datetime, inventory_id) VALUES (:member_id, :datetime, :inventory_id)"), {"member_id": member_id, "datetime": current_time, "inventory_id": inventory_id}
    
    with engine.connect() as connection:
        connection.execute(insert_query)
        connection.commit()



