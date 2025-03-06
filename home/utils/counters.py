# This will return count of remaining bookings for a members and Itinerary
from .database_engine import get_engine
import pandas as pd

def count(member_id, inventory_id):
    member_bookcount_query = f"""SELECT COUNT(*)
                                    FROM bookings
                                    WHERE member_id={member_id}"""
    
    inventory_count_query = f"""SELECT remaining_count
                                FROM inventory WHERE index={inventory_id}"""
    
    engine = get_engine()
    
    with engine.begin() as connection:
        member_bookcount = pd.read_sql(member_bookcount_query, connection).iloc[0, 0]
        inventory_count = pd.read_sql(inventory_count_query, connection).iloc[0, 0]

        return member_bookcount, inventory_count

