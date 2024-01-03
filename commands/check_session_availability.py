import json
import discord
from datetime import datetime
from service.SearchService import SearchService

async def check_session_availability(interaction: discord.Interaction, start: int, end: int, session: int, date: datetime):
    search = SearchService()
    embed = discord.Embed(title="Result", url="https://platform.aklbadminton.com/booking", description="List of courts", color=0xff0000)

    await interaction.response.send_message("Ok.")

    courts = [x for x in range(end - start)] 
    index = 0
    consec = 0

    for hour in range(start, end):
        start_date = date.replace(hour=hour)
        end_date = date.replace(hour=hour + 1)
        courts[index] = []
        for i in range(1, 13):
            session_info = await search.query_court(start_date, end_date, i)
            courts[index].append(not json.loads(session_info.content)["meta"]["error"])
        index += 1
    

    for slot in courts:
        if any(slot):
            consec += 1
        else:
            consec = consec - 1 if consec > 0 else 0

    if consec >= session:
        print("The session is doable")

    try:
        embed.add_field(name=f"Court {i}", value=json.loads(session_info.content)["meta"]["error"], inline=False)
        await interaction.followup.send(courts)

    except Exception as e:
        print(f"An error occurred: {e}")
        await interaction.followup.send("An error occurred while checking session availability.", delete_after=5)
