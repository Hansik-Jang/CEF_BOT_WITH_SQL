import discord
from discord.ext import commands
from discord.utils import get
import sqlite3

import checkFun
import myfun
from forAccessDB import *
from datetime import datetime, timedelta
from table2ascii import table2ascii as t2a, PresetStyle

sortSwitch = 3
gl_teamname = ''
SHOW_LIST_SWITCH = True # True이면 전체, False이면 특정 팀
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


# --------------------------------------
class Contract(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='계약정보', pass_context=True,
                      help="권한 : 전체\n"
                           "팀약자를 입력 안 할 경우 : 전체 클럽원들 중 계약기간이 5일 이하로 남은 명단을 출력합니다.\n"
                           "팀약자를 입력 했을 경우 : 입력한 팀에 소속된 전체 팀원들의 계약 현황을 출력합니다.\n",
                      brief="$계약정보 or $게약정보 '팀약자'")
    async def _contractInfor(self, ctx, *, teamName=None):
        global gl_teamname, SHOW_LIST_SWITCH
        print(teamName)
        teamList = []
        resultList = []
        outfutList = []
        # 전체목록 출력
        if teamName is None:
            d0_text = ''
            d1_text = ''
            d2_text = ''
            d3_text = ''
            d4_text = ''
            d5_text = ''
            li = []
            SHOW_LIST_SWITCH = True
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM CONTRACT")
            result = cur.fetchall()
            for row in result:
                nickname = getNicknameFromUserInfoWithID(row[0])
                team = getTeamNameFromUserInfoWithID(row[0])
                endData = getEndDateFromContractwithID(row[0])
                remainDate = myfun.calculateRemainDate(endData)
                li.append((nickname, team, remainDate))

            li.sort(key=lambda x:x[2])

            for data in li:
                if data[2] == 0:
                    d0_text = d0_text + data[0] + " (" + data[1] + ")\n"
                elif data[2] == 1 :
                    d1_text = d1_text + data[0] + " (" + data[1] + ")\n"
                elif data[2] == 2 :
                    d2_text = d2_text + data[0] + " (" + data[1] + ")\n"
                elif data[2] == 3 :
                    d3_text = d3_text + data[0] + " (" + data[1] + ")\n"
                elif data[2] == 4 :
                    d4_text = d4_text + data[0] + " (" + data[1] + ")\n"
                elif data[2] == 5 :
                    d5_text = d5_text + data[0] + " (" + data[1] + ")\n"
            embed = discord.Embed(title="전체 목록", description=f"과한 정보 출력을 막기 위해 팀별로 만료일 기준 D-5인 인원만 출력합니다.\n더 많은 정보를 원할 경우 $계약정보 '팀약자'로 검색해주세요.")
            embed.add_field(name=f"D-Day", value=f"{d0_text}", inline=True)
            embed.add_field(name=f"D-1", value=f"{d1_text}", inline=True)
            embed.add_field(name=f"D-2", value=f"{d2_text}", inline=True)
            embed.add_field(name=f"D-3", value=f"{d3_text}", inline=True)
            embed.add_field(name=f"D-4", value=f"{d4_text}", inline=True)
            embed.add_field(name=f"D-5", value=f"{d5_text}", inline=True)

            await ctx.send(embed=embed)

        # 특정 팀 출력
        else:
            teamName = teamName.upper()
            gl_teamname = teamName
            SHOW_LIST_SWITCH = False
            fullTeamName = getTeamFullNameFromTeamInfor(teamName)
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT ID FROM USER_INFORMATION WHERE TeamName=?", (teamName,))
            result = cur.fetchall()
            print(result)
            for row in result:
                try:
                    nickname = getNicknameFromUserInfoWithID(row[0])
                    startDate = myfun.convertDate(getStartDateFromContractwithID(row[0]))
                    period = getPeriodFromContractwithID(row[0])
                    endDate = myfun.convertDate(getEndDateFromContractwithID(row[0]))
                    remainDate = myfun.calculateRemainDate(getEndDateFromContractwithID(row[0]))
                    outfutList.append([nickname, startDate, period, endDate, remainDate])
                except:
                    pass
            outfutList.sort(key=lambda x : x[sortSwitch])
            output = t2a(
                header=["닉네임", "계약 시작일", "계약기간", "계약 종료일", "남은 기간"],
                body=outfutList,
                style=PresetStyle.borderless
            )
            await ctx.send(f"```\n"
                           f"<{fullTeamName} 계약 현황>\n"
                           f""
                           f"\n{output}\n```",
                           view=ButtonFunction())

    # 추후 재계약으로 변경 필요
    @commands.command(name='계약수정', pass_context=True,
                      help="권한 : 스태프\n"
                           "멘션한 유저의 DB 내 계약 정보를 수정 및 업데이트합니다.\n\n"
                           "사용시 주의사항 : \n"
                           "1. 계약정보가 기존에 입력이 되있는 유저만 수정이 가능합니다.\n"
                           "2. 계약기간은 숫자만 입력해도 되지만 계약시작일은 '/'를 사용해 연도, 월, 일을 구분해줘야 합니다.\n"
                           "연도 미입력 시 자동으로 입력 날짜를 기준으로 연도를 계산하여 작동합니다.\n"
                           "사용 예시 : $계약수정 @타임제이 23/10/29 30 or $계약수정 @타임제이 10/29 30",
                      brief="$계약수정 '@멘션' '계약시작일' '계약기간'")
    async def _contractEdit(self, ctx, member:discord.Member, startDate=None, period=None):
        if checkFun.checkStaff(ctx) :
            if startDate is not None and period is not None :
                if '/' in startDate :
                    year_now = str(datetime.today().year) + "/"
                    print(year_now)
                    idnum = member.id
                    if year_now not in startDate :
                        startDate = year_now + startDate
                    startDate_time = myfun.convertTextToDatetime(startDate)
                    period2 = int(period) - 1
                    endData_time = startDate_time + timedelta(days=period2)
                    endData = myfun.convertDateTimeToText(endData_time)
                    if checkInsertOverapFromContractWithID(member.id):
                        await ctx.reply(f"{myfun.getNickFromDisplayname2(member.display_name)}, 계약서 미등록 유저입니다.")
                    else:
                        try :
                            conn = sqlite3.connect("CEF.db")
                            cur = conn.cursor()
                            cur.execute("UPDATE CONTRACT SET StartDate=?, Period=?, EndDate=? WHERE ID=?",
                                        (startDate, period, endData, idnum))
                            await ctx.reply(f"{myfun.getNickFromDisplayname2(member.display_name)}, DB에 업데이트 되었습니다.\n"
                                            f"계약 시작일 : {startDate}, 계약 종료일 : {endData} (총 계약기간 : {str(period)}일")
                        finally :
                            conn.commit()
                            conn.close()

                else :
                    await ctx.reply("아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                    "$계약입력 @멘션 계약시작일 계약기간\n"
                                    "작성 예시) $계약입력 @타임제이 2023/10/21 30")
            else :
                await ctx.reply("아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                "$계약입력 @멘션 계약시작일 계약기간\n"
                                "작성 예시) $계약입력 @타임제이 2023/10/21 30")
        else :
            await ctx.reply("해당 명령어는 스태프만 사용 가능합니다.")

    # 계약 정보 전체 = 예비FA목록
    @commands.command(name='예비FA목록', pass_context=True,
                      aliases=['예비FA'],
                      help="권한 : 전체\n"
                           "전체 클럽원들 중 계약기간이 5일 이하로 남은 명단을 출력합니다.",
                      brief="$예비FA목록 or $예비FA")
    async def _preliminaryList(self, ctx):
        d0_text = ''
        d1_text = ''
        d2_text = ''
        d3_text = ''
        d4_text = ''
        d5_text = ''
        li = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM CONTRACT")
        result = cur.fetchall()
        for row in result :
            nickname = getNicknameFromUserInfoWithID(row[0])
            team = getTeamNameFromUserInfoWithID(row[0])
            endData = getEndDateFromContractwithID(row[0])
            remainDate = myfun.calculateRemainDate(endData)
            li.append((nickname, team, remainDate))

        li.sort(key=lambda x : x[2])

        for data in li :
            if data[2] == 0 :
                d0_text = d0_text + data[0] + " (" + data[1] + ")\n"
            elif data[2] == 1 :
                d1_text = d1_text + data[0] + " (" + data[1] + ")\n"
            elif data[2] == 2 :
                d2_text = d2_text + data[0] + " (" + data[1] + ")\n"
            elif data[2] == 3 :
                d3_text = d3_text + data[0] + " (" + data[1] + ")\n"
            elif data[2] == 4 :
                d4_text = d4_text + data[0] + " (" + data[1] + ")\n"
            elif data[2] == 5 :
                d5_text = d5_text + data[0] + " (" + data[1] + ")\n"
        embed = discord.Embed(title="예비 FA 목록", description="   ")
        embed.add_field(name=f"D-Day", value=f"{d0_text}", inline=True)
        embed.add_field(name=f"D-1", value=f"{d1_text}", inline=True)
        embed.add_field(name=f"D-2", value=f"{d2_text}", inline=True)
        embed.add_field(name=f"D-3", value=f"{d3_text}", inline=True)
        embed.add_field(name=f"D-4", value=f"{d4_text}", inline=True)
        embed.add_field(name=f"D-5", value=f"{d5_text}", inline=True)

        await ctx.send(embed=embed)

    @commands.command(name='계약입력', pass_context=True,
                      aliases=[],
                      help="권한 : 스태프\n"
                           "멘션한 인원의 계약 정보를 DB에 추가합니다.\n\n"
                           "사용시 주의사항 : \n"
                           "1. 계약정보가 기존에 입력이 되있는 유저만 수정이 가능합니다.\n"
                           "2. 계약기간은 숫자만 입력해도 되지만 계약시작일은 '/'를 사용해 연도, 월, 일을 구분해줘야 합니다.\n"
                           "연도 미입력 시 자동으로 입력 날짜를 기준으로 연도를 계산하여 작동합니다.\n"
                           "사용 예시 : $계약입력 @타임제이 23/10/29 30 or $계약수정 @타임제이 10/29 30",
                      brief="$예비FA목록 or $예비FA")
    async def _insertContact(self, ctx, member:discord.Member, startDate=None, period=None):
        if checkFun.checkStaff(ctx):
            if startDate is not None and period is not None:
                if '/' in startDate:
                    year_now = str(datetime.today().year) + "/"
                    print(year_now)
                    idnum = member.id
                    if year_now not in startDate :
                        startDate = year_now + startDate
                    startDate_time = myfun.convertTextToDatetime(startDate)
                    period2 = int(period) - 1
                    endData_time = startDate_time + timedelta(days=period2)
                    endData = myfun.convertDateTimeToText(endData_time)
                    if checkInsertOverapFromContractWithID(member.id):
                        try:
                            conn = sqlite3.connect("CEF.db")
                            cur = conn.cursor()
                            cur.execute("INSERT INTO CONTRACT VALUES(?, ?, ?, ?);", (idnum, startDate, period, endData))
                            await ctx.reply(f"{myfun.getNickFromDisplayname2(member.display_name)}, DB에 업데이트 되었습니다.")
                        finally:
                            conn.commit()
                            conn.close()
                    else:
                        await ctx.reply(f"{myfun.getNickFromDisplayname2(member.display_name)}, 이미 등록되어 있습니다.")
                else:
                    await ctx.reply("아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                    "$계약입력 @멘션 계약시작일 계약기간\n"
                                    "작성 예시) $계약입력 @타임제이 2023/10/21 30")
            else:
                await ctx.reply("아래 명령어 사용법을 참고하여 입력해주세요.\n"
                                "$계약입력 @멘션 계약시작일 계약기간\n"
                                "작성 예시) $계약입력 @타임제이 2023/10/21 30")
        else :
            await ctx.reply("해당 명령어는 스태프만 사용 가능합니다.")



async def setup(bot):
    await bot.add_cog(Contract(bot))