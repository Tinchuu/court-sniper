from datetime import datetime
from repository.SearchRepo import SearchRepo

class SearchService:

    async def query_court(self, start: datetime, end: datetime, court: int):
        search = SearchRepo()
        print("Inside search service ", start, end)
        result = await search.queryCourtAsync(start, end, court)
        return result

    async def list_bookings(self, start: datetime, end: datetime):
        search = SearchRepo()
        result = await search.getBookingsAsync(start, end)
        return result