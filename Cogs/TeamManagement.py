import discord
from discord.ext import commands
import asyncio
import config
import myfun
from discord.utils import get
from forAccessDB import *
from table2ascii import table2ascii as t2a, PresetStyle

bbNameFromChangeRankInTeam = ""
playerList = []
class MenuAboutChangeHeadButtonFuntion(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    @discord.ui.button(label='감독 변경', style=discord.ButtonStyle.secondary, row=1)
    async def menubutton1(self, interaction: discord.Interaction, button: discord.ui.Button) :
        await interaction.channel.send("버튼1 - 감독 변경")
        await interaction.response.defer()
        await interaction.edit_original_response(content="```감독 변경을 선택하였습니다.\n"
                                                         "변경할 감독의 번호를 선택해주세요.",
                                                 view=None)

    @discord.ui.button(label='코치 변경', style=discord.ButtonStyle.secondary, row=1)
    async def menubutton2(self, interaction: discord.Interaction, button: discord.ui.Button) :
        await interaction.channel.send("버튼1 - 코치 변경")
        await interaction.response.defer()
        await interaction.edit_original_response(content="```코치 변경을 선택하였습니다.\n"
                                                         "메뉴 번호를 선택 혹은 입력하세요.\n"
                                                         "1 - 코치 임명\n"
                                                         "2 - 코치 해임```")


class MenuAboutChangeCoachButtonFuntion(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
    @discord.ui.button(label='코치 임명', style=discord.ButtonStyle.secondary, row=1)
    async def changeCocachButton1(self, interaction: discord.Interaction, button: discord.ui.Button) :
        await interaction.channel.send("버튼 - 코치 임명")
        await interaction.response.defer()
        await interaction.edit_original_response(content="```코치 선임 -> \n"
                                                         "코치 선임을 선택하였습니다.\n"
                                                         "코치로 선임할 선수의 번호 혹은 버튼을 선택하세요.```",
                                                 view=None)


    @discord.ui.button(label='코치 해임', style=discord.ButtonStyle.secondary, row=1)
    async def changeCocachButton2(self, interaction: discord.Interaction, button: discord.ui.Button) :
        await interaction.channel.send("버튼 - 코치 해임")
        await interaction.response.defer()
        await interaction.edit_original_response(content="```코치 변경 -> \n"
                                                         "코치 해임을 선택하였습니다.\n"
                                                         "해임할 코치의 번호 혹은 버튼을 선택하세요.```",
                                                 view=None)

class ButtonFunction(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)

    @discord.ui.button(label='닉네임', style=discord.ButtonStyle.secondary, row=1)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button) :
        global sortSwitch, gl_teamname
        sortSwitch = 0
        outfutList = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (gl_teamname,))
        result = cur.fetchall()

        fullTeamName = getTeamFullNameFromTeamInfor(gl_teamname)
        for row in result :
            try :
                nickname = getNicknameFromUserInfoWithID(row[0])
                startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                period = getPeriodFromContractwithID(row[0])
                endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                outfutList.append([nickname, startDate, period, endDate, remainDate])
            except :
                pass
        outfutList.sort(key=lambda x : x[sortSwitch])
        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
            body=outfutList,
            style=PresetStyle.borderless
        )
        await interaction.response.defer()
        await interaction.edit_original_response(content=f"```\n"
                                                        f"<{fullTeamName} 계약 현황>\n"
                                                        f"정렬 기준 : 닉네임\n"
                                                        f"\n{output}\n```",  view=ButtonFunction())

    @discord.ui.button(label='계약 시작일', style=discord.ButtonStyle.secondary, row=1)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button) :
        global sortSwitch, gl_teamname
        sortSwitch = 1
        outfutList = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (gl_teamname,))
        result = cur.fetchall()
        fullTeamName = getTeamFullNameFromTeamInfor(gl_teamname)
        for row in result :
            try :
                nickname = getNicknameFromUserInfoWithID(row[0])
                startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                period = getPeriodFromContractwithID(row[0])
                endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                outfutList.append([nickname, startDate, period, endDate, remainDate])
            except :
                pass
        outfutList.sort(key=lambda x : x[sortSwitch])
        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
            body=outfutList,
            style=PresetStyle.borderless
        )
        await interaction.response.defer()
        await interaction.edit_original_response(content=f"```\n"
                                                        f"<{fullTeamName} 계약 현황>\n"
                                                        f"정렬 기준 : 계약 시작일\n"
                                                        f"\n{output}\n```",  view=ButtonFunction())

    @discord.ui.button(label='계약기간', style=discord.ButtonStyle.secondary, row=1)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button) :
        global sortSwitch, gl_teamname
        sortSwitch = 2
        outfutList = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (gl_teamname,))
        result = cur.fetchall()
        fullTeamName = getTeamFullNameFromTeamInfor(gl_teamname)
        for row in result :
            try :
                nickname = getNicknameFromUserInfoWithID(row[0])
                startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                period = getPeriodFromContractwithID(row[0])
                endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                outfutList.append([nickname, startDate, period, endDate, remainDate])
            except :
                pass
        outfutList.sort(key=lambda x : x[sortSwitch])
        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
            body=outfutList,
            style=PresetStyle.borderless
        )
        await interaction.response.defer()
        await interaction.edit_original_response(content=f"```\n"
                                                        f"<{fullTeamName} 계약 현황>\n"
                                                        f"정렬 기준 : 계약기간\n"
                                                        f"\n{output}\n```",  view=ButtonFunction())

    @discord.ui.button(label='계약 종료일', style=discord.ButtonStyle.secondary, row=1)
    async def button4(self, interaction: discord.Interaction, button: discord.ui.Button) :
        global sortSwitch, gl_teamname
        sortSwitch = 3
        outfutList = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (gl_teamname,))
        result = cur.fetchall()
        fullTeamName = getTeamFullNameFromTeamInfor(gl_teamname)
        for row in result :
            try :
                nickname = getNicknameFromUserInfoWithID(row[0])
                print(nickname)
                startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                print(startDate)
                period = getPeriodFromContractwithID(row[0])
                print(period)
                endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                print(endDate)
                remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                print(remainDate)
                outfutList.append([nickname, startDate, period, endDate, remainDate])
            except :
                pass
        outfutList.sort(key=lambda x : x[sortSwitch])
        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
            body=outfutList,
            style=PresetStyle.borderless
        )
        await interaction.response.defer()
        await interaction.edit_original_response(content=f"```\n"
                                                        f"<{fullTeamName} 계약 현황>\n"
                                                        f"정렬 기준 : 계약 종료일\n"
                                                        f"\n{output}\n```",  view=ButtonFunction())

    @discord.ui.button(label='남은 기간', style=discord.ButtonStyle.secondary, row=1)
    async def button5(self, interaction: discord.Interaction, button: discord.ui.Button) :
        global sortSwitch, gl_teamname
        sortSwitch = 4
        outfutList = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (gl_teamname,))
        result = cur.fetchall()
        fullTeamName = getTeamFullNameFromTeamInfor(gl_teamname)
        for row in result :
            try :
                nickname = getNicknameFromUserInfoWithID(row[0])
                startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                period = getPeriodFromContractwithID(row[0])
                endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                outfutList.append([nickname, startDate, period, endDate, remainDate])
            except :
                pass
        outfutList.sort(key=lambda x : x[sortSwitch])
        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
            body=outfutList,
            style=PresetStyle.borderless
        )
        await interaction.response.defer()
        await interaction.edit_original_response(content=f"```\n"
                                                        f"<{fullTeamName} 계약 현황>\n"
                                                        f"정렬 기준 : 남은 기간\n"
                                                        f"\n{output}\n```",  view=ButtonFunction())

class 팀관리(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='직책변경', pass_context=True)
    async def _changeRankInTeam(self, ctx) :
        # 0. 감독 역할 확인 및 소속 팀 정보(myTeam), 이전 감독, 코치 저장
        role_names = [role.name for role in ctx.author.roles]
        if "감독" in role_names :
            insertHeadLoopSwitch = True
            myTeam = getMyTeam(ctx)
            exHead = [myfun.getNickFromDisplayname(ctx)]
            exCoach = ['', '']
            newHead = []
            newCoach = []
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT Nickname FROM USER_INFORMATION WHERE TeamName=? and Rank=?", (myTeam, "코치"))
            result = cur.fetchall()
            for i, idx in enumerate(result) :
                if idx[0] != "" :
                    exCoach[i] = idx[i]
            # 1. 감독 변경
            # 1-1. 팀원 리스트 출력 및 버튼(팀원) 추가, 건너뛰기, 종료 버튼 추가
            selectListText = '0. 변경 안함\n'
            selectList = []
            getteamli = getTeammateList(myTeam)
            getteamli.remove(myfun.getNickFromDisplayname(ctx))
            getteamli.sort()
            for i, teammate in enumerate(getteamli, start=1) :
                selectList.append((i, teammate))
                selectListText = selectListText + str(i) + ". " + teammate + "\n"

            embed = discord.Embed(title=f"{getTeamFullNameFromTeamInfor(myTeam)} 직책 변경")
            # embed.add_field(name="감독 변경", value=f"{myfun.getNickFromDisplayname(ctx)} -> ")
            # embed.add_field(name="코치 변경", value=f"{exCoach[0]}, {exCoach[1]} -> ")
            embed.add_field(name="팀원 목록", value=selectListText)

            embed.set_footer(text="맞으면 1, 틀리면 2를 입력하세요.")
            ann_embed = await ctx.send(embed=embed)

            while insertHeadLoopSwitch :
                try :
                    msg = await self.bot.wait_for("message",
                                                  check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=30.0)
                except asyncio.TimeoutError :
                    await ann_embed.delete()
                    await ctx.send(f"시간이 초과되었습니다.\n"
                                   f"다시 명령어를 입력해주세요\n"
                                   f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
                else :
                    select = int(msg.content) - 1
                    choiceHead = selectList[select][1]
                    newHead.append(choiceHead)
                    # 확인 작업
                    check_question = await ctx.send(f"변경할 감독 : {newHead[0]}\n"
                                                    f"맞으면 1번, 틀리면 2번을 입력하세요.")
                    checkLoopSwitch = True
                    while checkLoopSwitch :
                        try :
                            check_msg = await self.bot.wait_for("message",
                                                                check=lambda
                                                                    m : m.author == ctx.author and m.channel == ctx.channel,
                                                                timeout=30.0)
                        except asyncio.TimeoutError :
                            await ann_embed.delete()
                            await ctx.send(f"시간이 초과되었습니다.\n"
                                           f"다시 명령어를 입력해주세요\n"
                                           f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
                        else :
                            if check_msg.content == "0" :
                                await ann_embed.delete()
                                await ctx.send("강제 종료되었습니다.")
                                checkLoopSwitch = False
                                insertHeadLoopSwitch = False
                            elif check_msg.content == "1" :
                                await ctx.send(f"{selectList[select][1]}")
                            elif check_msg.content == "2" :
                                checkLoopSwitch = False

            # 1-1-1. 팀원 선택 시, 감독 변경 -> 3번으로 이동
            # 1-1-2. 건너뛰기 선택 시, 2로 이동
            # 1-1-3. 종료 선택 시, 강제종료 (메뉴 삭제 및 종료 멘트 출력)

            # 2. 코치 변경
            # 2-1. 메뉴 (현재 코치 목록), 버튼(선임, 해임, 뒤로가기, 종료) 추가
            # 2-2. 선임 선택 시,
            # 2-2-1. 팀원 리스트 출력 및 버튼 추가, 건너뛰기, 종료 버튼 추가
            # 2-2-1-1. 팀원 선택 시, 정보 저장(exHead = ctx, newHead) -> 3번으로 이동
            # 2-2-2. 건너뛰기 선택 시, 3으로 이동
            # 2-2-3. 종료 선택 시, 강제종료 (메뉴 삭제 및 종료 멘트 출력)

            # 3. 확인 작업
            # 3-1. 선택한 정보 출력(건너뛰기 선택한 항목은 미출력)
            # 3-2. 버튼(확인, 뒤로가기, 종료) 추가
            # 3-2-1. 확인 선택 시
            # 3-2-1-1. 디스코드 상호 작용 - 역할 : 기존 감독 역할(감독, 코치) 제거, 선택한 팀원에 감독 역할(감독, 코치) 추가
            # 3-2-1-2. 디스코드 상호 작용 - 게시 : 이적센터 채널에 감독 변경 명시
            # 3-2-1-3. DB 상호 작용 : 기존 감독 Rank 선수로 변경
            # 3-2-2. 뒤로가기 선택 시, 2로 이동
            # 3-2-3. 종료 선택 시, 강제종료 (메뉴 삭제 및 종료 멘트 출력)



    @commands.command(name='팀정보수정', pass_context=True,
                      help="권한 : 스태프 전용\n"
                           "팀 정보(팀약자, 풀네임, 색상코드, 로고 링크)를 수정합니다.\n",
                      brief="$해채 '팀약자'")
    async def _editTeamInfor(self, ctx) :
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
            for row in result :
                if row[0] == "FA" :
                    pass
                else :
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
            else :
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
                        if msg.content.lower() == "1" :
                            temp_msg = await ctx.send("```<1. 팀 약자 수정>\n"
                                                      "수정할 이름을 입력하세요.```")
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
                                edit_abbName = msg1.content.upper()
                                await ctx.channel.purge(limit=1)
                        # 팀 풀네임 수정
                        elif msg.content.lower() == "2" :
                            temp_msg = await ctx.send("```<2. 팀 풀네임 수정>\n"
                                                      "수정할 이름을 입력하세요.```")
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
                                edit_fullName = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 색상 코드 수정
                        elif msg.content.lower() == "3" :
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
                                if "#" in msg1.content :
                                    msg.content.replace("#", "")
                                edit_colorCode = msg1.content
                                await ctx.channel.purge(limit=1)
                        # 팀 이모지 코드 수정
                        elif msg.content.lower() == "4" :
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
                        elif msg.content.lower() == "5" :
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
                        elif msg.content.lower() == "6" :
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
                            else :
                                await result.delete()
                                # 다음 단계 진행
                                print(msg2.content)
                                if msg2.content == "1" :
                                    print(1, loop_switch)
                                    loop_switch = False
                                    switch = msg2.content
                                    await ctx.channel.purge(limit=1)
                                    print(switch)
                                # 이전 단계 복귀
                                elif msg2.content == "2" :
                                    print(2, loop_switch)
                                    loop_switch = True
                                    switch = msg2.content
                                    await ctx.channel.purge(limit=1)
                                elif msg2.content == "3" :
                                    print(3, loop_switch)
                                    await ctx.channel.purge(limit=1)
                                    await ctx.send("강제 종료되었습니다.", delete_after=15)
                                    loop_switch = False
                                    switch = msg2.content
            else :
                text = ''
                for abb in abbList :
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
                if fullName != edit_fullName :
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt :
                            cur.execute("UPDATE TEAM_INFORMATION SET TeamName=? WHERE Abbreviation=?",
                                        (edit_fullName, edit_abbName))
                        else :
                            cur.execute("UPDATE TEAM_INFORMATION SET TeamName=? WHERE Abbreviation=?",
                                        (edit_fullName, abbName))
                    finally :
                        conn.commit()
                        conn.close()
                        await ctx.send("풀네임 수정 완료")
                # 팀 색상 코드 수정
                if colorCode != edit_colorCode :
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        if swt :
                            cur.execute("UPDATE TEAM_INFORMATION SET ColorCode=? WHERE Abbreviation=?",
                                        (edit_colorCode, edit_abbName))
                        else :
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
                if imoji != edit_imoji :
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

        else :
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"팀관리 전용 : {error}")
async def setup(bot) :
    await bot.add_cog(팀관리(bot))