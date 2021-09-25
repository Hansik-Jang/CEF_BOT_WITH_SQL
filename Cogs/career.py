import discord
from discord.ext import commands
import gspread

class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='커리어테스트', pass_context=True)
    async def _test(self, ctx):
        await ctx.send("커리어테스트")


def setup(bot):
    bot.add_cog(Body(bot))
