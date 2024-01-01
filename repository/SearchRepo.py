import requests
from datetime import datetime
class SearchRepo:
    def __init__(self):
        self.url = "https://platform.aklbadminton.com/api"

    async def getBookings(self, start: datetime, end: datetime) -> requests.Response:
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        params = f"?start={s}&end={e}"
        try:
            response = await requests.get(self.url + "/booking/feed" + params)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    async def queryCourt(self, start: datetime, end: datetime, court: int) -> requests.Response:
        s = start.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        e = end.strftime("%Y-%m-%dT%H") + "%3A00%3A00"
        params = f"?start={s}&end={e}&facility={court}" 
        try:
            response = await requests.get(self.url + "/booking/estimate" + params)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")