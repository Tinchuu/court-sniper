import json
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from commands.check_session_availability import check_session_availability
import requests
from models.booking import Booking
from typing import List
from models.Month import Month
from models.TimeOptions import TimeOptions
from datetime import datetime, timedelta

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

async def parse_date(interaction: discord.Interaction, month: Month, day: int) -> datetime:
    today = datetime.now()
    try:
        date = datetime(today.year, month.value, day)
        return date
    except ValueError as e:
        await interaction.response.send_message("An invalid date was parsed.", delete_after=5)
        return

@bot.tree.command(name="check_session", description="Check whether a session is free")
async def check_session(interaction: discord.Interaction, start: int, end: int, session: int, month: Month, day: int):
    date = parse_date(interaction, month, day)
    format_date = date.strftime("%A %d %b")
    await interaction.response.send_message(f"Request for session date: {format_date}")
    await check_session_availability(interaction, start, end, session, date)


@bot.tree.command(name="monitor_session", description="Constantly checks for a session in the designated time")
async def query_courts(interaction: discord.Interaction, start: int, end: int, session: int, month: Month, day: int):
    date = date = parse_date(interaction, month, day)
    format_date = date.strftime("%A %d %b")
    await interaction.response.send_message(f"Request for session date: {format_date}")
    await check_session_availability(interaction, start, end, session, date)

bot.run(TOKEN)

