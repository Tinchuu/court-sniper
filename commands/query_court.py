import datetime
from repository import respository

def query_court(start: datetime.datetime, end: datetime.datetime):
    repo = respository.Repository()
    result = repo.getBookings(start, end)
    
