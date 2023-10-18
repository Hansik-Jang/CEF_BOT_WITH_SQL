import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import sqlite3
import myfun


class League(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='내전리그이모지초기화', pass_context=True)
    async def _erageimojiaboutNaeJeon(self, ctx):
        for member in ctx.guild.members:
            print(member.display_name)



async def setup(bot):
    await bot.add_cog(League(bot))