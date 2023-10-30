import discord
from discord.ext import commands
import myfun
from discord.utils import get
from forAccessDB import *
import random
from datetime import datetime, timedelta
import config

class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='전체팀목록', pass_context=True, aliases=['팀목록', '전체팀명단'],
                      help="권한 : 전체"
                           "\nCEF에 소속된 팀들의 총원과 지난 시즌 성적 등 정보를 출력합니다.",
                      brief="$전체팀목록")
    async def _wholeTeamList(self, ctx) :
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION")
        result = cur.fetchall()
        result.sort(key=lambda x:x[3])
        embed = discord.Embed(title="CEF 전체 팀 간략 정보")
        for row in result :
            print(row)
            abbName = row[0]
            print(abbName)
            fullName = row[1]
            print(fullName)
            print(row[3])
            if row[3] == -1 :
                lastRank = ""
            elif row[3] == 99 :
                lastRank = "New"
            elif row[3] == 100 :
                lastRank = "-"
            else :
                # lastRank = "지난 시즌 : " + str(row[3]) + " 위"
                lastRank = str(row[3]) + " 위"
            print(lastRank)
            if abbName == "FA" :
                abb2 = "FA (무소속)"
                embed.add_field(name=f"{fullName}", value=f" - 현재 인원 : {str(myfun.getRoleCount(ctx, abb2))} 명",
                                inline=False)
            else :
                imoji = getImojiFromTeamInfor(abbName)
                if imoji == "":
                    embed.add_field(name=f"{fullName}",
                                    value=f" - 팀 약자 : {abbName}\n"
                                          f"- 현재 인원 : {str(myfun.getRoleCount(ctx, abbName))} 명\n"
                                          f"- 지난 순위 : {lastRank}",
                                    inline=True)
                else:
                    embed.add_field(name=f"{imoji} {fullName}",
                                    value=f" - 팀 약자 : {abbName}\n"
                                          f"- 현재 인원 : {str(myfun.getRoleCount(ctx, abbName))} 명\n"
                                          f"- 지난 순위 : {lastRank}",
                                    inline=True)
        await ctx.send(embed=embed)

    @commands.command(name="팀명단", pass_context=True,
                      help="권한 : 전체"
                           "\n특정 팀의 명단을 포지션별로 구분하여 출력합니다.",
                      brief="$팀명단 '팀약자'")
    async def _teamList(self, ctx, name) :
        if name != "" :
            posList = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]
            teamList = []
            getRole = get(ctx.guild.roles, name=name)
            name = name.upper()
            embed = discord.Embed(title=f"팀 {name} 정보", description=f"총원 : {myfun.getRoleCount(ctx, name)} 명")
            for member in getRole.members :
                nickname = getNicknameFromUserInfoWithID(member.id)
                mainPosition = getMainPositionFromUserInfoWithID(member.id)
                teamList.append((mainPosition, nickname))
            for pos in posList :
                text = ''
                for mem in teamList :
                    if pos == mem[0] :
                        text = text + mem[1] + "\n"
                embed.add_field(name=f"{pos}", value=f"{text}")

            await ctx.send(embed=embed)

        else :
            ctx.reply("팀약자와 함께 명령어를 사용해주세요.\n"
                      "사용방법 : $팀명단 '팀약자'\n"
                      "예시) $팀명단 FCB")

async def setup(bot):
    await bot.add_cog(Team(bot))