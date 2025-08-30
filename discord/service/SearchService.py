from datetime import datetime
import json

from typing import List
from requests import Response
from repository.SearchRepo import SearchRepo
import numpy


class SearchService:
    search = SearchRepo()

    async def check_time(self, start: int, end: int, date: datetime) -> List[list]:
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

    async def query_court(self, start: datetime, end: datetime, court: int) -> Response:
        print("Inside search service ", start, end)
        result = await self.search.query_courts_async(start, end, court)
        return result

    async def list_bookings(self, start: datetime, end: datetime) -> Response:
        result = await self.search.get_bookings_async(start, end)
        return result
