import discord
from discord.ext import commands
import random

class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='채널권한복사', pass_context=True)
    async def _copypermission(self, ctx):
        for role in ctx.guild.roles:
            pass


def setup(bot):
    bot.add_cog(Others(bot))