import discord
from discord.ext import commands


class League(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='리그테스트', pass_context=True)
    async def _test(self, ctx):
        await ctx.send("리그테스트")


def setup(bot):
    bot.add_cog(League(bot))