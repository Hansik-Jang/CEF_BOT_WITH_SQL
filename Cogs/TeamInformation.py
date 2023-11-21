import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
import config
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

class Dropdown(discord.ui.Select) :
    def __init__(self) :
        # 옵션에 팀 정보 받아서 넣기
        options = []
        teamTemp = getTeamList()
        for name in teamTemp:
            options.append(discord.SelectOption(label=name,
                                                description=f"{getTeamFullNameFromTeamInfor(name)}",
                                                emoji=f"{getImojiFromTeamInfor(name)}"))

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='팀 선택', min_values=1, max_values=1, options=options)

    # 드롭다운 선택 시 상호작용
    async def callback(self, interaction: discord.Interaction) :
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        # 상호 작용 메시지 세팅
        sortResult = ['', '', '', '', '', '', '', '', '', '']
        colour = getStringColorCodeFromTeamInfor(self.values[0])
        role = str(len(get(interaction.guild.roles, name=self.values[0]).members))
        if colour == "":
            embed = discord.Embed(title=f"{getImojiFromTeamInfor(self.values[0])} {getTeamFullNameFromTeamInfor(self.values[0])}")
        else:
            embed = discord.Embed(title=getTeamFullNameFromTeamInfor(self.values[0]), colour=colour)
        embed.add_field(name="팀 정보",
                        value=f"현재 인원 : {str(len(get(interaction.guild.roles, name=self.values[0]).members))} 명\n"
                              f"지난 순위 : {getLastRankFromTeamInfor(self.values[0])}",
                        inline=False)
        if getLogoFromTeamInfor(self.values[0]) != '':
            embed.set_thumbnail(url=getLogoFromTeamInfor(self.values[0]))
        # DB 정보 얻기
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE TeamName=?", (self.values[0], ))
        teamList = cur.fetchall()
        # DB 정보 정렬하여 Embed로 정리
        for data in teamList :
            if data[2] == "LW" :
                sortResult[0] = sortResult[0] + data[1] + "\n"
            elif data[2] == "ST" :
                sortResult[1] = sortResult[1] + data[1] + "\n"
            elif data[2] == "RW" :
                sortResult[2] = sortResult[2] + data[1] + "\n"
            elif data[2] == "CAM" :
                sortResult[3] = sortResult[3] + data[1] + "\n"
            elif data[2] == "CM" :
                sortResult[4] = sortResult[4] + data[1] + "\n"
            elif data[2] == "CDM" :
                sortResult[5] = sortResult[5] + data[1] + "\n"
            elif data[2] == "LB" :
                sortResult[6] = sortResult[6] + data[1] + "\n"
            elif data[2] == "CB" :
                sortResult[7] = sortResult[7] + data[1] + "\n"
            elif data[2] == "RB" :
                sortResult[8] = sortResult[8] + data[1] + "\n"
            elif data[2] == "GK" :
                sortResult[9] = sortResult[9] + data[1] + "\n"

        for i, position in enumerate(config.positionList) :
            embed.add_field(name=position, value=sortResult[i])

        # 상호 작용
        await interaction.response.defer()
        msg = await interaction.original_response()
        await msg.edit(content=f"{self.values[0]}을 선택하였습니다.", embed=embed)

class DropdownView(discord.ui.View) :
    def __init__(self) :
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())


class 팀정보(commands.Cog):
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
            abbName = row[0]
            fullName = row[1]
            if row[3] == -1 :
                lastRank = ""
            elif row[3] == 99 :
                lastRank = "New"
            elif row[3] == 100 :
                lastRank = "-"
            else :
                # lastRank = "지난 시즌 : " + str(row[3]) + " 위"
                lastRank = str(row[3]) + " 위"
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
        view = DropdownView()
        # Sending a message containing our view
        await ctx.send('조회할 팀을 선택하세요.', embed=embed, view=view)

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
                    print(remainDate)
                    if remainDate < 0:
                        remainDate = "만료"
                    elif remainDate == 0:
                        remainDate = "만료 임박"
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

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"팀정보 전용 : {error}")

async def setup(bot) :
    await bot.add_cog(팀정보(bot))