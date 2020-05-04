import discord
from discord.ext import commands

TOKEN = "NzA2OTMxNTE4NTk3MTAzNjQ3.XrBbnw.Ho8-50eg_fHKcQImhCXhiwDg4jM"
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready")

client.run(TOKEN)