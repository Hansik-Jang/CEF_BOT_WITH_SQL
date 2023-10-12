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

global DEVELOPER_SWITCH


class Member(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx) :
        ownRoles = [role.name for role in ctx.author.roles]
        # DB 입력 값 -----------------
        myID = ctx.author.id
        nickname = ''
        mainPostion = ''
        subPostion = ''
        teamNumber = 0
        rank = "선수"
        nicknameChangeCoupon = 1
        # ----------------------------
        joinSwitch = False  # Switch가 True면 가입 명령어 가능 상태
        NICKNAME_FORMAT_CHECK_SWITCH = False    # 닉네임 양식 '[, ]' 포함 여부 - True : 다음 단계 진행
        NICKNAME_OVERLAP_CHECK_SWITCH = False
        MAIN_POSITION_CHECK_SWITCH = False
        SUB_POSITION_CHECK_SWITCH = False
        RE_JOIN_CHECK_SWITCH = False
        announcement = await ctx.send("```EAFC 프로클럽 커뮤니티 CEF**에 오신 것을 환영합니다.\n"
                                      "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                      "1. 역할 소유 검사\n"
                                      "2. 영문 닉네임 검사\n"
                                      "3. 닉네임 양식 검사\n"
                                      "4. 닉네임 중복 검사\n"
                                      "5. 포지션 정보 입력\n"
                                      "6. 신규/재가입 검사```")
# ===== 역할 제거 단계 ==================================================================================================
        if config.baseRoleName in config.totalCommunityRoleNameList:  # CEF, RFA, KPA, EVT, SNI 역할이 있으면
            if config.baseRoleName in ownRoles :  # CEF 역할을 갖고 있으면
                await ctx.reply(content=f"이미 가입되었습니다.", delete_after=5)
                await announcement.delete()
                joinSwitch = False  # 스위치 False로 변경
            else:  # CEF 역할을 안 갖고 있으면(타 커뮤니티 유저) 모든 역할 회수 후 스위치 True
                department = ""
                user = ctx.author
                for role in ownRoles:
                    if role == "EVT":
                        department = "EVT"
                    elif role == 'RFA':
                        department = "RFA"
                    elif role == "KPA":
                        department = "KPA"
                    elif role == "SNI":
                        department = "SNI"
                removeRole = get(ctx.guild.roles, name=department)
                if department != '':    # 타 커뮤니티 역할이 있으면
                    await user.remove_roles(removeRole)
                    await ctx.send(content=f"```기존 역할 '{department}'를 회수하였습니다.```")
                    joinSwitch = True
                else:
                    await ctx.send(content=f"소속된 '커뮤니티' 혹은 '팀'이 없습니다.")
                    joinSwitch = True
                await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                                "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                "1. 역할 소유 검사 - ○\n"
                                                "2. 영문 닉네임 검사\n"
                                                "3. 닉네임 양식 검사\n"
                                                "4. 닉네임 중복 검사\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
# ===== 닉네임 단계 시작 ==================================================================================================
        if joinSwitch :  # Switch가 True이면 가입 진행
# ========= 한글, 영어 검사 ==============================================================================================
            if checkFun.checkEnglish(ctx):
                await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                                "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                "1. 역할 소유 검사 - ○\n"
                                                "2. 영문 닉네임 검사 - ○\n"
                                                "3. 닉네임 양식 검사\n"
                                                "4. 닉네임 중복 검사\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
# ============= 닉네임 양식 검사 =========================================================================================
                if checkFun.checkNicknameForm(ctx):  # 닉네임 양식 검사 (별명 안에 '[', ']'가 있으면
                    NICKNAME_FORMAT_CHECK_SWITCH = True
                    nickname = myfun.getNickFromDisplayname(ctx)
                else:   # 닉네임 양식 검사 (별명 안에 '[', ']'가 없으면
                    msg1 = await ctx.send(content=f"CEF 서버는 디스코드 내 별명을 기준으로 활동하게 됩니다.\n"
                                                  f"디스코드 닉네임은 **'{ctx.author.name}'**, "
                                                  f"서버 내 별명은 **'{myfun.getNickFromDisplayname(ctx)}'**으로 ")
                    if checkFun.checkDisplayNameChange(ctx):
                        # 디스코드 닉네임과 서버 별명이 다를 경우
                        try:
                            msg2 = await ctx.send(content=f"현재 서버 내 별명인 **'{myfun.getNickFromDisplayname(ctx)}'**으로 가입을 진행하시겠습니까?\n"
                                                          f"10초 이내에 원하는 번호를 입력해주세요.\n"
                                                          f"1. 현재 닉네임으로 다음 단계\n"
                                                          f"2. 닉네임 수정 후 다시 진행")
                            msg = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == ctx.channel,
                                                          timeout=10.0)
                        except asyncio.TimeoutError:
                            await ctx.channel.send("시간이 초과되었습니다. 다시 %가입 명령어를 입력해주세요.", delete_after=10)
                        else :
                            if msg.content.lower() == '1':      # 현재 닉네임으로 진행
                                NICKNAME_FORMAT_CHECK_SWITCH = True
                                nickname = myfun.getNickFromDisplayname(ctx)
                            elif msg.content.lower() == '2':    # 닉네임 변경 후 재시도
                                NICKNAME_FORMAT_CHECK_SWITCH = False
                                await ctx.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후 다시 %가입"
                                                       f" 명령어를 입력해주세요.", delete_after=10)
                        finally:
                            await msg.delete()
                            await msg1.delete()
                            await msg2.delete()
                    else:
                        # 디스코드 닉네임과 서버 별명이 같을 경우
                        try:
                            msg2 = await ctx.send(content=f"서버 내 별명을 변경하지 않은 것으로 확인됩니다.\n"
                                                          f"현재 닉네임으로 가입을 진행하시겠습니까? 10초 이내에 원하는 번호를 입력해주세요.\n"
                                                          f"1. 현재 닉네임으로 다음 단계\n"
                                                          f"2. 닉네임 수정 후 다시 진행")
                            msg = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == ctx.channel,
                                                          timeout=10.0)
                        except asyncio.TimeoutError:
                            await ctx.channel.send("시간이 초과되었습니다. 다시 %가입 명령어를 입력해주세요.", delete_after=10)
                        else:
                            if msg.content.lower() == '1':      # 현재 닉네임으로 진행
                                NICKNAME_FORMAT_CHECK_SWITCH = True
                                nickname = myfun.getNickFromDisplayname(ctx)
                            elif msg.content.lower() == '2':    # 닉네임 변경 후 시도
                                NICKNAME_FORMAT_CHECK_SWITCH = False
                                await ctx.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후 다시 %가입 "
                                                       f"명령어를 입력해주세요., delete_after=10")
                            await ctx.channel.purge(limit=1)
                        finally:
                            await msg.delete()
                            await msg1.delete()
                            await msg2.delete()
            else:
                await ctx.send("닉네임은 영문만 사용이 가능합니다. 닉네임 수정 후 다시 시도해주세요.", delete_after=10)

        if NICKNAME_FORMAT_CHECK_SWITCH:
            await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                            "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                            "1. 역할 소유 검사 - ○\n"
                                            "2. 영문 닉네임 검사 - ○\n"
                                            "3. 닉네임 양식 검사 - ○\n"
                                            "4. 닉네임 중복 검사\n"
                                            "5. 포지션 정보 입력\n"
                                            "6. 신규/재가입 검사```")
            await ctx.send("영문 닉네임 확인, 닉네임 확인 완료", delete_after=10)
# ========= 닉네임 중복 검사 =============================================================================================
            if checkFun.checkNicknameOverlap(ctx):  # 닉네임 중복 검사
# ============= 포지션 선택 =============================================================================================
                await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                                "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                "1. 역할 소유 검사 - ○\n"
                                                "2. 영문 닉네임 검사 - ○\n"
                                                "3. 닉네임 양식 검사 - ○\n"
                                                "4. 닉네임 중복 검사 - ○\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
                embed = discord.Embed(title="메인 포지션을 선택합니다.", description="본인이 희망하는 '메인' 포지션의 번호를 입력해주세요.")
                embed.add_field(name="**1**", value="LW", inline=True)
                embed.add_field(name="**2**", value="ST", inline=True)
                embed.add_field(name="**3**", value="RW", inline=True)
                embed.add_field(name="**4**", value="CAM", inline=True)
                embed.add_field(name="**5**", value="CM", inline=True)
                embed.add_field(name="**6**", value="CDM", inline=True)
                embed.add_field(name="**7**", value="LB", inline=True)
                embed.add_field(name="**8**", value="CB", inline=True)
                embed.add_field(name="**9**", value="RB", inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="**10**", value="GK", inline=True)
                embed.add_field(name="", value="", inline=True)
                embed_msg = await ctx.send(embed=embed)
                try:
                    msg = await self.bot.wait_for("message",
                                                  check=lambda
                                                      m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=10.0)
                except asyncio.TimeoutError:
                    await ctx.channel.send("시간이 초과되었습니다. 다시 %가입 명령어를 입력해주세요.", delete_after=10)
                else:
                    if msg.content.lower() == '1':
                        mainPostion = "LW"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '2':
                        mainPostion = "ST"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '3':
                        mainPostion = "RW"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '4':
                        mainPostion = "CAM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '5':
                        mainPostion = "CM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '6':
                        mainPostion = "CDM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '7':
                        mainPostion = "LB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '8':
                        mainPostion = "CB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '9':
                        mainPostion = "RB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '10':
                        mainPostion = "GK"
                        MAIN_POSITION_CHECK_SWITCH = True
                    else:
                        await ctx.send("잘못 입력하였습니다. 다시 시도해주세요.", delete_after=10)
                        MAIN_POSITION_CHECK_SWITCH = False

                await embed_msg.delete()
                if MAIN_POSITION_CHECK_SWITCH:
                    embed = discord.Embed(title="부 포지션을 선택합니다.", description="본인이 희망하는 '부' 포지션의 번호를 입력해주세요.")
                    embed.add_field(name="**1**", value="LW", inline=True)
                    embed.add_field(name="**2**", value="ST", inline=True)
                    embed.add_field(name="**3**", value="RW", inline=True)
                    embed.add_field(name="**4**", value="CAM", inline=True)
                    embed.add_field(name="**5**", value="CM", inline=True)
                    embed.add_field(name="**6**", value="CDM", inline=True)
                    embed.add_field(name="**7**", value="LB", inline=True)
                    embed.add_field(name="**8**", value="CB", inline=True)
                    embed.add_field(name="**9**", value="RB", inline=True)
                    embed.add_field(name="", value="", inline=True)
                    embed.add_field(name="**10**", value="GK", inline=True)
                    embed.add_field(name="**0**", value="없음", inline=True)
                    embed2_msg = await ctx.send(embed=embed)
                    try :
                        msg = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=10.0)
                    except asyncio.TimeoutError :
                        await ctx.channel.send("시간이 초과되었습니다. 다시 %가입 명령어를 입력해주세요.", delete_after=10)
                    else :
                        if msg.content.lower() == '1':
                            subPostion = "LW"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '2':
                            subPostion = "ST"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '3':
                            subPostion = "RW"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '4':
                            subPostion = "CAM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '5':
                            subPostion = "CM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '6':
                            subPostion = "CDM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '7':
                            subPostion = "LB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '8':
                            subPostion = "CB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '9':
                            subPostion = "RB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '10':
                            subPostion = "GK"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '0':
                            subPostion = ""
                            SUB_POSITION_CHECK_SWITCH = True
                        else:
                            await ctx.send("잘못 입력하였습니다. 다시 시도해주세요.", delete_after=10)
                            SUB_POSITION_CHECK_SWITCH = False

                await embed2_msg.delete()
                if MAIN_POSITION_CHECK_SWITCH and SUB_POSITION_CHECK_SWITCH:
                    if subPostion != "":
#                        await ctx.send(content=f"```입력된 정보\n"
#                                               f"닉네임 : {nickname}\n"
#                                               f"포지션 : {mainPostion}/{subPostion}```")
                        edit_nickname = nickname + "[" + mainPostion + "/" + subPostion + "]"
                    else:
#                        await ctx.send(content=f"```입력된 정보\n"
#                                               f"닉네임 : {nickname}\n"
#                                               f"포지션 : {mainPostion}```")
                        edit_nickname = nickname + "[" + mainPostion + "]"
                    user = ctx.author
                    await user.edit(nick=edit_nickname)
                    RE_JOIN_CHECK_SWITCH = True
            else:
                await ctx.send(content=f"{ctx.author.mention}, '{nickname}'은 현재 사용 중입니다.", delete_after=10)

        if RE_JOIN_CHECK_SWITCH:
            await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                            "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                            "1. 역할 소유 검사 - ○\n"
                                            "2. 영문 닉네임 검사 - ○\n"
                                            "3. 닉네임 양식 검사 - ○\n"
                                            "4. 닉네임 중복 검사 - ○\n"
                                            "5. 포지션 정보 입력 - ○\n"
                                            "6. 신규/재가입 검사```")
# ========= 닉네임 양식 검사 =============================================================================================
            if checkFun.checkRejoin(ctx):   # 재가입 체크, 참이면 중복 없음 -> 신규 가입
                await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                                "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                "1. 역할 소유 검사 - ○\n"
                                                "2. 영문 닉네임 검사 - ○\n"
                                                "3. 닉네임 양식 검사 - ○\n"
                                                "4. 닉네임 중복 검사 - ○\n"
                                                "5. 포지션 정보 입력 - ○\n"
                                                "6. 신규/재가입 검사 - ○```")
                # DB 추가
                try:
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO USER_INFORMATION VALUES(?, ?, ?, ?, ?, ?, ?);",
                                (myID, nickname, mainPostion, subPostion, teamNumber, rank, nicknameChangeCoupon))
                    conn.commit()
                finally:
                    conn.close()
                # CEF, 신규 역할 부여
                user = ctx.author
                CEF_ROLE = get(ctx.guild.roles, name="테스트용")
                # NEW_ROLE = get(ctx.guild.roles, name="신규")
                await user.add_roles(CEF_ROLE)
                # await user.add_roles(NEW_ROLE)
                await ctx.send(content=f"{ctx.author.mention}, 모든 가입 절차가 완료되었습니다.\n"
                                       f"닉네임 : {nickname}\n"
                                       f"포지션 : {mainPostion}/{subPostion}\n"
                                       f"신규 가입을 환영합니다.")
            # 재가입
            else:
                await announcement.edit(content="```EAFC 프로클럽 커뮤니티, CEF**에 오신 것을 환영합니다.\n"
                                                "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                "1. 역할 소유 검사 - ○\n"
                                                "2. 영문 닉네임 검사 - ○\n"
                                                "3. 닉네임 양식 검사 - ○\n"
                                                "4. 닉네임 중복 검사 - ○\n"
                                                "5. 포지션 정보 입력 - ○\n"
                                                "6. 신규/재가입 검사 - ○```")
                # DB 업데이트
                try:
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("UPDATE USER_INFORMATION SET Nickname=?, MainPosition=?, SubPosition=?,"
                                "TeamNumber=?, Rank=? WHERE id=?", (nickname, mainPostion, subPostion, teamNumber, rank, myID))
                    conn.commit()
                finally:
                    conn.close()
                # CEF 역할 부여
                user = ctx.author
                CEF_ROLE = get(ctx.guild.roles, name="테스트용")
                await user.add_roles(CEF_ROLE)
                await ctx.send(content=f"{ctx.author.mention}, 모든 가입 절차가 완료되었습니다.\n"
                                       f"닉네임 : {nickname}\n"
                                       f"포지션 : {mainPostion}/{subPostion}\n"
                                       f"재가입을 환영합니다.")




    @commands.command(name='탈퇴', pass_context=True, aliases=['Withdrawal', 'withdrawal'])
    async def _withdrawal(self, ctx) :
        pass

    @commands.command(name='포지션변경', pass_context=True, aliases=['chanegePosition'])
    async def _changePos(self, ctx) :
        pass

    @commands.command(name='닉네임변경', pass_context=True, aliases=['changeNickname'])
    async def _changeNick(self, ctx, *, nickname) :
        pass


def setup(bot) :
    bot.add_cog(Member(bot))
