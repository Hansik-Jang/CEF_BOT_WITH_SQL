import discord
from discord.ext import commands
import random

class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='팀추첨', pass_context=True)
    async def _select(self, ctx):
        team = ['RMA', 'CFC', 'MCI', 'INT', 'LIE', 'TOT', 'SUN']
        names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        li = []
        for name in names:
            temp = ''
            cho = random.choice(team)
            temp = name + ' - ' + cho
            li.append(temp)
            team.remove(cho)

        for l in li:
            await ctx.send(content=f"{l}")


def setup(bot):
    bot.add_cog(Transfer(bot))