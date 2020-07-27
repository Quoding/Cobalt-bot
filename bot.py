#!/usr/bin/env python3

"""bot.py : main Python file for Cobalt bot"""

__author__ = "Quoding"
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Quoding"
__email__ = "quoding@protonmail.ch"

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from polls import make_poll

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hey {member.name}, take a walk on the left side.")


@bot.command(name="poll", help="Create a poll. Usage: !poll [days, yesno]")
async def create_poll(ctx, preset):
    await ctx.message.delete()

    emojis, response = make_poll(preset)

    msg = await ctx.send(response)

    for emoji in emojis:
        await msg.add_reaction(emoji)


bot.run(TOKEN)
