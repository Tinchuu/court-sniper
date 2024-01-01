from datetime import datetime
import requests
import asyncio

class SearchRepo:
    def __init__(self):
        self.url = "https://platform.aklbadminton.com/api"

    def getBookings(self, start: datetime, end: datetime) -> requests.Response:
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        params = f"?start={s}&end={e}"
        try:
            response = requests.get(self.url + "/booking/feed" + params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

    def queryCourt(self, start: datetime, end: datetime, court: int) -> requests.Response:
        s = start.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        e = end.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        params = f"?start={s}&end={e}&facility={court}" 
        try:
            response = requests.get(self.url + "/booking/estimate" + params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

    async def getBookingsAsync(self, start: datetime, end: datetime) -> requests.Response:
        return await asyncio.to_thread(self.getBookings, start, end)

    async def queryCourtAsync(self, start: datetime, end: datetime, court: int) -> requests.Response:
        return await asyncio.to_thread(self.queryCourt, start, end, court)
