import discord
from datetime import datetime, timedelta
import sqlite3
import checkFun
import asyncio
from myfun import *
from discord.ext import commands
from discord.utils import get
import string
import config
import myfun
import forAccessDB
from forAccessDB import *
global DEVELOPER_SWITCH

class 개발자전용(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='정보동기화', pass_context=True,
                      aliases=['동기화'],
                      help="권한 : 스태프\n"
                           "CEF 역할을 갖고 있는 모든 유저의 정보를 DB에 동기화 합니다.",
                      brief="포지션변경 or $포변")
    async def _syncUserInfor(self, ctx):
        CEF_ROLE = get(ctx.guild.roles, name="CEF")
        for member in CEF_ROLE.members:
            print(member.display_name)
            try:
                myNickname = getNickFromDisplayname2(member.display_name)
                myJupo = getJupoFromDisplayname2(member.display_name)
                myBupo = getBupoFromDisplayname2(member.display_name)
                if myBupo == "없음":
                    myBupo = ""
                roleNameList = [role.name for role in member.roles]
                myTeamname = ''
                print(roleNameList)
                for TEAM_NAME in config.TEAM_NAME_LIST:
                    temp = TEAM_NAME + " Coach"
                    myRank = "선수"
                    myTeamname = "FA"
                    if temp in roleNameList:
                        myRank = "코치"
                    if "감독" in roleNameList:
                        myRank = "감독"

                    if TEAM_NAME in roleNameList :
                        myTeamname = TEAM_NAME
                        break

                myNickChangeCoupon = 0

                print(member.id, myNickname, myJupo, myBupo, myTeamname, myRank, myNickChangeCoupon)
                if checkUseJoinCommandWithID(member.id):
                    pass
                else:
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO USER_INFORMATION VALUES(?, ?, ?, ?, ?, ?, ?)",
                                (member.id, myNickname, myJupo, myBupo, myTeamname, myRank, myNickChangeCoupon))
                    await ctx.send(f"```{myNickname} 수정 완료\n"
                                   f"주포 : {myJupo}, 부포 : {myBupo}, 소속 : {myTeamname}, 신분 : {myRank}, 닉변권 : {myNickChangeCoupon} 개 ```")
                    conn.commit()
                    conn.close()
            except:
                await ctx.send(f"{ctx.author.mention}\n"
                               f"{member.display_name} 실패")
        await ctx.send("완료")

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"개발자전용 전용 : {error}")
async def setup(bot) :
    await bot.add_cog(개발자전용(bot))