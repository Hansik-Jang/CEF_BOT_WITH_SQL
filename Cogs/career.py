import discord
from discord.ext import commands
import gspread
import sqlite3
from forAccessDB import *
import config
import myfun


class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='내정보', pass_context=True)
    async def _myinformation(self, ctx):
        if checkUseJoinCommand(ctx):
            history = "24-1 '소속팀' '직책' '순위' 中 '전체 팀 수'\n" \
                      "(예시)\n" \
                      "24-1 FCB 감독 5위 中 16팀"
            career = getInforFromTotsFW(ctx)
            embed = discord.Embed(title=getNicknameFromUserInfo(ctx),
                                  description=ctx.author.id,
                                  color=getColorCodeFromTeamInfor(ctx))
            embed.add_field(name="소속", value=getTeamAbbNameFromTeamInfor(ctx), inline=True)
            embed.add_field(name="신분", value=getRankFromUserInfo(ctx), inline=True)
            embed.add_field(name="닉네임 변경권", value=getNickChangeCouponFromUserInfo(ctx), inline=True)
            embed.add_field(name="주포지션", value=getMainPositionFromUserInfo(ctx), inline=True)
            embed.add_field(name="부포지션", value=getSubPositionFromUserInfo(ctx), inline=True)
            embed.add_field(name="히스토리", value=history, inline=False)

            embed2_msg = await ctx.send(embed=embed)

        else:
            await ctx.reply(config.notJoinText)

    @commands.command(name='히스토리', pass_context=True)
    async def _history(self, ctx):
        if checkUseJoinCommand(ctx):
            await ctx.reply(getInfoFromSeasonUserHistory(ctx))
        else:
            await ctx.reply(config.notJoinText)


    @commands.command(name='커리어', pass_context=True)
    async def _career(self, ctx):

        if checkUseJoinCommand(ctx):
            await ctx.send(f"{getInforFromTotsFW(ctx)}")
        else:
            await ctx.reply(config.notJoinText)

async def setup(bot):
    await bot.add_cog(Body(bot))
