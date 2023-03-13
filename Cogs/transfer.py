import discord
from discord.ext import commands
import myfun
from discord.utils import get
import random

class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='팀추첨', pass_context=True)
    async def _select(self, ctx):
        fcb = get(ctx.guild.roles, name="FC Barcelona")
        for member in fcb.members:
            data_list = [member.id, myfun.getNickFromDisplayname2(member.display_name), 0]
            print(data_list)


def setup(bot):
    bot.add_cog(Transfer(bot))