# ID 733686227684818946
# token NzMzNjg2MjI3Njg0ODE4OTQ2.XxGx0Q.kijzk6efHHcXccrLnDHs-pfQwFE

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from dad_joke import *
from shakespeare_insults import *

deerank=commands.Bot(command_prefix='>')


@deerank.event                  # when it logs in
async def on_ready():
    print("deerank is ready")

@deerank.command()              # to make the bot logout
async def leave(ctx):
    await deerank.close()

@deerank.command()              # pinging
async def ping(ctx):
    await ctx.send(f'Pong!\n {round(deerank.latency * 1000)}ms')

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
                        ' As I see it, yes.',
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
    except:
        await ctx.send("An Except occured. Try again.")

@deerank.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@deerank.command()                                                              #still have to try
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if not member==None:
        try:
            cur_guild_owner=ctx.message.guild.owner_id
            if ctx.message.author.id==cur_guild_owner:
                await member.kick(reason=reason)
            else:
                await ctx.send(f"{ctx.message.author.mention}, you are not classified to do that.\n Report any pussy fights to your superior, {ctx.message.guild.owner.mention}.")
        except:
            await ctx.send(f"An error occured. Please check whether the name of the member was spelt right. \nGiven Name:{member}")
    else:
        await ctx.send(f"Dear retard, mention the name of the person you'd like to deerank!")

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

@deerank.command(pass_context=True)
async def df(ctx, member: discord.Member=None):
    try:
        if member==None:
            await ctx.send(f"{ctx.message.author.mention}, thou is a retard. You didn't tell me whom to unlease my wrath on!")
        else:
            new_insult=get_insult()
            await ctx.send(f"Dear {member.mention},\n{new_insult}")
    except:
        await ctx.send("Thou speaking the language of retards. \nThou may choose to try again.\nOr not.\n Whatever)")




deerank.run('NzMzNjg2MjI3Njg0ODE4OTQ2.XxGx0Q.kijzk6efHHcXccrLnDHs-pfQwFE')