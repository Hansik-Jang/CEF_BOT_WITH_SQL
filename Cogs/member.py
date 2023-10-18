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


class Member(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx) :
        ownRoles = [role.name for role in ctx.author.roles]
        joinChannel = get(ctx.guild.channels, id=706501803788730429)
        # DB 입력 값 -----------------
        myID = ctx.author.id
        nickname = ''
        mainPosition = ''
        subPosition = ''
        teamNumber = 0
        rank = "선수"
        nicknameChangeCoupon = 1
        # ----------------------------
        joinSwitch = False  # Switch가 True면 가입 명령어 가능 상태
        NICKNAME_FORMAT_CHECK_SWITCH = False  # 닉네임 양식 '[, ]' 포함 여부 - True : 다음 단계 진행
        NICKNAME_OVERLAP_CHECK_SWITCH = False
        MAIN_POSITION_CHECK_SWITCH = False
        SUB_POSITION_CHECK_SWITCH = False
        RE_JOIN_CHECK_SWITCH = False
        name = ctx.author.name
        channel = get(ctx.guild.channels, id=ctx.channel.id)
        thread = await channel.create_thread(
            name=name,
            type=discord.ChannelType.private_thread
        )
        msg10 = await ctx.send(content=f"{ctx.author.mention}\n"
                                       f"{thread.mention}을 확인하여 가입을 진행주세요.")
        await thread.send(content=f"{ctx.author.mention}")

        # ===============================================================================================================

        # ===== 역할 제거 단계 ==================================================================================================
        if config.baseRoleName in config.totalCommunityRoleNameList :  # CEF, RFA, KPA, EVT, SNI 역할이 있으면
            if config.baseRoleName in ownRoles :  # CEF 역할을 갖고 있으면
                await ctx.reply(content=f"이미 가입되었습니다.", delete_after=10)
                await thread.send(content=f"해당 스레드는 30초 후 자동 삭제됩니다.")
                joinSwitch = False  # 스위치 False로 변경
                await asyncio.sleep(30)
                await thread.delete()
            else :  # CEF 역할을 안 갖고 있으면(타 커뮤니티 유저) 모든 역할 회수 후 스위치 True

                announcement = await thread.send("```EAFC 프로클럽 커뮤니티 CEF에 오신 것을 환영합니다.\n"
                                                 "봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                 "1. 역할 소유 검사\n"
                                                 "2. 영문 닉네임 검사\n"
                                                 "3. 닉네임 양식 검사\n"
                                                 "4. 닉네임 중복 검사\n"
                                                 "5. 포지션 정보 입력\n"
                                                 "6. 신규/재가입 검사```")
                department = ""
                user = ctx.author
                for role in ownRoles :
                    if role == "EVT" :
                        department = "EVT"
                    elif role == 'RFA' :
                        department = "RFA"
                    elif role == "KPA" :
                        department = "KPA"
                    elif role == "SNI" :
                        department = "SNI"
                removeRole = get(ctx.guild.roles, name=department)
                if department != '' :  # 타 커뮤니티 역할이 있으면
                    await user.remove_roles(removeRole)
                    await thread.send(content=f"```기존 역할 '{department}'를 회수하였습니다.```")
                    joinSwitch = True
                else :
                    an_msg1 = await thread.send(content=f"소속된 '커뮤니티' 혹은 '팀'이 없습니다.")
                    joinSwitch = True
                await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                                f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                f"1. 역할 소유 검사 - {department}\n"
                                                f"2. 영문 닉네임 검사\n"
                                                "3. 닉네임 양식 검사\n"
                                                "4. 닉네임 중복 검사\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
        # ===== 닉네임 단계 시작 ==================================================================================================
        if joinSwitch :  # Switch가 True이면 가입 진행
            # ========= 한글, 영어 검사 ==============================================================================================
            if checkFun.checkEnglish(ctx) :
                nickname = myfun.getNickFromDisplayname(ctx)
                await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                                f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                f"1. 역할 소유 검사 - {department} (○)\n"
                                                f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                                "3. 닉네임 양식 검사\n"
                                                "4. 닉네임 중복 검사\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
                # ============= 닉네임 양식 검사 =========================================================================================
                if checkFun.checkNicknameForm(ctx) :  # 닉네임 양식 검사 (별명 안에 '[', ']'가 있으면
                    NICKNAME_FORMAT_CHECK_SWITCH = True
                else :  # 닉네임 양식 검사 (별명 안에 '[', ']'가 없으면
                    msg1 = await thread.send(content=f"CEF 서버는 디스코드 내 별명을 기준으로 활동하게 됩니다.\n"
                                                     f"디스코드 닉네임은 **'{ctx.author.name}'**, "
                                                     f"서버 내 별명은 **'{myfun.getNickFromDisplayname(ctx)}'**으로 ")
                    if checkFun.checkDisplayNameChange(ctx) :
                        # 디스코드 닉네임과 서버 별명이 다를 경우
                        try :
                            msg2 = await thread.send(
                                content=f"현재 서버 내 별명인 **'{myfun.getNickFromDisplayname(ctx)}'**으로 가입을 진행하시겠습니까?\n"
                                        f"10초 이내에 원하는 번호를 입력해주세요.\n"
                                        f"1. 현재 닉네임으로 다음 단계\n"
                                        f"2. 닉네임 수정 후 다시 진행")
                            msg = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == thread,
                                                          timeout=10.0)
                        except asyncio.TimeoutError :
                            await msg10.delete()
                            await thread.send(content=f"시간이 초과되었습니다.\n"
                                                      f"{joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                                      f"해당 스레드는 30초 후 자동 삭제됩니다.")
                            await asyncio.sleep(30)
                            await thread.delete()
                        else :
                            if msg.content.lower() == '1' :  # 현재 닉네임으로 진행
                                NICKNAME_FORMAT_CHECK_SWITCH = True
                                nickname = myfun.getNickFromDisplayname(ctx)
                            elif msg.content.lower() == '2' :  # 닉네임 변경 후 재시도
                                NICKNAME_FORMAT_CHECK_SWITCH = False
                                await msg10.delete()
                                await thread.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후"
                                                          f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                                await asyncio.sleep(30)
                                await thread.delete()
                        finally :
                            await msg1.delete()
                            await msg2.delete()
                    else :
                        # 디스코드 닉네임과 서버 별명이 같을 경우
                        try :
                            msg2 = await thread.send(content=f"서버 내 별명을 변경하지 않은 것으로 확인됩니다.\n"
                                                             f"현재 닉네임으로 가입을 진행하시겠습니까? 10초 이내에 원하는 번호를 입력해주세요.\n"
                                                             f"1. 현재 닉네임으로 다음 단계\n"
                                                             f"2. 닉네임 수정 후 다시 진행")
                            msg = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == thread,
                                                          timeout=10.0)
                        except asyncio.TimeoutError :
                            await thread.send("시간이 초과되었습니다. 다시 %가입 명령어를 입력해주세요.", delete_after=10)
                        else :
                            if msg.content.lower() == '1' :  # 현재 닉네임으로 진행
                                NICKNAME_FORMAT_CHECK_SWITCH = True
                                nickname = myfun.getNickFromDisplayname(ctx)
                            elif msg.content.lower() == '2' :  # 닉네임 변경 후 시도
                                NICKNAME_FORMAT_CHECK_SWITCH = False
                                await msg10.delete()
                                await thread.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후"
                                                          f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                                await asyncio.sleep(30)
                                await thread.delete()
                        finally :
                            await msg1.delete()
                            await msg2.delete()
            else :
                await msg10.delete()
                await thread.send("닉네임은 영문만 사용이 가능합니다.\n"
                                  f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                  f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await asyncio.sleep(30)
                await thread.delete()
        if NICKNAME_FORMAT_CHECK_SWITCH :
            await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                            f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                            f"1. 역할 소유 검사 - {department} (○)\n"
                                            f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                            "3. 닉네임 양식 검사 - (○)\n"
                                            "4. 닉네임 중복 검사\n"
                                            "5. 포지션 정보 입력\n"
                                            "6. 신규/재가입 검사```")
            await thread.send("영문 닉네임 확인, 닉네임 확인 완료", delete_after=10)
            # 닉네임 중복 검사 =============================================================================================
            if checkFun.checkNicknameOverlap(ctx):  # 닉네임 중복 검사
                # 포지션 선택 =============================================================================================
                await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                                f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                f"1. 역할 소유 검사 - {department} (○)\n"
                                                f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                                "3. 닉네임 양식 검사 - (○)\n"
                                                "4. 닉네임 중복 검사 - 중복 없음 (○)\n"
                                                "5. 포지션 정보 입력\n"
                                                "6. 신규/재가입 검사```")
                embed = discord.Embed(title="메인 포지션을 선택합니다.", description="본인이 희망하는 '메인' 포지션의 번호를 30 초내에 입력해주세요.")
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
                embed_msg = await thread.send(embed=embed)
                try :
                    msg = await self.bot.wait_for("message",
                                                  check=lambda
                                                      m : m.author == ctx.author and m.channel == thread,
                                                  timeout=30.0)
                except asyncio.TimeoutError :
                    await msg10.delete()
                    await thread.send("시간이 초과되었습니다.\n"
                                      f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                      f"해당 스레드는 30초 후 자동 삭제됩니다.")
                    await asyncio.sleep(30)
                    await thread.delete()
                else :
                    if msg.content.lower() == '1' :
                        mainPosition = "LW"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '2' :
                        mainPosition = "ST"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '3' :
                        mainPosition = "RW"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '4' :
                        mainPosition = "CAM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '5' :
                        mainPosition = "CM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '6' :
                        mainPosition = "CDM"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '7' :
                        mainPosition = "LB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '8' :
                        mainPosition = "CB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '9' :
                        mainPosition = "RB"
                        MAIN_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '10' :
                        mainPosition = "GK"
                        MAIN_POSITION_CHECK_SWITCH = True
                    else :
                        await msg10.delete()
                        await thread.send("잘못 입력하였습니다..\n"
                                          f"{joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                        await asyncio.sleep(30)
                        await thread.delete()

                await embed_msg.delete()
                if MAIN_POSITION_CHECK_SWITCH :
                    embed = discord.Embed(title="서브 포지션을 선택합니다.", description="본인이 희망하는 '서브' 포지션의 번호를 30 초내에 입력해주세요.")
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
                    embed2_msg = await thread.send(embed=embed)
                    try :
                        msg = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == thread,
                                                      timeout=30.0)
                    except asyncio.TimeoutError :
                        await msg10.delete()
                        await thread.send("시간이 초과되었습니다.\n"
                                          f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                        await asyncio.sleep(30)
                        await thread.delete()

                    else :
                        if msg.content.lower() == '1' :
                            subPosition = "LW"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '2' :
                            subPosition = "ST"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '3' :
                            subPosition = "RW"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '4' :
                            subPosition = "CAM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '5' :
                            subPosition = "CM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '6' :
                            subPosition = "CDM"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '7' :
                            subPosition = "LB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '8' :
                            subPosition = "CB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '9' :
                            subPosition = "RB"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '10' :
                            subPosition = "GK"
                            SUB_POSITION_CHECK_SWITCH = True
                        elif msg.content.lower() == '0' :
                            subPosition = ""
                            SUB_POSITION_CHECK_SWITCH = True
                        else :
                            await thread.send("잘못 입력하였습니다..\n"
                                              f"{joinChannel.mention}에 다시 가입 명령어를 입력해주세요\n"
                                              f"해당 스레드는 30초 후 자동 삭제됩니다.")
                            await msg10.delete()
                            await asyncio.sleep(30)
                            await thread.delete()

                await embed2_msg.delete()

                # ==== 주포, 부포 같을 시 부포 삭제
                if mainPosition == subPosition :
                    subPosition = ''

                if MAIN_POSITION_CHECK_SWITCH and SUB_POSITION_CHECK_SWITCH :
                    if subPosition != "" :
                        edit_nickname = nickname + "[" + mainPosition + "/" + subPosition + "]"
                    else :
                        edit_nickname = nickname + "[" + mainPosition + "]"
                    RE_JOIN_CHECK_SWITCH = True
            else:
                await msg10.delete()
                await thread.send(content=f"{ctx.author.mention}, 현재 '{nickname}'와(과) 동일한 닉네임 혹은 유사한 닉네임이 사용 중입니다..\n"
                                          f"닉네임 수정 후 {joinChannel.mention}에 다시 가입 명령어를 입력해주세요.\n"
                                          f"닉네임 중복 문제의 경우 '스태프'에게 문의해주세요.\n"
                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await asyncio.sleep(30)
                await thread.delete()

        if RE_JOIN_CHECK_SWITCH :
            await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                            f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                            f"1. 역할 소유 검사 - {department} (○)\n"
                                            f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                            f"3. 닉네임 양식 검사 - (○)\n"
                                            f"4. 닉네임 중복 검사 - 중복 없음 (○)\n"
                                            f"5. 포지션 정보 입력 - {mainPosition}/{subPosition} (○)\n"
                                            f"6. 신규/재가입 검사```")
            # ========= 닉네임 양식 검사 =============================================================================================
            if checkFun.checkRejoin(ctx) :  # 재가입 체크, 참이면 중복 없음 -> 신규 가입
                rejoin_text = "신규 가입"
                await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                                f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                f"1. 역할 소유 검사 - {department} (○)\n"
                                                f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                                f"3. 닉네임 양식 검사 - (○)\n"
                                                f"4. 닉네임 중복 검사 - 중복 없음 (○)\n"
                                                f"5. 포지션 정보 입력 - {mainPosition}/{subPosition} (○)\n"
                                                f"6. 신규/재가입 검사 - {rejoin_text} (○)```")
                # DB 추가
                try :
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO USER_INFORMATION VALUES(?, ?, ?, ?, ?, ?, ?);",
                                (myID, nickname, mainPosition, subPosition, teamNumber, rank, nicknameChangeCoupon))
                    conn.commit()
                finally :
                    conn.close()
                # CEF, 신규 역할 부여
                if subPosition == '':
                    postion_text = mainPosition
                else:
                    postion_text = mainPosition + "/" + subPosition

                user = ctx.author
                CEF_ROLE = get(ctx.guild.roles, name="테스트용")
                # NEW_ROLE = get(ctx.guild.roles, name="신규")
                await user.add_roles(CEF_ROLE)
                # await user.add_roles(NEW_ROLE)
                await thread.send(content=f"가입 절차가 완료되었습니다.\n"
                                       f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await msg10.delete()
                await ctx.reply(content=f"{ctx.author.mention}, 모든 가입 절차가 완료되었습니다.\n"
                                        f"닉네임 : {nickname}\n"
                                        f"포지션 : {postion_text}\n"
                                        f"신규 가입을 환영합니다.")
                await user.edit(nick=edit_nickname)
                await asyncio.sleep(30)
                await thread.delete()
            # 재가입
            else :
                rejoin_text = "재가입"
                await announcement.edit(content=f"```EAFC 프로클럽 커뮤니티, CEF에 오신 것을 환영합니다.\n"
                                                f"봇을 통해 아래와 같은 가입 과정을 진행하게 됩니다.\n"
                                                f"1. 역할 소유 검사 - {department} (○)\n"
                                                f"2. 영문 닉네임 검사 - {nickname} (○)\n"
                                                f"3. 닉네임 양식 검사 - (○)\n"
                                                f"4. 닉네임 중복 검사 - 중복 없음 (○)\n"
                                                f"5. 포지션 정보 입력 - {mainPosition}/{subPosition} (○)\n"
                                                f"6. 신규/재가입 검사 - {rejoin_text} (○)```")
                # DB 업데이트
                try :
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("UPDATE USER_INFORMATION SET Nickname=?, MainPosition=?, SubPosition=?,"
                                "TeamNumber=?, Rank=? WHERE id=?",
                                (nickname, mainPosition, subPosition, teamNumber, rank, myID))
                    conn.commit()
                finally :
                    conn.close()
                # CEF 역할 부여
                if subPosition == '':
                    position_text = mainPosition
                else:
                    position_text = mainPosition + "/" + subPosition
                user = ctx.author
                CEF_ROLE = get(ctx.guild.roles, name="테스트용")
                await user.add_roles(CEF_ROLE)
                await thread.send(content=f"가입 절차가 완료되었습니다.\n"
                                       f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await msg10.delete()
                await ctx.reply(content=f"{ctx.author.mention}, 모든 가입 절차가 완료되었습니다.\n"
                                        f"닉네임 : {nickname}\n"
                                        f"포지션 : {position_text}\n"
                                        f"재가입을 환영합니다.")
                await user.edit(nick=edit_nickname)
                await asyncio.sleep(30)
                await thread.delete()
                user = ctx.author


    @commands.command(name='닉네임변경', pass_context=True, aliases=['닉변'])
    async def _changeNick(self, ctx, *, insert_nickname=None):
        result = forAccessDB.getUserInformation(ctx)
        ex_nickname = myfun.getNickFromDisplayname(ctx)
        # 등록 여부 검사
        if result is not None :
            # 변경할 닉네임 입력 했는지 검사
            if insert_nickname is not None :
                # 닉네임 중복 검사
                if checkFun.checkNicknameOverlapText(insert_nickname):

                    # 닉변권 개수 검사
                    if result[6] > 0:   # 1개 이상일 경우에만 가능
                        # 입력 데이터 정리
                        myID = ctx.author.id
                        nickname = insert_nickname
                        reduceCount = result[6] - 1
                        # DB 업데이트
                        try :
                            conn = sqlite3.connect("CEF.db")
                            cur = conn.cursor()
                            cur.execute("UPDATE USER_INFORMATION SET Nickname=?, NickChangeCoupon=? WHERE id=?", (nickname, reduceCount, myID))
                            conn.commit()
                        finally :
                            conn.close()

                        # 디스코드 닉네임 수정
                        result = forAccessDB.getUserInformation(ctx)
                        nickname = result[1]
                        mainPos = result[2]
                        subPos = result[3]
                        imoji = getImoji(ctx)
                        edit_nickname = myfun.recombinationNickname(nickname, mainPos, subPos, imoji)
                        user = ctx.author
                        await user.edit(nick=edit_nickname)
                        await ctx.reply(content=f"닉네임 변경이 완료되었습니다.\n"
                                                f"{ex_nickname} -> {edit_nickname}\n"
                                                f"남은 닉변권 개수 : {reduceCount}")


                    else:               # 닉변권이 0개일 경우
                        await ctx.reply(content=f"닉변권 개수가 {result[6]} 입니다.")
                else:
                    await ctx.reply(content=f"{ctx.author.mention}, 현재 '{insert_nickname}'와(과) 동일한 닉네임 혹은 유사한 닉네임이 사용 중입니다..\n"
                                            f"닉네임 수정 후 다시 명령어를 입력해주세요.\n"
                                            f"닉네임 중복 문제의 경우 '스태프'에게 문의해주세요.\n"
                                            f"해당 스레드는 30초 후 자동 삭제됩니다.")
            else:
                await ctx.reply(f"변경할 닉네임을 입력 후에 다시 명령어를 사용해주세요.\n"
                                f"사용 예시 : %닉네임변경 Messi / $닉변 Messi")
        else:
            await ctx.reply(config.notJoinText)

    @commands.command(name='포지션변경', pas_context=True, aliases=['포변'])
    async def _changePos(self, ctx):
        if checkUseJoinCommand(ctx):
            name = myfun.getNickFromDisplayname(ctx)
            channel = get(ctx.guild.channels, id=ctx.channel.id)
            thread = await channel.create_thread(
                name=name,
                type=discord.ChannelType.private_thread
            )
            msg10 = await ctx.send(content=f"{ctx.author.mention}\n"
                                           f"{thread.mention}을 확인하여 가입을 진행주세요.")

            embed = discord.Embed(title="메인 포지션을 선택합니다.", description="본인이 희망하는 '메인' 포지션의 번호를 30 초내에 입력해주세요.")
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
            embed_msg = await thread.send(embed=embed)
            try :
                msg = await self.bot.wait_for("message",
                                              check=lambda
                                                  m : m.author == ctx.author and m.channel == thread,
                                              timeout=30.0)
            except asyncio.TimeoutError :
                await msg10.delete()
                await thread.send("시간이 초과되었습니다.\n"
                                  f"다시 명령어를 입력해주세요\n"
                                  f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await asyncio.sleep(30)
                await thread.delete()
            else :
                if msg.content.lower() == '1' :
                    mainPosition = "LW"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '2' :
                    mainPosition = "ST"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '3' :
                    mainPosition = "RW"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '4' :
                    mainPosition = "CAM"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '5' :
                    mainPosition = "CM"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '6' :
                    mainPosition = "CDM"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '7' :
                    mainPosition = "LB"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '8' :
                    mainPosition = "CB"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '9' :
                    mainPosition = "RB"
                    MAIN_POSITION_CHECK_SWITCH = True
                elif msg.content.lower() == '10' :
                    mainPosition = "GK"
                    MAIN_POSITION_CHECK_SWITCH = True
                else :
                    await msg10.delete()
                    await thread.send("잘못 입력하였습니다..\n"
                                      f"다시 명령어를 입력해주세요\n"
                                      f"해당 스레드는 30초 후 자동 삭제됩니다.")
                    await asyncio.sleep(30)
                    await thread.delete()

            await embed_msg.delete()
            if MAIN_POSITION_CHECK_SWITCH :
                embed = discord.Embed(title="서브 포지션을 선택합니다.", description="본인이 희망하는 '서브' 포지션의 번호를 30 초내에 입력해주세요.")
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
                embed2_msg = await thread.send(embed=embed)
                try :
                    msg = await self.bot.wait_for("message",
                                                  check=lambda
                                                      m : m.author == ctx.author and m.channel == thread,
                                                  timeout=30.0)
                except asyncio.TimeoutError :
                    await msg10.delete()
                    await thread.send("시간이 초과되었습니다.\n"
                                      f"다시 명령어를 입력해주세요\n"
                                      f"해당 스레드는 30초 후 자동 삭제됩니다.")
                    await asyncio.sleep(30)
                    await thread.delete()

                else :
                    if msg.content.lower() == '1' :
                        subPosition = "LW"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '2' :
                        subPosition = "ST"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '3' :
                        subPosition = "RW"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '4' :
                        subPosition = "CAM"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '5' :
                        subPosition = "CM"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '6' :
                        subPosition = "CDM"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '7' :
                        subPosition = "LB"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '8' :
                        subPosition = "CB"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '9' :
                        subPosition = "RB"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '10' :
                        subPosition = "GK"
                        SUB_POSITION_CHECK_SWITCH = True
                    elif msg.content.lower() == '0' :
                        subPosition = ""
                        SUB_POSITION_CHECK_SWITCH = True
                    else :
                        await thread.send("잘못 입력하였습니다..\n"
                                          f"다시 명령어를 입력해주세요\n"
                                          f"해당 스레드는 30초 후 자동 삭제됩니다.")
                await msg10.delete()
                await asyncio.sleep(30)
                await thread.delete()

                await embed2_msg.delete()

            # ==== 주포, 부포 같을 시 부포 삭제
            if mainPosition == subPosition :
                subPosition = ''

            # DB 업데이트
            nickname = myfun.getNickFromDisplayname(ctx)
            imoji = myfun.getimoji(ctx)
            edit_nickname = myfun.recombinationNickname(nickname, mainPosition, subPosition, imoji)
            ex_mainPos = forAccessDB.getMainPositionFromUserInfo(ctx)
            ex_subPos = forAccessDB.getSubPositionFromUserInfo(ctx)
            try:
                conn = sqlite3.connect("CEF.db")
                cur = conn.cursor()
                cur.execute("UPDATE USER_INFORMATION SET  MainPosition=?, SubPosition=?, WHERE id=?",
                            (mainPosition, subPosition, ctx.author.id))
                print("DB 업데이트 완료")
            finally:
                conn.close()
            user = ctx.author
            await user.edit(nick=edit_nickname)
            await ctx.reply(f"정보가 업데이트되었습니다.\n"
                            f"주포지션 : {ex_mainPos} -> {mainPosition}\n"
                            f"부포지션 : {ex_subPos} -> {subPosition}")

        else:
            await ctx.reply(config.notJoinText)


async def setup(bot) :
    await bot.add_cog(Member(bot))
