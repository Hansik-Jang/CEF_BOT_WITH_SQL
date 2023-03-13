import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
import myfun
import random


class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='바르샤', pass_context=True)
    async def _insert_information(self, ctx):
        print('a')
        fcb = get(ctx.guild.roles, name="FC Barcelona")
        for member in fcb.members :
            data_list = [member.id, myfun.getNickFromDisplayname2(member.display_name), 0]
            await ctx.send(content=f"{data_list}")

    @commands.command(name='출석체크', pass_context=True)
    async def _check(self, ctx):
        conn = sqlite3.connect("FCB.db")
        cur = conn.cursor()


def setup(bot):
    bot.add_cog(Check(bot))
