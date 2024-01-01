import json
import discord
from datetime import datetime
from service.SearchService import SearchService

async def check_session_availability(interaction: discord.Interaction, start: int, end: int, session: int, date: datetime):
    search = SearchService()
    start_date = date.replace(hour=start)
    end_date = date.replace(hour=end)

    print(start_date)
    print(end_date)

    try:
        session_info = await search.query_court(start_date, end_date, 1)
        await interaction.response.send_message(session_info.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        await interaction.response.send_message("An error occurred while checking session availability.")
