import discord
from discord.ext import commands
from discord.utils import get
import checkFun
from forAccessDB import *
import config
import asyncio
import myfun
from table2ascii import table2ascii as t2a, PresetStyle


class 스태프전용_팀관리(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.command(name='팀등록', pass_context=True,
                      help="권한 : 스태프 전용\n"
                           "팀 명단 체크, 팀 정보(팀약자, 풀네임, 색상코드, 로고 링크) 입력, DB 업데이트 등 팀 등록을 진행합니다.\n",
                      brief="$팀등록 @멘션(다수 가능)")
    async def _registerTeam(self, ctx, *people: discord.Member) :
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            temp = ''
            insertSwitch = False
            exitSwitch = True
            for man in people :
                temp = temp + man.display_name + "\n"

            temp_msg = await ctx.send(f"```팀등록에 앞서 명단 체크를 진행합니다.\n\n"
                                      f"팀에 등록될 명단 : \n"
                                      f"{temp}\n"
                                      f"맞으면 1, 틀리면 2를 입력해주세요.```")
            try :
                temp_msg2 = await self.bot.wait_for("message",
                                                    check=lambda
                                                        m : m.author == ctx.author and m.channel == ctx.channel,
                                                    timeout=30.0)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.\n"
                               f"다시 명령어를 입력해주세요\n"
                               f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
            else :
                if temp_msg2.content == "1" :
                    insertSwitch = True
                    await temp_msg.edit(content=f"다음 단계로 진행합니다.", delete_after=30)
                elif temp_msg2.content == "2" :
                    await temp_msg.edit(content=f"명령어를 종료합니다. 수정 후 다시 입력해주세요.", delete_after=30)

            if insertSwitch :
                abbName = ""
                fullName = ""
                colorCode = ""
                lastRank = 99
                logoLink = ""
                loop_switch = 1
                text = ("1. 팀약자 : \n"
                        "2. 풀네임 : \n"
                        "3. 색상코드 : \n"
                        "4. 로고 링크 : \n\n"
                        "<TIP>\n"
                        "1. 이모지는 명령어 사용 전 미리 등록한 후 로고 입력 후 로고 앞에 '\'를 붙여 다음과 같은 형태를 입력해야 합니다.\n"
                        "<로고이름:로고 ID 번호>\n"
                        "2. 로고 링크는 채팅 채널에 이미지 업로드 후 우클릭하여 링크 복사하기를 하여 '이미지 링크'를 입력해주세요.\n")
                embed = discord.Embed(title="팀등록 절차를 시작합니다.", description=text, color=discord.Color.red())
                embed_msg = await ctx.send(embed=embed)
                while loop_switch < 5 :
                    if abbName == "" :
                        text1 = f"1. 팀약자 : {abbName} (입력 X)\n"
                    else :
                        text1 = f"1. 팀약자 : {abbName} (입력 O)\n"
                    if fullName == "" :
                        text2 = f"2. 풀네임 : {fullName} (입력 X)\n"
                    else :
                        text2 = f"2. 풀네임 : {fullName} (입력 O)\n"
                    if colorCode == "" :
                        text3 = f"3. 색상코드 : {colorCode} (입력 X)\n"
                    else :
                        text3 = f"3. 색상코드 : {colorCode} (입력 O)\n"
                    if logoLink == "" :
                        text5 = f"4. 로고 링크 : {logoLink} (입력 X)\n"
                    else :
                        text5 = f"4. 로고 링크 : {logoLink} (입력 O)\n"
                    text6 = "5. 강제 종료하기\n\n"
                    text_tip = (f"<TIP>\n"
                                f"1. 이모지는 명령어 사용 전 미리 등록한 후 로고 입력 후 로고 앞에 '\'를 붙여 다음과 같은 형태를 입력해야 합니다.\n"
                                f"   <로고이름:로고 ID 번호>\n"
                                f"2. 로고 링크는 채팅 채널에 이미지 업로드 후 우클릭하여 링크 복사하기를 하여 '이미지 링크'를 입력해주세요.\n")
                    text = text1 + text2 + text3 + text5 + text6 + text_tip
                    exitText = text1 + text2 + text3 + text5
                    embed2 = discord.Embed(title="팀등록 절차를 시작합니다.", description=text, color=discord.Color.yellow())
                    await embed_msg.edit(embed=embed2)
                    ann_msg = await ctx.send("안내 문구에 따라 정보를 입력해주세요.")

                    if loop_switch == 1 :
                        temp_msg = await ann_msg.edit(content="안내 문구에 따라 정보를 입력해주세요."
                                                              "\n1번. 팀약자를 입력해주세요.")
                    elif loop_switch == 2 :
                        temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                              "\n2번. 팀이름 전체를 대소문자 구분하여 입력해주세요.")
                    elif loop_switch == 3 :
                        temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                              "\n3번. 팀 색상코드 #을 제외한 6자리를 입력해주세요. ")
                    elif loop_switch == 4 :
                        break
                    try :
                        msg2 = await self.bot.wait_for("message",
                                                       check=lambda
                                                           m : m.author == ctx.author and m.channel == ctx.channel,
                                                       timeout=30.0)
                    except asyncio.TimeoutError :
                        await ctx.send("시간이 초과되었습니다.\n"
                                       f"다시 명령어를 입력해주세요\n"
                                       f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
                        break
                    else :
                        if loop_switch == 1 :
                            await temp_msg.delete()
                            await ctx.channel.purge(limit=1)
                            abbName = msg2.content.upper()
                        elif loop_switch == 2 :
                            await temp_msg.delete()
                            await ctx.channel.purge(limit=1)
                            fullName = msg2.content
                        elif loop_switch == 3 :
                            await temp_msg.delete()
                            await ctx.channel.purge(limit=1)
                            colorCode = msg2.content
                        if msg2.content == "5" :
                            break
                            await ctx.send("강제 종료되었습니다.")
                            exitSwitch = False
                        else :
                            await ctx.send("잘못 입력하였습니다.", delete_after=10)
                    loop_switch += 1

            await ctx.send(f"안내 문구에 따라 정보를 입력해주세요."
                           "\n4번. 팀 로고 이미지 파일(jpg, png 파일)을 업로드해주세요.")
            if exitSwitch :
                def check(message) :
                    if message.author == ctx.author and message.channel == ctx.channel :
                        attachments = message.attachments
                        if len(attachments) == 0 :
                            return False
                        attachment = attachments[0]
                        return attachment.filename.endswith(('.jpg', '.png'))

                try :
                    image_msg = await self.bot.wait_for("message", check=check, timeout=60.0)
                except asyncio.TimeoutError :
                    await ctx.send("시간이 초과되었습니다.\n"
                                   f"다시 명령어를 입력해주세요\n"
                                   f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
                else :
                    image = image_msg.attachments[0]
                edit_colorCode = "0x" + str(colorCode)  # 역할 색상
                embed3 = discord.Embed(title="입력 결과", color=discord.Color.green())
                embed3.add_field(name="팀 약자", value=abbName)
                embed3.add_field(name="풀네임", value=fullName)
                embed3.add_field(name="색상코드", value=colorCode)
                embed3.set_thumbnail(url=image.url)
                await embed_msg.delete()
                await ctx.send(embed=embed3)

                # 디스코드 상호작용
                guild = ctx.guild
                await guild.create_role(name=abbName, colour=discord.Colour.from_str(edit_colorCode))  # 역할 생성
                await asyncio.sleep(1)
                for man in people :
                    role = get(ctx.guild.roles, name=abbName)
                    await man.add_roles(role)
                    await ctx.send(f"{man.display_name} - {abbName} 역할 추가 완료")

                # 디스코드 이적센터 채널 게시
                channel = get(ctx.guild.channels, name=config.TRANSFER_CENTER)
                await channel.send(f"<팀 창단>\n"
                                   f"팀명 : {fullName}\n"
                                   f"팀약자 : {abbName}\n"
                                   f"팀 색상 : {colorCode}\n"
                                   f"팀 이미지 : {logoLink}\n"
                                   f"팀 카테고리 및 역할 이미지는 별도로 스태프가 설정해야합니다.")

                # DB TEAM_INFORMATION 인서트
                try :
                    conn = sqlite3.connect("CEF.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO TEAM_INFORMATION VALUES(?, ?, ?, ?, ?, ?);",
                                (abbName, fullName, colorCode, lastRank, "", image.url))
                    await ctx.send("DB 추가 완료")
                except :
                    await ctx.send("DB 업데이트 오류 발생. 다시 시도해주세요")
                finally :
                    conn.commit()
                    conn.close()
                await ctx.reply("역할 이모지는 서버 설정에서 별도로 설정해주세요.")


        else :
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='팀해체(미완)', pass_context=True,
                      help="권한 : 스태프 전용\n"
                           "팀 명단 체크, 팀 정보(팀약자, 풀네임, 색상코드, 로고 링크) 입력, DB 삭제 등 팀 해체를 진행합니다.\n",
                      brief="$해채 '팀약자'")
    async def _deleteTeam(self, ctx) :
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            # 소속 팀원 역할 제거

            # DB - USER_INFORMATION 소속 선수들 소속명 'FA'로 수정

            # DB - TEAM_INFORMATION 정보 삭제

            # 소속 역할 삭제
            pass
        else :
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name="이적", pass_context=True,
                      help="권한 : 스태프 전용\n"
                           "특정 인원의 이적 과정을 진행합니다.\n"
                           "기존 계약 여부 검사, FA 역할 제거, 팀 역할 추가, 이적센터 게시 등의 모든 과정을 처리합니다.\n"
                           "계약시작일의 경우 앞의 연도 생략 시 현재 연도로 자동 계산됩니다.\n"
                           "사용 예시 : $이적 @타임제이 FCB 11/7 20 or $이적 @타임제이 FCB 23/11/7 20",
                      brief="$이적 @멘션 '팀약자' '계약시작일' '계약기간'")
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
                                if abbTeamName not in memberRoleList :
                                    # 디스코드 내 작업 - FA 역할 회수
                                    if "FA (무소속)" in memberRoleList :
                                        role = get(ctx.guild.roles, name="FA (무소속)")
                                        await member.remove_roles(role)  # O
                                        await ctx.reply(f"FA 역할 제거", delete_after=delete_time)
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

    @commands.command(name='FA전환(미완)', pass_context=True,
                      help="권한 : 스태프 전용\n"
                           "특정 인원을 FA로 전환합니다.\n"
                           "멘션한 인원의 계약 정보, 팀 역할 등을 삭제합니다.",
                      brief="$FA전환 @멘션")
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

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"스태프전용_팀관리 : {error}")


async def setup(bot) :
    await bot.add_cog(스태프전용_팀관리(bot))
