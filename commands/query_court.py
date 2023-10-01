import datetime
from repository import respository
import asyncio

async def query_court(start: datetime.datetime, end: datetime.datetime):
    repo = respository.Repository()

    result = asyncio.create_task(repo.getBookings(start, end))

    return result

