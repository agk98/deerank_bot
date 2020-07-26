import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import BadArgument,MissingRequiredArgument
import os


deerank=commands.Bot(command_prefix='>')


@deerank.command()
async def load(ctx, extension):
    deerank.load_extension(f"cogs.{extension}")

@deerank.command()
async def unload(ctx, extension):
    deerank.unload_extension(f'cogs.{extension}')


f= open('deerank_bot.Token','r')  
token=f.readline().split('=')[1][:-1]
f.close() 

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        deerank.load_extension(f'cogs.{filename[:-3]}')

deerank.run(str(token))