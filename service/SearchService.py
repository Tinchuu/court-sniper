from datetime import datetime
import json
from repository.SearchRepo import SearchRepo
import numpy

class SearchService:

    async def check_time(self, start: int, end: int, date: datetime):
        courts = []

        for hour in range(start, end):
            start_date = date.replace(hour=hour)
            end_date = date.replace(hour=hour + 1)

            current = []
            for i in range(1, 13):
                session_info = await self.query_court(start_date, end_date, i)
                current.append(not json.loads(session_info.content)["meta"]["error"])
            courts.append(numpy.where(numpy.array(current))[0].tolist())
        
        return courts


    async def query_court(self, start: datetime, end: datetime, court: int):
        search = SearchRepo()
        print("Inside search service ", start, end)
        result = await search.queryCourtAsync(start, end, court)
        return result

    async def list_bookings(self, start: datetime, end: datetime):
        search = SearchRepo()
        result = await search.getBookingsAsync(start, end)
        return result