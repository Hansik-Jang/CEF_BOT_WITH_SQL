import discord
from discord.ext import commands
import sqlite3
import myfun
from discord.utils import get
from forAccessDB import *
import asyncio


class ManageTeam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='팀등록', pass_context=True)
    async def _registerTeam(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            abbName = ""
            fullName = ""
            colorCode = ""
            lastRank = 99
            imoji = ""
            logoLink = ""
            loop_switch = 1
            text = ("1. 팀약자 : \n"
                    "2. 풀네임 : \n"
                    "3. 색상코드 : \n"
                    "4. 이모지 : \n"
                    "5. 로고 링크 : \n\n"
                    "<TIP>\n"
                    "1. 이모지는 명령어 사용 전 미리 등록한 후 로고 입력 후 로고 앞에 '\'를 붙여 다음과 같은 형태를 입력해야 합니다.\n"
                    "<로고이름:로고 ID 번호>\n"
                    "2. 로고 링크는 채팅 채널에 이미지 업로드 후 우클릭하여 링크 복사하기를 하여 '이미지 링크'를 입력해주세요.\n")
            embed = discord.Embed(title="팀등록 절차를 시작합니다.", description=text, color=discord.Color.red())
            embed_msg = await ctx.send(embed=embed)
            while loop_switch < 6:
                print(loop_switch)
                if abbName == "":
                    text1 = f"1. 팀약자 : {abbName} (입력 X)\n"
                else:
                    text1 = f"1. 팀약자 : {abbName} (입력 O)\n"
                if fullName == "":
                    text2 = f"2. 풀네임 : {fullName} (입력 X)\n"
                else:
                    text2 = f"2. 풀네임 : {fullName} (입력 O)\n"
                if colorCode == "":
                    text3 = f"3. 색상코드 : {colorCode} (입력 X)\n"
                else:
                    text3 = f"3. 색상코드 : {colorCode} (입력 X)\n"
                if imoji == "":
                    text4 = f"4. 이모지 : {imoji} (입력 X)\n"
                else:
                    text4 = f"4. 이모지 : {imoji} (입력 O)\n"
                if logoLink == "":
                    text5 = f"5. 로고 링크 : {logoLink} (입력 X)\n"
                else:
                    text5 = f"5. 로고 링크 : {logoLink} (입력 O)\n"
                text6 = "6. 강제 종료하기\n\n"
                text_tip = (f"<TIP>\n"
                           f"1. 이모지는 명령어 사용 전 미리 등록한 후 로고 입력 후 로고 앞에 '\'를 붙여 다음과 같은 형태를 입력해야 합니다.\n"
                           f"   <로고이름:로고 ID 번호>\n"
                           f"2. 로고 링크는 채팅 채널에 이미지 업로드 후 우클릭하여 링크 복사하기를 하여 '이미지 링크'를 입력해주세요.\n")
                text = text1 + text2 + text3 + text4 + text5 + text6 + text_tip
                exitText = text1 + text2 + text3 + text4 + text5
                embed2 = discord.Embed(title="팀등록 절차를 시작합니다.", description=text, color=discord.Color.yellow())
                await embed_msg.edit(embed=embed2)
                ann_msg = await ctx.send("안내 문구에 따라 정보를 입력해주세요.")

                if loop_switch == 1:
                    temp_msg = await ann_msg.edit(content="안내 문구에 따라 정보를 입력해주세요."
                                                          "\n1번. 팀약자를 입력해주세요.")
                elif loop_switch == 2:
                    temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                          "\n2번. 팀이름 전체를 대소문자 구분하여 입력해주세요.")
                elif loop_switch == 3:
                    temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                          "\n3번. 팀 색상코드 #을 제외한 6자리를 입력해주세요. ")
                elif loop_switch == 4:
                    temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                          "\n4번. TIP 1번을 참고하여 이모지를 입력해주세요.")
                elif loop_switch == 5:
                    temp_msg = await ann_msg.edit(content=f"안내 문구에 따라 정보를 입력해주세요."
                                                          "\n5번. TIP 2번을 참고하여 이미지 링크를 입력해주세요.")
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
                    print(type(msg2.content), msg2.content)
                    if loop_switch == 1:
                        await temp_msg.delete()
                        await ctx.channel.purge(limit=1)
                        abbName = msg2.content.upper()
                    elif loop_switch == 2:
                        await temp_msg.delete()
                        await ctx.channel.purge(limit=1)
                        fullName = msg2.content
                    elif loop_switch == 3:
                        await temp_msg.delete()
                        await ctx.channel.purge(limit=1)
                        colorCode = msg2.content
                    elif loop_switch == 4:
                        await temp_msg.delete()
                        await ctx.channel.purge(limit=1)
                        imoji = msg2.content
                    elif loop_switch == 5:
                        await temp_msg.delete()
                        await ctx.channel.purge(limit=1)
                        logoLink = str(msg2.content)
                loop_switch += 1
            embed3 = discord.Embed(title="입력 결과", description=exitText, color=discord.Color.yellow())
            await embed_msg.delete()
            await ctx.send(embed=embed3)

            # 디스코드 상호작용
            x = "0x" + str(colorCode)
            guild = ctx.guild
            await guild.create_role(name=abbName, colour=discord.Colour.from_str(x))
            #await getRole.edit(color=discord.Colour.from_str(x))
            # DB TEAM_INFORMATION 인서트
            try:
                conn = sqlite3.connect("CEF.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO TEAM_INFORMATION VALUES(?, ?, ?, ?, ?, ?);",
                            (abbName, fullName, colorCode, lastRank, imoji, logoLink))
            finally:
                conn.commit()
                conn.close()
            await ctx.send("역할 이모지는 별도로 설정해야 합니다.")
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='팀해체', pass_context=True)
    async def _deleteTeam(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='팀정보수정', pass_context=True)
    async def _editTeamInfor(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        switch = ""
        if "스태프" in role_names :
            abbName = ""
            edit_abbName = ""
            edit_fullName = ""
            edit_colorCode = ""
            edit_imoji = ""
            edit_logo = ""
            swt = False
            loop_switch = True
            temp = ''
            abbList = []
            await ctx.channel.purge(limit=1)
            # 팀 약자 정보 획득
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT Abbreviation From TEAM_INFORMATION")
            result = cur.fetchall()
            result.sort()
            # 임베드 작업
            embed = discord.Embed(title="현재 팀 목록")
            for row in result:
                if row[0] == "FA":
                    pass
                else:
                    abbList.append(row[0])
                    embed.add_field(name=f"{row[0]}", value=" ", inline=True)
            ann_msg = await ctx.send(f"```팀 정보 수정합니다.\n"
                                     f"수정할 팀의 이름를 입력해주세요.\n"
                                     f"{temp}```")
            embed_msg = await ctx.send(embed=embed)
            # 팀 약자 입력
            try :
                msg = await self.bot.wait_for("message",
                                              check=lambda
                                                  m : m.author == ctx.author and m.channel == ctx.channel,
                                              timeout=30.0)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.\n"
                               f"다시 명령어를 입력해주세요\n"
                               f"해당 메시지는 30초 후 자동 삭제됩니다.", delete_after=15)
            else:
                await ctx.channel.purge(limit=1)
                abbName = msg.content.upper()

            # ----------------- 수정할 항목 선택 -----------------
            if abbName in abbList :
                while loop_switch :
                    print(0, loop_switch)
                    fullName = getTeamFullNameFromTeamInfor(abbName)
                    colorCode = getColorCodeFromTeamInfor(abbName)
                    imoji = getImojiFromTeamInfor(abbName)
                    logo = getLogoFromTeamInfor(abbName)
                    await ann_msg.edit(content=f"```<입력 현황>\n"
                                               f"팀 약자 : {abbName} -> {edit_abbName}\n"
                                               f"팀 이름 : {fullName} -> {edit_fullName}\n"
                                               f"색상 코드 : {colorCode} -> {edit_colorCode}\n```"
                                               f"이모지 : {imoji} -> {edit_imoji}\n"
                                               f"로고 : {logo} -> {edit_logo}")
                    embed2 = discord.Embed(title="변경할 항목 선택", description="선택할 번호를 입력하세요.")
                    embed2.add_field(name="1.", value="팀약자", inline=True)
                    embed2.add_field(name="2.", value="풀네임", inline=True)
                    embed2.add_field(name="3.", value="색상코드", inline=True)
                    embed2.add_field(name="4.", value="이모지", inline=True)
                    embed2.add_field(name="5.", value="이미지", inline=True)
                    embed2.add_field(name="6.", value="종료하기", inline=True)
                    await embed_msg.edit(embed=embed2)
                    # 번호 선택
                    try :
                        msg = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=30.0)
                    except asyncio.TimeoutError :
                        await ctx.send("시간이 초과되었습니다.\n"
                                       f"다시 명령어를 입력해주세요\n"
                                       f"해당 메시지는 30초 후 자동 삭제됩니다.", delete_after=15)
                        break
                    else :
                        # 팀 약자 수정
                        await ctx.channel.purge(limit=1)
                        if msg.content.lower() == "1":
                            temp_msg = await ctx.send("```<1. 팀 약자 수정>\n"
                                                      "수정할 이름을 입력하세요.```")
                            try :
                                msg1 = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == ctx.channel,
                                                          timeout=30.0)
                            except asyncio.TimeoutError:
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else:
                                await temp_msg.delete()
                                edit_abbName = msg1.content.upper()
                                await ctx.channel.purge(limit=1)
                        # 팀 풀네임 수정
                        elif msg.content.lower() == "2":
                            temp_msg = await ctx.send("```<2. 팀 풀네임 수정>\n"
                                                      "수정할 이름을 입력하세요.```")
                            try :
                                msg1 = await self.bot.wait_for("message",
                                                          check=lambda
                                                              m : m.author == ctx.author and m.channel == ctx.channel,
                                                          timeout=30.0)
                            except asyncio.TimeoutError:
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else:
                                await temp_msg.delete()
                                edit_fullName = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 색상 코드 수정
                        elif msg.content.lower() == "3":
                            temp_msg = await ctx.send("```<3. 팀 색상코드 수정>\n"
                                                      "수정할 색상코드를 입력하세요.```")
                            try :
                                msg1 = await self.bot.wait_for("message",
                                                               check=lambda
                                                                   m : m.author == ctx.author and m.channel == ctx.channel,
                                                               timeout=30.0)
                            except asyncio.TimeoutError :
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else :
                                await temp_msg.delete()
                                if "#" in msg1.content:
                                    msg.content.replace("#","")
                                edit_colorCode = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 팀 이모지 코드 수정
                        elif msg.content.lower() == "4":
                            temp_msg = await ctx.send("```<4. 팀 이모지 수정>\n"
                                                      "수정할 이모지 앞에 '\'를 붙인 후 입력하세요.\n```")
                            try :
                                msg1 = await self.bot.wait_for("message",
                                                               check=lambda
                                                                   m : m.author == ctx.author and m.channel == ctx.channel,
                                                               timeout=30.0)
                            except asyncio.TimeoutError :
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else :
                                await temp_msg.delete()
                                edit_imoji = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 팀 이미지 수정
                        elif msg.content.lower() == "5":
                            temp_msg = await ctx.send("```<5. 팀 이미지 수정>\n"
                                                      "수정할 팀 이미지의 링크를 입력하세요.```")
                            try :
                                msg1 = await self.bot.wait_for("message",
                                                               check=lambda
                                                                   m : m.author == ctx.author and m.channel == ctx.channel,
                                                               timeout=30.0)
                            except asyncio.TimeoutError :
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else :
                                await temp_msg.delete()
                                edit_logo = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 수정 완료 및 종료
                        elif msg.content.lower() == "6":
                            result = await ctx.send(f"```<입력 결과>\n"
                                                    f"팀 약자 : {abbName} -> {edit_abbName}\n"
                                                    f"팀 이름 : {fullName} -> {edit_fullName}\n"
                                                    f"색상 코드 : {colorCode} -> {edit_colorCode}\n```"
                                                    f"이모지 : {imoji} -> {edit_imoji}\n"
                                                    f"로고 : {logo} -> {edit_logo}\n"
                                                    f"```입력한 결과가 맞습니까?\n"
                                                    f"1 - 다음 단계로 진행하기\n"
                                                    f"2 - 수정 단계로 돌아가기\n"
                                                    f"3 - 강제 종료```")
                            try :
                                msg2 = await self.bot.wait_for("message",
                                                               check=lambda
                                                                   m : m.author == ctx.author and m.channel == ctx.channel,
                                                               timeout=30.0)
                            except asyncio.TimeoutError :
                                await ctx.send("시간이 초과되었습니다.\n"
                                               f"다시 명령어를 입력해주세요\n"
                                               f"해당 메시지는 30초 후 자동 삭제됩니다.")
                            else:
                                await result.delete()
                                # 다음 단계 진행
                                print(msg2.content)
                                if msg2.content == "1":
                                    print(1, loop_switch)
                                    loop_switch = False
                                    switch = msg2.content
                                    await ctx.channel.purge(limit=1)
                                    print(switch)
                                # 이전 단계 복귀
                                elif msg2.content == "2":
                                    print(2, loop_switch)
                                    loop_switch = True
                                    switch = msg2.content
                                    await ctx.channel.purge(limit=1)
                                elif msg2.content == "3":
                                    print(3, loop_switch)
                                    await ctx.channel.purge(limit=1)
                                    await ctx.send("강제 종료되었습니다.", delete_after=15)
                                    loop_switch = False
                                    switch = msg2.content
            else:
                text = ''
                for abb in abbList:
                    text = text + abb + ", "
                await ctx.reply(f"팀 약자를 잘못 입력하였습니다. 다시 시도해주세요.\n"
                                f"팀약자 목록 : {text}", delete_after=30)
            print("A", msg2.content, switch)
            # DB 저장 단계
            if switch == "1" :
                # USER_INFORMATION 팀원 정보 업데이트
                getRole = get(ctx.guild.roles, name=abbName)
                for member in getRole.members :
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("UPDATE USER_INFORMATION SET TeamName=? WHERE ID=?",
                                    (edit_abbName, member.id))
                        await ctx.send(f"{member.display_name} {edit_abbName} 업데이트 완료")
                    finally :
                        conn.commit()
                        conn.close()

                # TEAM_INFORMATION 업데이트
                # 팀 약자 수정
                if abbName != edit_abbName :
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("UPDATE TEAM_INFORMATION SET Abbreviation=? WHERE Abbreviation=?",
                                    (edit_abbName, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                    # 디스코드 작용
                    await getRole.edit(name=edit_abbName)
                    swt = True
                    await ctx.send("약자 수정 완료")
                # 팀 풀네임 수정
                if fullName != edit_fullName:
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt:
                            cur.execute("UPDATE TEAM_INFORMATION SET TeamName=? WHERE Abbreviation=?",
                                        (edit_fullName, edit_abbName))
                        else:
                            cur.execute("UPDATE TEAM_INFORMATION SET TeamName=? WHERE Abbreviation=?",
                                        (edit_fullName, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                        await ctx.send("풀네임 수정 완료")
                # 팀 색상 코드 수정
                if colorCode != edit_colorCode:
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt:
                            cur.execute("UPDATE TEAM_INFORMATION SET ColorCode=? WHERE Abbreviation=?",
                                        (edit_colorCode, edit_abbName))
                        else:
                            cur.execute("UPDATE TEAM_INFORMATION SET ColorCode=? WHERE Abbreviation=?",
                                        (edit_colorCode, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                    # 디스코드 작용
                    x = "0x" + str(edit_colorCode)
                    await getRole.edit(color=discord.Colour.from_str(x))
                    await ctx.send("색상코드 수정 완료")
                # 팀 이모지 수정
                if imoji != edit_imoji:
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt :
                            cur.execute("UPDATE TEAM_INFORMATION SET Imoji=? WHERE Abbreviation=?",
                                        (edit_imoji, edit_abbName))
                        else :
                            cur.execute("UPDATE TEAM_INFORMATION SET Imoji=? WHERE Abbreviation=?",
                                        (edit_imoji, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                    await ctx.send("이모지 수정 완료")
                # 팀 로고 수정
                if logo != edit_logo :
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt :
                            cur.execute("UPDATE TEAM_INFORMATION SET Logo=? WHERE Abbreviation=?",
                                        (logo, edit_abbName))
                        else :
                            cur.execute("UPDATE TEAM_INFORMATION SET Logo=? WHERE Abbreviation=?",
                                        (edit_logo, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                    await ctx.send("로고 수정 완료")

        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

async def setup(bot):
    await bot.add_cog(ManageTeam(bot))