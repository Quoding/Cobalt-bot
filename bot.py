#!/usr/bin/env python3

"""bot.py : main Python file for Cobalt bot"""

__author__ = "Quoding"
__version__ = "0.1.0"
__maintainer__ = "Quoding"
__email__ = "quoding@protonmail.ch"

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from python_abstract_art.main import make_image
import io

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord")


@bot.command(help="Generate a dope-ass abstract picture, yo!")
async def genimg(ctx):
    img = make_image()

    with io.BytesIO() as image_binary:
        img.save(image_binary, "PNG")
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))


bot.run(TOKEN)
