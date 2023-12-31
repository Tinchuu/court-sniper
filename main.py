import datetime
import json
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from commands.query_court import query_court
import requests
from models.booking import Booking
from typing import List

load_dotenv()

TOKEN = os.getenv("DTOKEN")
GUILD = os.getenv("GUILD")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')

    print(f'{bot.user}\n')

@bot.tree.command(name="speak")
async def speak(interaction: discord.Interaction):
    response = await query_court(interaction)
    await response

@bot.tree.command(name="query_courts", description="Checks in the weeks what courts are free in the specified time frame.")
async def query_courts(interaction: discord.Interaction, start_time: int, end_time: int):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=1)

    start = start.replace(hour=start_time)
    end = end.replace(hour=end_time)

    embed = discord.Embed(title="Result", url="https://platform.aklbadminton.com/booking", description="List of courts", color=0xff0000)

    for _ in range(7):
        url = "https://platform.aklbadminton.com/api/booking/feed"
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        params=f"?start={s}&end={e}"
        response = requests.get(url + params)

        bookings_list: List[Booking] = []
        courts_list = [] 

        for booking_dict in json.loads(response.content):
            bookings_list.append(Booking.from_dict(booking_dict))

        print(url + params)

        embed.add_field(name="undefined", value=json.loads(response.content)[0], inline=False)

        start = end
        end = end = start + datetime.timedelta(days=1)

    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)

