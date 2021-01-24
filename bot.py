# bot.py
import discord
import json
import sys # TESTING ONLY
from datetime import datetime

from discord.ext import commands
from bot_google import text_from_image_google


from keys.discordToken import DISCORD_TOKEN

from text_to_data_converter import parse
from data_to_text_converter import get_rank_message
from database_handler import *
from ranking_handler import *

# discord token
TOKEN = DISCORD_TOKEN

# command prefix
bot = commands.Bot(command_prefix="/")

# once per hosting machine
async def init():
    # initial datbase setup (creates tables)
    initialise_database()

# whenever bot activated 
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# kill bot TESTING ONLY
@bot.command()
async def die(ctx):
    sys.exit(1)

# command: rank - ranks the player based on image TODO add more commands and a better desc for this one
@bot.command()
async def rank(ctx):
    # server details
    server_name = ctx.guild.name
    server_id = get_server_id(server_name)
    # ensure server exists in database
    if server_id == None: 
        print("not in db, adding new to database")
        insert_server(server_name)
    # time details
    date = datetime.now()
    date_string = date.strftime("%m/%d/%Y, %H:%M:%S")
    # user details
    nick = ctx.message.author.name

    # process message attachments (image)
    if ctx.message.attachments:
        # extract image
        image_url = ctx.message.attachments[0].url
        # extract text using Vision API of choice
        raw_text = text_from_image_google(image_url) #GOOGLE API TODO add more APIs
        # parse text into lifeskill rank format (dict: skill -> level)
        parsed_text = parse(raw_text)

        # add to database and save entry locally
        lifeskill_json = json.dumps(parsed_text) 
        insert_entry(server_id, nick, lifeskill_json, date_string)
        current_entry = (server_id, nick, lifeskill_json, date_string)

        # pull local user data from database
        user_entries = get_local_newest_unique_player_entries(server_id)

        # rank user
        rank_dict = rank_user(user_entries, current_entry)

        #TODO format rank_dict
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embed.add_field(name="Your ranks are:", value=get_rank_message(rank_dict), inline=False)
        await ctx.send(embed=embed)

    else:
        await ctx.send("where my lvls at :c")

# self activation
bot.run(TOKEN)