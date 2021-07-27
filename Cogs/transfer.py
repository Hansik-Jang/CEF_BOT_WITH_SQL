import discord
from discord.ext import commands

class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='이적테스트', pass_context=True)
    async def _test(self, ctx):
        await ctx.send("이적테스트")


def setup(bot):
    bot.add_cog(Body(bot))