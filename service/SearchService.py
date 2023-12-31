import datetime
from repository import SearchRepo
import asyncio

class SearchService:
    

    async def query_court(start: datetime.datetime, end: datetime.datetime, court):
        repo = SearchRepo.SearchRepo()
        result = await asyncio.create_task(repo.queryCourt(start, end, 1))
        return result

    async def list_bookings(start: datetime.datetime, end: datetime.datetime):
        repo = SearchRepo.SearchRepo()
        result = await asyncio.create_task(repo.getBookings(start, end))
        return result