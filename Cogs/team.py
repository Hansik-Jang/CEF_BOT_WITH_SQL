import discord
from discord.ext import commands
import myfun
from discord.utils import get
from forAccessDB import *
import random
from datetime import datetime, timedelta

class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='팀등록', pass_context=True)
    async def _registerTeam(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            if checkUseJoinCommandWithID(ctx.author.id):

            else :
                await ctx.reply("```해당 인원은 등록되지 않는 인원입니다.```", delete_after=30)
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)
async def setup(bot):
    await bot.add_cog(Team(bot))