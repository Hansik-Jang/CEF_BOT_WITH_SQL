import discord
from discord.ext import commands
import myfun
from discord.utils import get
from forAccessDB import *
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

    # 미완
    @commands.command(name="이적", pass_context=True)
    async def _transfer(self, ctx, member:discord.Member, abbTeamName):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            if checkUseJoinCommandWithID(member.id):
                if abbTeamName is not None:
                    teamRole = get(ctx.guild.roles, name=abbTeamName)
                    await member.add_roles(teamRole)
                else:
                    await ctx.reply("잘못된 팀 이름입니다.\n"
                                    "사용방법 : %이적 @멘션 팀약자", delete_after=15)
            else:
                await ctx.reply("해당 인원은 등록되지 않는 인원입니다.", delete_after=15)
        else:
            await ctx.reply("해당 명령어는 스태프만 사용 가능합니다.", delete_after=15)

async def setup(bot):
    await bot.add_cog(Transfer(bot))