import discord
from discord.ext import commands
from discord.ext.commands import BadArgument,MissingRequiredArgument

class Admin(commands.Cog):
    def __init__(self, client):
        self.client=client
    
    def logging_error(self,ctx, error):
        with open('deerank.log','a') as logger:
            logger.write(f"message: {ctx.message.content}\nlogged: {str(error)}\n\n")

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command()
    async def leave(self, ctx):
        try:
            if ctx.message.guild.owner_id==ctx.message.author.id:
                await ctx.send("Alright, i'll leave. It's your loss anyway!")
                await self.client.close()
            else:
                await ctx.send('You are not authorized to kick me out.')
        except Exception as e:
            await ctx.send("An error occured. This will be logged for reference.")
            self.client.logging_error(ctx, e)
        finally:
            pass
    
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        cur_guild=ctx.message.guild
        if cur_guild.member(member.id):
            cur_guild_owner=ctx.message.guild.owner_id
            if ctx.message.author.id==cur_guild_owner:
                await member.kick(reason=reason)
            else:
                await ctx.send(f"{ctx.message.author.mention}, you are not classified to do that.\n Report any pussy fights to your superior, {ctx.message.guild.owner.mention}.")
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Dear {ctx.message.author.mention}, you are a retard. \nThere is no member that goes by that name in this guild.")
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("missing name")
            else:
                await ctx.send("An Error occured. This will be logged for further reference.")
                self.client.logging_error(ctx, error)
    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason):
        cur_guild=ctx.message.guild
        if cur_guild.member(member.id):
            cur_guild_owner=ctx.message.guild.owner_id
            if ctx.message.author.id==cur_guild_owner:
                await member.ban(reason=reason)
            else:
                await ctx.send(f"{ctx.message.author.mention}, you are not classified to do that.\n Report any pussy fights to your superior, {ctx.message.guild.owner.mention}.")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Dear {ctx.message.author.mention}, you are a retard. \nThere is no member that goes by that name in this guild.")
        else:
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Dear retard, mention the name of the person you'd like to banish!")
            else:
                await ctx.send("An Error occured. This will be logged for further reference.")
                self.client.logging_error(ctx, error)
    
def setup(client):
    client.add_cog(Admin(client))