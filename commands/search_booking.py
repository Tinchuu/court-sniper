import datetime
from repository import SearchRepo
import asyncio

async def list_bookings(start: datetime.datetime, end: datetime.datetime):
    repo = SearchRepo.SearchRepo()
    result = await asyncio.create_task(repo.get_bookings(start, end))
    return result