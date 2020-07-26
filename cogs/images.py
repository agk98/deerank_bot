import discord
from discord.ext import commands
from discord.ext.commands import BadArgument, MissingRequiredArgument
import praw
import random
import asyncio

class Image(commands.Cog):
    def __init__(self, client):
        with open('deerank_bot.Token','r') as secrets:
            lines=secrets.readlines()
            for line in lines:
                line=line.split('=')
                if line[0]=='REDDIT_APP_ID':
                    REDDIT_APP_ID=line[1][:-1]
                else:
                    if line[0]=='REDDIT_APP_SECRET':
                        REDDIT_APP_SECRET=line[1][:-1]
        self.client=client
        self.reddit=praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="DeeRank_bot:%s:1.0"%REDDIT_APP_ID)

    
    def loggin_errors(self, ctx, error):
        with open('deerank.log','a') as logger:
            logger.write(f"message:{ctx.message.content}\nLogged:{str(error)}\n\n")
    
    @commands.command()
    async def memez(self, ctx, *, category=None):
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            if self.reddit:
                if category==None:
                    default_categories=['memes','funny','wholesomememes','dankmemes','raimimemes','historymemes','lastimages','okbuddyretard','comedyheaven']
                    chosen_subreddit=random.choice(default_categories)
                else:
                    chosen_subreddit=category
                submissions=self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick=random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission=next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)
            else:
                await ctx.send("Error occured!")
    @memez.error
    async def memes_error(self, ctx, error):
        await ctx.send("An error occured. This will be logged for future reference.")
        self.loggin_errors(ctx, error)
    
def setup(client):
    client.add_cog(Image(client))

