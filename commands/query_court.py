import datetime
import json
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests
from models.booking import Booking
from typing import List

async def query_court(interaction: discord.Interaction, start: int, end: int, session: int):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=1)

    start = start.replace(hour=6)
    end = end.replace(hour=12)

    url = "https://platform.aklbadminton.com/api/booking/feed"
    s = start.strftime("%Y-%m-%d")
    e = end.strftime("%Y-%m-%d")
    params=f"?start={s}&end={e}"
    response = requests.get(url + params)

    print(url + params)

    return interaction.response.send_message(json.loads(response.content)[0])
