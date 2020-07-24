# ID 733686227684818946
# tokenNzMzNjg2MjI3Njg0ODE4OTQ2.Xxk-Iw.jDF9961Smhi8lVYN-6G2Dj3tuMMToken

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from dad_joke import *
from shakespeare_insults import *
from discord.ext.commands import BadArgument

# to add logging with logging module
# import logging

# logger=logging.getLogger('discord')
# logger.setLevel(logging.NOTSET)
# handler=logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)


deerank=commands.Bot(command_prefix='>')

@deerank.event                  # when it logs in
async def on_ready():
    print("deerank is ready")

@deerank.event
async def on_command_error(ctx, error):
    await ctx.send("An error occured and I can't figure out what it is. Please check whether your command had all the right parameters or no.")

@deerank.command()              # to make the bot logout
async def leave(ctx):
    try:
        if ctx.message.guild.owner_id==ctx.message.author.id:
            await deerank.close()
        else:
            await ctx.send("You are not authorised to kick me out!")
    except Exception as e:
        await ctx.send("An error occured. This will be logged for reference.")
        with open('deerank.log','a') as logger:
            logger.write(f"message: {ctx.message.content}\nlogged: {str(e)}\n\n")
    finally:
        pass

@deerank.command(aliases=['8ball'])         # 8ball
async def _8ball(ctx, *, question=None):
    try:
        if question==None:
            await ctx.send("Dear retard,\n Please ask me question after the >8ball command.")
        else:
            responses=['It is certain',
                        'It is decidedly so.',
                        'Without a doubt.',
                        'Yes – definitely.',
                        'You may rely on it.',
                        'As I see it, yes.',
                        'Most likely.',
                        'Outlook good.',
                        'Yes.',
                        'Signs point to yes.',
                        'Reply hazy, try again.',
                        'Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again.',
                        "Don't count on it.",
                        "My reply is no.",
                        'My sources say no.',
                        'Outlook not so good.',
                        'Very doubtful.']
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    except Exception as e:
        await ctx.send("An error occured. This will be logged for reference.")
        with open('deerank.log','a') as logger:
            logger.write(f"message: {ctx.message.content}\n logged: {str(e)}\n\n")
    finally:
        pass

@deerank.command()                                                              #still have to try
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if not member==None:
        try:
            cur_guild=ctx.message.guild
            if cur_guild.member(member.id):
                cur_guild_owner=ctx.message.guild.owner_id
                if ctx.message.author.id==cur_guild_owner:
                    await member.kick(reason=reason)
                else:
                    await ctx.send(f"{ctx.message.author.mention}, you are not classified to do that.\n Report any pussy fights to your superior, {ctx.message.guild.owner.mention}.")
        except:
            await ctx.send(f"An error occured. Please check whether the name of the member was spelt right. \nGiven Name:{member}")
    else:
        await ctx.send(f"Dear retard, mention the name of the person you'd like to deerank!")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(f"Dear {ctx.message.author.mention}, you are a retard. \nThere is no member that goes by that name in this guild.")

@deerank.command()                                                               #try
async def ban(ctx, member: discord.Member=None, *, reason=None):
    if not member==None:
        try:
            cur_guild_owner=ctx.message.guild.owner_id
            if ctx.message.author.id==cur_guild_owner:
                await member.ban(reason=reason)
            else:
                await ctx.send(f"{ctx.message.author.mention}, you are not classified to do that.\n Report any pussy fights to your superior, {ctx.message.guild.owner.mention}.")
        except:
            await ctx.send(f"An error occured. Please check whether the name of the member was spelt right. \nGiven Name:{member}")
    else:
        await ctx.send(f"Dear retard, mention the name of the person you'd like to banish!")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(f"Dear {ctx.message.author.mention}, you are a retard. \nThere is no member that goes by that name in this guild.")


@deerank.command()
async def dad_joke(ctx):
    try:
        the_joke=request_joke()
        if not the_joke==0:
            await ctx.send(f"{the_joke}")
        else:
            await ctx.send(f"You are your dad's greatest joke!")
    except:
        await ctx.send("Thou speaking the language of retards. \nThou may choose to try again.\nOr not.\n Whatever.")

@deerank.command()
async def df(ctx, member: discord.Member=None):
    try:
        if member==None:
            await ctx.send(f"{ctx.message.author.mention}, thou is a retard. You didn't tell me whom to unlease my wrath on!")
        else:
            new_insult=get_insult()
            await ctx.send(f"Dear {member.mention},\n{new_insult}")
    except:
        await ctx.send("Thou speaking the language of retards. \nThou may choose to try again.\nOr not.\n Whatever)")



f= open('deerank_bot.Token','r')  
token=f.read()
f.close() 

deerank.run(str(token))