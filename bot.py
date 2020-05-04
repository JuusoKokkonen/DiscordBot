import discord
from discord.ext import commands

TOKEN = "NzA2OTMxNTE4NTk3MTAzNjQ3.XrBoIg.5PRHcDDulAoL6M64DzXhbyP6vq4"
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def test(ctx):
    await ctx.send(xd())

@client.command()
async def close(ctx):
    await ctx.send("Shutting down")
    await client.logout()

def xd():
    return("Testing")
client.run(TOKEN)