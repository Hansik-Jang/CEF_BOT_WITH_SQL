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
            else:
                text = (getStartDateFromContract(ctx) + " ~ " + getEndDateFromContract(ctx)
                        + " (총 " + str(getPeriodFromContract(ctx)) + " 일)")
                embed.add_field(name="계약기간", value=text, inline=False)
            embed.add_field(name="히스토리", value=history, inline=False)

            embed2_msg = await ctx.send(embed=embed)

        else:
            await ctx.reply(config.notJoinText)

    @commands.command(name='히스토리', pass_context=True)
    async def _history(self, ctx):
        if checkUseJoinCommand(ctx):
            i = 0
            text_li = []
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM SEASON_USER_HISTORY WHERE ID=?", (ctx.author.id,))
            data_list = cur.fetchall()
            data_list.sort(key=lambda x : x[1])  # Season 순으로 정렬
            print(data_list)
            print(len(data_list))
            while i < len(data_list):
                i = i + 1
                print(i, data_list[i])
                season = data_list[i][1]
                team = data_list[i][2]
                job = data_list[i][3]
                position = data_list[i][4]
                rank = data_list[i][5]
                host = getHostFromSeasonTeamCount(season)
                totalcount = getHostFromSeasonTeamCount(season)
                print(season, type(season))
                print(team, type(team))
                print(job, type(type))
                print(position, type(position))
                print(rank, type(rank))
                print(host, type(host))
                print(totalcount, type(totalcount))
                print("====")
            '''for i in range(len(data_list)+1):
                print(i, data_list[i])
                season = data_list[i][1]
                team = data_list[i][2]
                job = data_list[i][3]
                position = data_list[i][4]
                rank = data_list[i][5]
                host = getHostFromSeasonTeamCount(season)
                totalcount = getHostFromSeasonTeamCount(season)
                print(season, type(season))
                print(team, type(team))
                print(job, type(type))
                print(position, type(position))
                print(rank, type(rank))
                print(host, type(host))
                print(totalcount, type(totalcount))
                print("====")'''
            '''i = 0
            for data in data_list:
                season = data[1]
                team = data[2]
                job = data[3]
                position = data[4]
                rank = data[5]
                host = getHostFromSeasonTeamCount(season)
                totalcount = getHostFromSeasonTeamCount(season)
                i = i + 1
                print(i, "========================================")
                print(season, type(season))
                print(team, type(team))
                print(job, type(type))
                print(position, type(position))
                print(rank, type(rank))
                print(host, type(host))
                print(totalcount, type(totalcount))
                print("====")
                text = ''
                print(data)
                text = text + getHostFromSeasonTeamCount(data[1]) + " " + data[1] + " 시즌 " + data[2] + " " + data[
                    3] + " " \
                       + data[4] + " " + str(data[5]) + "위 (" + str(getTotalCountFromSeasonTeamCount(data[1])) + "팀)\n"
                print(text)'''
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
