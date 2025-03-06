from .database_engine import get_engine
from sqlalchemy import text

def cancel(booking_id):
    engine = get_engine()

    delete_query = text("DELETE FROM bookings WHERE index = :booking_id")

    with engine.connect() as connection:
        connection.execute(delete_query, {"booking_id": booking_id})
        connection.commit() 

