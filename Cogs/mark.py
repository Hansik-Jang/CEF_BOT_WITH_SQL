import discord
from discord.ext import commands

class Mark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='출석테스트', pass_context=True)
    async def _test(self, ctx):
        await ctx.send("출석테스트")


async def setup(bot):
    await bot.add_cog(Mark(bot))