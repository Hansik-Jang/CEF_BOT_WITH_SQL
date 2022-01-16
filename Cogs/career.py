import discord
from discord.ext import commands
import gspread

import myfun


class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='커리어테스트', pass_context=True)
    async def _test(self, ctx):
        await ctx.send("커리어테스트")
        await ctx.send(myfun.getNickFromDisplayname(ctx.author.display_name))

def setup(bot):
    bot.add_cog(Body(bot))
