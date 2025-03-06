from .database_engine import get_engine
import pandas as pd


def booking_data(member_id):
    engine = get_engine()

    query = f"""SELECT * FROM bookings WHERE member_id={member_id}"""

    with engine.begin() as connection:
        return pd.read_sql(query, connection)


