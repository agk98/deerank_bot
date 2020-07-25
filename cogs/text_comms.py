import discord
from discord.ext import commands
from discord.ext.commands import BadArgument,MissingRequiredArgument
import random
from dad_joke import *
from shakespeare_insults import *

class Text(commands.Cog):
    def __init__(self, client):
        self.client=client

    def logging_errors(self, ctx, error):
        with open('deerank.log','a') as logger:
            logger.write(f"message: {ctx.message.content}\nlogged: {str(error)}\n\n")

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        try:
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
            await ctx.send("An error occured. This will be logged for consideration.")
            self.logging_errors(ctx, e)
        finally:
            pass
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Dear retard,\n Please ask me question after the >8ball command.")
        else:
            await ctx.send("An error occured. This will be logged for consideration.")
            self.logging_errors(ctx,e)

    @commands.command()
    async def df(self, ctx, member:discord.Member):
        new_insult=get_insult()
        await ctx.send(f"Dear {member.mention},\n{new_insult}")

    @df.error
    async def df_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.message.author.mention}, thou is a retard. You didn't tell me whom to unlease my wrath on!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Dear {ctx.message.author.mention}, you are a retard. \nThere is no member that goes by that name in this guild.")
        else:
            await ctx.send("An error occured. This will be logged for future consideration.")
            self.logging_errors(ctx,e)
    
    @commands.command()
    async def dad_joke(self, ctx):
        new_joke=request_joke()
        if not new_joke==0:
            await ctx.send(f"{new_joke}")
        else:
            await ctx.send("I dont have a dad joke for you right now.")
    
    @dad_joke.error
    async def joke_error(self, ctx, error):
        await ctx.send("An error occured. This will be logged for consideration.")
        self.logging_errors(ctx, error)
    

def setup(client):
    client.add_cog(Text(client))
