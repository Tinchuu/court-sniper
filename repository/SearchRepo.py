from datetime import datetime
from requests import Response
import requests
import asyncio

class SearchRepo:
    def __init__(self):
        self.url = "https://platform.aklbadminton.com/api"
    
    def request(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

    def get_bookings(self, start: datetime, end: datetime) -> Response:
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        params = f"?start={s}&end={e}"
        self.request((self.url + "/booking/feed" + params))

    def query_court(self, start: datetime, end: datetime, court: int) -> Response:
        s = start.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        e = end.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        params = f"?start={s}&end={e}&facility={court}" 
        self.request((self.url + "/booking/feed" + params))

    async def get_bookings_async(self, start: datetime, end: datetime) -> Response:
        return await asyncio.to_thread(self.get_bookings, start, end)

    async def query_courts_async(self, start: datetime, end: datetime, court: int) -> Response:
        return await asyncio.to_thread(self.query_court, start, end, court)
