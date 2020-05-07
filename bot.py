import discord
from discord.ext import commands
import requests
import random

TOKEN = "NzA2OTMxNTE4NTk3MTAzNjQ3.XrBoIg.5PRHcDDulAoL6M64DzXhbyP6vq4"
client = commands.Bot(command_prefix = "!")

# Checks if everything is working and bot started without problems
@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def help_test(ctx):
    await ctx.send("XD")


@client.command()
async def test(ctx):
    await ctx.send(xd())

# Calculator command
@client.command()
async def calc(ctx, number1=" ", operator="xd", number2=" "):
    if operator != "+" or "-" or "*" or "/":
        await ctx.send(calculate(number1, operator, number2))
    else:
        await ctx.send("""Argument error. Please insert first number, operator (+, -, *, /) and a second number separated by space. (Example input: 11.7 * 24.75)""")

# Image command
@client.command()
async def image(ctx, query):
    await ctx.send(fetch_image(query))

# Bot shut down
@client.command()
async def close(ctx):
    await ctx.send("Shutting down")
    await client.logout()


# Calculator function
def calculate(number1, operator, number2):
    try:   
        if isinstance(number1, int):
            num1 = int(number1)
        else:
            num1 = float(number1)

        if isinstance(number2, int):
            num2 = int(number2)
        else:
            num2 = float(number2)


        if operator == "+":
            return(num1 + num2)

        if operator == "-":
            return(num1 - num2)

        if operator == "*":
            return(num1 * num2)

        if operator == "/":
            return(num1 / num2)
    except:
        return("""Error! check the arguments and use "." instead of "," when using decimal numbers. (Example input: 11.7 * 24.75) """)

# Fetch image
def fetch_image(query):
    try:
        results = requests.get("https://api.unsplash.com/search/photos?page=1&query=" + query + "&client_id=yS-xA5p3NK56qj3ilGqVjfHKtjytcQY72tcTZ6_MyOU")
        json_results = results.json()
        return(json_results["results"][random.randint(0, 9)]["urls"]["regular"])
    except:
        return("No images found :(")

def xd():
    return("Testing")

client.run(TOKEN)