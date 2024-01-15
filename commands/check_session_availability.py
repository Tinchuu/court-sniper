import json
import discord
from datetime import datetime
from service.SearchService import SearchService

async def check_session_availability(interaction: discord.Interaction, start: int, end: int, session: int, date: datetime):
    search = SearchService()
    embed = discord.Embed(title="Result", url="https://platform.aklbadminton.com/booking", description="List of courts", color=0xff0000)

    await interaction.response.send_message("Ok.")

    courts = await search.check_time(start, end, date)

    try:
        index = 0
        for i in range(start, end):
            embed.add_field(name=f"Time: {i}", value=courts[index], inline=False)
            index += 1
        await interaction.followup.send(embed=embed)

    except Exception as e:
        print(f"An error occurred: {e}")
        await interaction.followup.send("An error occurred while checking session availability.", delete_after=5)
