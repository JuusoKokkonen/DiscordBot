import discord, requests, time, random
from discord.ext import commands

# Bot token
TOKEN = "NzA2OTMxNTE4NTk3MTAzNjQ3.XrBoIg.5PRHcDDulAoL6M64DzXhbyP6vq4"


# Command prefix that "activates" the commands
client = commands.Bot(command_prefix = "!")


# Checks if everything is working and bot started without problems
@client.event
async def on_ready():
    print("Bot is ready")


# Info command -- prints all commands and required arguments
@client.command()
async def info(ctx):
    ping_desc = "!ping -- shows your ping.\n"
    clear_desc = "!clear n -- clears n amount of chat messages. (default 5)\n"
    calc_desc = "!calc n1 op n2 -- insert 2 numbers and an operator. Example: !calc 70 * 123\n"
    image_desc = "!image x -- fetches an image using the searchword x. Example: !image dog\n"
    trivia_desc = "!trivia x -- fetch a trivia question and tells the correct answer x seconds later.\n"
    info_desc = "!info -- prints what you are reading right now.\n"
    close_desc = "!close -- shuts the bot down.\n"

    info_print = "All available commands:\n\n "+ping_desc+clear_desc+calc_desc+image_desc+trivia_desc+info_desc+close_desc
    await ctx.send(info_print)


# Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}ms")


# Clear bot messages command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


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


# Trivia command
@client.command()
async def trivia(ctx, duration, category=0, difficulty=""):
    if duration:
        await trivia_function(ctx, duration, category, difficulty)
    else:
        await ctx.send("Missing arguments. Please add duration for the question and optionally the question category. (Example input: !trivia 10)")


# Bot shut down
@client.command()
async def close(ctx):
    await ctx.send("Shutting down")
    await client.logout()



# Calculator function
def calculate(number1, operator, number2):
    try:   
        if isinstance(number1, int) == True:
            num1 = int(number1)
        else:
            num1 = float(number1)

        if isinstance(number2, int) == True:
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

# Fetch image function
def fetch_image(query):
    try:
        results = requests.get("https://api.unsplash.com/search/photos?page=1&query=" + query + "&client_id=yS-xA5p3NK56qj3ilGqVjfHKtjytcQY72tcTZ6_MyOU")
        json_results = results.json()
        try:
            return(json_results["results"][random.randint(0, 9)]["urls"]["regular"])
        except:
            return(json_results["results"][0]["urls"]["regular"])
    except:
        return("No images found :(")

# Trivia game function
async def trivia_function(ctx, duration, category, difficulty):
    if duration.isnumeric() == True:

        results = requests.get("https://opentdb.com/api.php?amount=1&category="+str(category)+"&type=multiple&difficulty="+difficulty)
        json_results = results.json()
        category = ""
        question = ""
        right_answer = ""
        answers = []


        category = (json_results["results"][0]["category"])
        question = (json_results["results"][0]["question"])
        right_answer = (json_results["results"][0]["correct_answer"])
        answers.append(right_answer)
        answers.append(json_results["results"][0]["incorrect_answers"][0])
        answers.append(json_results["results"][0]["incorrect_answers"][1])
        answers.append(json_results["results"][0]["incorrect_answers"][2])
            

        question_string = "Category: "+category+"\n"+question+"\n\n"
        i = 1
        while len(answers) > 0:
            index = random.randint(0, (len(answers)-1))
            question_string += str(i)+". "+answers[index]+"\n"
            i += 1
            del answers[index]
        await ctx.send(question_string)


        await ctx.send("Correct answer in " + duration + " seconds.")


        answer_time = int(duration)
        while answer_time > 0:
            answer_time -= 1
            time.sleep(1)


        await ctx.send("Correct answer was: "+right_answer)

    else:
        await ctx.send("Check your arguments")


client.run(TOKEN)