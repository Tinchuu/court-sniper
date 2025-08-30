import discord
from datetime import datetime
from service.SearchService import SearchService

def convert_time_format(num: int) -> str:
    if num > 12:
        return f"{num % 12}:00 pm"
    elif num == 0:
        return "12:00 am"
    elif num == 12:
        return "12:00 pm"
    else:
        return f"{num}:00 am"

# Should return a bool to indicate if the session is viable
async def check_session_availability(channel: discord.channel.TextChannel, start: int, end: int, session: int, date: datetime) -> bool:
    search = SearchService()
    display_date = date.strftime("%A %d %b")
    start_time = convert_time_format(start)
    end_time = convert_time_format(end)
    embed = discord.Embed(title=f"{display_date}", url="https://platform.aklbadminton.com/booking", description=f"List of free courts between {start_time} and {end_time}", color=0xff0000)

    courts = await search.check_time(start, end, date)


    time_display = []
    for time in courts:
        current_display = ""

        if len(time) == 0:
            time_display.append("No free courts.")
            continue

        for court in time:
            current_display += f"{court + 1}, "

        time_display.append(current_display.rstrip(", "))

    try:
        index = 0
        for i in range(start, end):
            embed.add_field(name=f"Time: {convert_time_format(i)} - {convert_time_format(i + 1)}", value=time_display[index], inline=False)
            index += 1
        await channel.send(embed=embed)

    except Exception as e:
        print(f"An error occurred: {e}")
        await channel.send("An error occurred while checking session availability.")
        return False
