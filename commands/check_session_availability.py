import json
import discord
from datetime import datetime
from service.SearchService import SearchService

async def check_session_availability(interaction: discord.Interaction, start: int, end: int, session: int, date: datetime):
    search = SearchService()
    start_date = date.replace(hour=start)
    end_date = date.replace(hour=end)

    embed = discord.Embed(title="Result", url="https://platform.aklbadminton.com/booking", description="List of courts", color=0xff0000)

    try:
        for i in range(1, 13):
            session_info = await search.query_court(start_date, end_date, i)
            embed.add_field(name=f"Court {i}", value=json.loads(session_info.content)["meta"]["error"], inline=False)
            
        await interaction.response.send_message(embed=embed)

    except Exception as e:
        print(f"An error occurred: {e}")
        await interaction.response.send_message("An error occurred while checking session availability.")
