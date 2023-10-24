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

            role_names = [role.name for role in ctx.author.roles]
            history = getHystoryFromSeasonUserHistory(ctx)
            embed = discord.Embed(title=getNicknameFromUserInfo(ctx),
                                  description=ctx.author.id)
            embed.add_field(name="소속", value=getTeamNameFromUserInfo(ctx), inline=True)
            embed.add_field(name="신분", value=getRankFromUserInfo(ctx), inline=True)
            embed.add_field(name="닉네임 변경권", value=getNickChangeCouponFromUserInfo(ctx), inline=True)
            embed.add_field(name="주포지션", value=getMainPositionFromUserInfo(ctx), inline=True)
            embed.add_field(name="부포지션", value=getSubPositionFromUserInfo(ctx), inline=True)
            if "감독" in role_names:
                embed.add_field(name="계약기간", value="감독 직책으로 미표기", inline=False)
            elif "FA (무소속)" in role_names:
                embed.add_field(name="계약기간", value="FA 신분으로 미표기", inline=False)
            else:
                text = (getStartDateFromContract(ctx) + " ~ " + getEndDateFromContract(ctx)
                        + " (총 " + str(getPeriodFromContract(ctx)) + " 일)")
                embed.add_field(name="계약기간", value=text, inline=False)
            career = getTotsFromCareerWithID(ctx.author.id)
            val = getValFromCareerValondorWithID(ctx.author.id)
            text = career + val
            if text == "":
                embed.add_field(name="커리어", value="기록 없음", inline=False)
            else:
                embed.add_field(name="커리어", value=text, inline=False)
            if history == "":
                embed.add_field(name="히스토리", value="기록 없음", inline=False)
            else:
                embed.add_field(name="히스토리", value=history, inline=False)


            embed2_msg = await ctx.send(embed=embed)

        else:
            await ctx.reply(config.notJoinText)


    @commands.command(name='토츠', pass_context=True)
    async def _awardTots(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='발롱도르', pass_context=True)
    async def _awardValondor(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='리그순위', pass_context=True)
    async def _awardValondor(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

async def setup(bot):
    await bot.add_cog(Body(bot))
