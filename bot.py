# bot.py
import discord
from discord.ext import commands
from bot_google import text_from_image_google
from text_parser import parse, simple_format
from database_handler import *
from keys.discordToken import DISCORD_TOKEN
from datetime import datetime

TOKEN = DISCORD_TOKEN

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    initialize_database()
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_guild_join(guild):
    print("I joined a guild named " + guild.name)
    initialize_database()

@bot.command()
async def rank(ctx):

    if ctx.message.attachments:
        img_raw_text = text_from_image_google(ctx.message.attachments[0].url)
        parsed_text = parse(img_raw_text)
        formatted_text = simple_format(parsed_text)
        lifeskill_json = json.dumps(parsed_text) 
        date = datetime.now()
        date_string = date.strftime("%m/%d/%Y, %H:%M:%S")

        await ctx.send(formatted_text)

        nick = ctx.message.author
        server_name = ctx.message.guild.name
        server_id = get_server_id(server_name)

        # TODO compare with othr entries
        insert_entry(server_id, nick, lifeskill_json, date_string)

        print(ctx.message.author)
        print(ctx.message.created_at)
    else:
        await ctx.send("where my lvls at :c")

    #await ctx.message.delete()
    #await ctx.send(arg)

bot.run(TOKEN)