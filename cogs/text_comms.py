import discord
from discord.ext import commands
from discord.ext.commands import BadArgument,MissingRequiredArgument
import random

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
        finally:
            pass
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Dear retard,\n Please ask me question after the >8ball command.")
        else:
            
