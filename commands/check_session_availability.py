import json
import discord
from datetime import datetime
from service.SearchService import SearchService

def convert_time_format(num: int):
    if num >= 12:
        return f"{num % 12}:00 pm"
    elif num == 0:
        return "12:00 am"
    else:
        return f"{num}:00 am"

async def check_session_availability(interaction: discord.Interaction, start: int, end: int, session: int, date: datetime):
    search = SearchService()
    display_date = date.strftime("%A %d %b")
    start_time = convert_time_format(start)
    end_time = convert_time_format(end)
    embed = discord.Embed(title=f"{display_date}", url="https://platform.aklbadminton.com/booking", description=f"List of courts between {start_time} and {end_time}", color=0xff0000)

    courts = await search.check_time(start, end, date)

    try:
        index = 0
        for i in range(start, end):
            embed.add_field(name=f"Time: {convert_time_format(i)}", value=courts[index], inline=False)
            index += 1
        await interaction.followup.send(embed=embed)

    except Exception as e:
        print(f"An error occurred: {e}")
        await interaction.followup.send("An error occurred while checking session availability.")
