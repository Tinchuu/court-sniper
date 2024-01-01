from datetime import datetime
from repository import SearchRepo
import asyncio

class SearchService:


    async def query_court(self, start: datetime, end: datetime, court: int):
        repo = SearchRepo.SearchRepo()
        print("Inside search service ", start, end)
        result = asyncio.create_task(repo.queryCourt(start, end, court))
        return result

    async def list_bookings(self, start: datetime, end: datetime):
        repo = SearchRepo.SearchRepo()
        result = asyncio.create_task(repo.getBookings(start, end))
        return result