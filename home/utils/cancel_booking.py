from .database_engine import get_engine
from sqlalchemy import text

def cancel(booking_id):
    engine = get_engine()

    delete_query = text("DELETE FROM bookings WHERE booking_id = :booking_id")

    inventory_increase = text(
        "UPDATE inventory SET remaining_count = remaining_count + 1 where index= (SELECT inventory_id from bookings WHERE booking_id = :booking_id)"
    )

    with engine.connect() as connection:
        connection.execute(inventory_increase, {"booking_id": booking_id})
        connection.execute(delete_query, {"booking_id": booking_id})
        connection.commit() 

