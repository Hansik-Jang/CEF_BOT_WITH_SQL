import discord
from discord.ext import commands
import sqlite3
import myfun
from discord.utils import get
from forAccessDB import *


class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='전체팀목록', pass_context=True, aliases=['팀목록', '전체팀명단'])
    async def _wholeTeamList(self, ctx):
        text = ''
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION")
        result = cur.fetchall()
        result.sort(key=lambda x : x[3])
        i = 0

        embed = discord.Embed(title="CEF 전체 팀 간략 정보", description="")
        print("A")
        for row in result:
            print(row)
            abbName = row[0]
            fullName = row[1]
            if row[3] == -1 :
                lastRank = ""
            elif row[3] == 99:
                lastRank = "New"
            elif row[3] == 100:
                lastRank = "-"
            else :
                #lastRank = "지난 시즌 : " + str(row[3]) + " 위"
                lastRank = str(row[3]) + " 위"

            if abbName == "FA":
                abb2 = "FA (무소속)"
                embed.add_field(name=f"{fullName}", value=f" - 현재 인원 : {str(myfun.getRoleCount(ctx, abb2))} 명",
                                inline=False)
            else :
                embed.add_field(name=f"{fullName}", value=f" - 팀 약자 : {abbName}\n"
                                                          f"- 현재 인원 : {str(myfun.getRoleCount(ctx, abbName))} 명\n"
                                                          f"- 지난 순위 : {lastRank}",
                            inline=True)
        await ctx.send(embed=embed)

    @commands.command(name="팀명단", pass_context=True)
    async def _teamList(self, ctx, name):
        if checkUseJoinCommandWithID(ctx.author.id):
            print(name)
            if name != "":
                posList = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]
                teamList = []
                getRole = get(ctx.guild.roles, name=name)
                print(getRole)
                name = name.upper()
                embed = discord.Embed(title=f"팀 {name} 정보", description=f"총원 : {myfun.getRoleCount(ctx, name)} 명")
                for member in getRole.members:
                    print(member.display_name, member.id)
                    nickname = getNicknameFromUserInfoWithID(member.id)
                    print(nickname)
                    mainPosition = getMainPositionFromUserInfoWithID(member.id)
                    print(mainPosition)
                    teamList.append((mainPosition, nickname))
                print(teamList)
                for pos in posList:
                    text = ''
                    for mem in teamList:
                        print(pos, mem[0], mem[1])
                        if pos == mem[0]:
                            text = text + mem[1] + "\n"
                    embed.add_field(name=f"{pos}", value=f"{text}")

                await ctx.send(embed=embed)

            else:
                ctx.reply("팀약자와 함께 명령어를 사용해주세요.\n"
                          "사용방법 : $팀명단 '팀약자'\n"
                          "예시) $팀명단 FCB")
        else :
            await ctx.reply("해당 인원은 등록되지 않는 인원입니다.")

async def setup(bot):
    await bot.add_cog(Team(bot))