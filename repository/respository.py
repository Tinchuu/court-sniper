import requests
import datetime

class Repository:
    def __init__(self):
        self.url = "https://platform.aklbadminton.com/api/booking/feed"

    def getBookings(self, start: datetime.datetime, end: datetime.datetime):
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        params=f"?start={s}&end={e}"
        try:
            response = requests.get(self.url + params)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")