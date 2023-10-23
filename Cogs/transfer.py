import discord
from discord.ext import commands

import config
import myfun
from discord.utils import get
from forAccessDB import *
import random
from datetime import datetime, timedelta
import checkFun

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
    async def _transfer(self, ctx, member:discord.Member, abbTeamName=None, startDate=None, period=None):
        delete_time = 15
        role_names = [role.name for role in ctx.author.roles]
        # 스태프 전용 명령어
        if "스태프" in role_names :
            # 등록 여부 검사
            if checkUseJoinCommandWithID(member.id):
                # 팀 약자 정상 작성 검사
                # FA 전환
                if abbTeamName is not None:
                    # 계약 시작일, 계약 기간 작성 여부 검사
                    if startDate is not None and period is not None :
                        # 계약 시작일 정상 작성 여부 검사
                        if '/' in startDate :
                            if checkUseJoinCommandWithID(member.id):
                                abbTeamName = abbTeamName.upper()
                                memberRoleList = [role.name for role in member.roles]
                                print(memberRoleList)
                                if abbTeamName not in memberRoleList :
                                    print(abbTeamName)
                                    # 디스코드 내 작업 - FA 역할 회수
                                    if "FA (무소속)" in memberRoleList :
                                        print("1")
                                        role = get(ctx.guild.roles, name="FA (무소속)")
                                        print("2")
                                        await member.remove_roles(role)  # O
                                        print("3")
                                        await ctx.reply(f"FA 역할 제거", delete_after=delete_time)
                                        print("4")
                                    # 디스코드 내 작업 - 팀 역할 추가
                                    abbTeamName = abbTeamName.upper()
                                    add_role = get(ctx.guild.roles, name=abbTeamName)
                                    await member.add_roles(add_role)
                                    await ctx.reply(f"역할 추가", delete_after=delete_time)
                                    # 이적센터 채널에 명시
                                    channel = get(ctx.guild.channels, name=config.TRANSFER_CENTER)
                                    await channel.send(f"<{getTeamFullNameFromTeamInfor(abbTeamName)}>\n"
                                                       f"{member.mention} 입단")
                                    # DB - USER_INFORMATION 테이블, TeamName abbTeamName으로 업데이트
                                    try:
                                        conn = sqlite3.connect("CEF.db")
                                        cur = conn.cursor()
                                        cur.execute("UPDATE USER_INFORMATION SET TeamName=? WHERE ID=?",
                                                    (abbTeamName, member.id))
                                    finally:
                                        conn.commit()
                                        conn.close()
                                    # 계약 테이블 업데이트
                                    year_now = str(datetime.today().year) + "/"
                                    print(year_now)
                                    idnum = member.id
                                    if year_now not in startDate :
                                        startDate = year_now + startDate
                                    startDate_time = myfun.convertTextToDatetime(startDate)
                                    period2 = int(period) - 1
                                    endData_time = startDate_time + timedelta(days=period2)
                                    endData = myfun.convertDateTimeToText(endData_time)
                                    # DB - 계약 Table 이미 작성된 인원인지 검사
                                    if checkInsertOverapFromContractWithID(member.id) :
                                        # DB - CONTRACT 테이블, 정보 추가
                                        try :
                                            conn = sqlite3.connect("CEF.db")
                                            cur = conn.cursor()
                                            cur.execute("INSERT INTO CONTRACT VALUES(?, ?, ?, ?);",
                                                        (idnum, startDate, period, endData))
                                            await ctx.reply(
                                                f"{myfun.getNickFromDisplayname2(member.display_name)}, DB에 업데이트 되었습니다.")
                                        finally :
                                            conn.commit()
                                            conn.close()
                                    # 계약 갱신
                                    else:
                                        await ctx.reply("```해당 인원은 이미 계약이 등록되어 있습니다.\n"
                                                        "FA전환 후 사용하거나 재계약 명령어를 사용해주세요.```", delete_after=delete_time)
                                else :
                                    await ctx.reply("```해당 인원은 이미 소속 역할을 갖고 있습니다.```", delete_after=delete_time)
                            else:
                                await ctx.reply("```해당 인원은 등록되지 않는 인원입니다.```", delete_after=delete_time)
                        else :
                            await ctx.reply("```아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                            "$계약입력 @멘션 계약시작일 계약기간\n"
                                            "작성 예시) $계약입력 @타임제이 2023/10/21 30```", delete_after=delete_time)
                    else :
                        await ctx.reply("```아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                        "$계약입력 @멘션 팀명 계약시작일 계약기간\n"
                                        "작성 예시) $이적 @타임제이 FCB 2023/10/21 30```", delete_after=delete_time)
                else:
                    await ctx.reply("```팀 약자를 함께 입력해주세요.\n"
                                    "사용방법 : %이적 @멘션 팀약자```", delete_after=delete_time)
            else:
                await ctx.reply("```해당 인원은 등록되지 않는 인원입니다.```", delete_after=delete_time)
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=delete_time)

    @commands.command(name='FA전환', pass_context=True)
    async def _FA(self, ctx, member:discord.Member):
        delete_time = 15
        role_names = [role.name for role in ctx.author.roles]
        # 스태프 전용 명령어
        if "스태프" in role_names or "감독" in role_names:
            # 등록 여부 검사
            if checkUseJoinCommandWithID(member.id):
                if checkUseJoinCommandWithID(member.id):
                    # DB - USER_INFORMATION 테이블, TeamName FA로 업데이트
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("UPDATE USER_INFORMATION SET TeamName=?, Rank=? WHERE ID=?",
                                    ("FA", "선수", member.id))
                    finally :
                        conn.commit()
                        conn.close()
                    # DB - CONTRACT 테이블, 정보 삭제
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("DELETE FROM CONTRACT WHERE ID=?",
                                    (member.id, ))
                    finally :
                        conn.commit()
                        conn.close()
                    # 디스코드 내 작업 - 역할 회수
                    try:
                        memberRoleList = [role.name for role in member.roles]
                        print(memberRoleList)
                        for teamname in checkFun.reclaimTeamRole() :
                            if teamname in memberRoleList :
                                abbName = teamname
                                role = get(ctx.guild.roles, name=teamname)
                                await member.remove_roles(role)
                                await ctx.send(f"{teamname} 역할 제거", delete_after=delete_time)
                    except:
                        pass
                    # 이적센터 채널에 명시
                    channel = get(ctx.guild.channels, name=config.TRANSFER_CENTER)
                    await channel.send(f"<{getTeamFullNameFromTeamInfor(abbName)}>\n"
                                       f"{member.mention} 계약해지")
                else :
                    await ctx.reply("해당 인원은 등록되지 않는 인원입니다.", delete_after=delete_time)
            else:
                await ctx.reply("```해당 인원은 등록되지 않는 인원입니다.```", delete_after=delete_time)
        else:
            await ctx.reply("```해당 명령어는 스태프 혹은 감독만 사용 가능합니다.```", delete_after=delete_time)
async def setup(bot):
    await bot.add_cog(Transfer(bot))