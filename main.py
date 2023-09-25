import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import requests

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
        if guild.name == GUILD:
            break

    print(
        f'{bot.user}\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.tree.command(name="speak")
async def speak(interaction: discord.Interaction):
    url = "https://platform.aklbadminton.com/api/booking/feed?start=2023-10-03&end=2023-10-04"
    response = requests.get(url)
    await interaction.response.send_message(response.iter_content[1])

bot.run(TOKEN)

