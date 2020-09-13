# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from bot_google import text_from_image_google
from text_parser import parse, simple_format
from keys.discordToken import DISCORD_TOKEN

TOKEN = DISCORD_TOKEN

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def rank(ctx):
    if ctx.message.attachments:
        img_raw_text = text_from_image_google(ctx.message.attachments[0].url)
        parsed_text = parse(img_raw_text)
        formatted_text = simple_format(parsed_text)
        await ctx.send(formatted_text)
        print(ctx.message.user)
    else:
        await ctx.send("where my lvls at :c")

    #await ctx.message.delete()
    #await ctx.send(arg)

bot.run(TOKEN)