import discord
from discord.ext import commands
import myfun
from discord.utils import get
from forAccessDB import *
import random
from datetime import datetime, timedelta
import config


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


class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='전체팀목록2', pass_context=True, aliases=['팀목록2', '전체팀명단2'],
                      help="권한 : 전체"
                           "\nCEF에 소속된 팀들의 총원과 지난 시즌 성적 등 정보를 출력합니다.",
                      brief="$전체팀목록")
    async def _wholeTeamList2(self, ctx) :
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION")
        result = cur.fetchall()
        result.sort(key=lambda x : x[3])
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
                if imoji == "" :
                    embed.add_field(name=f"{fullName}",
                                    value=f" - 팀 약자 : {abbName}\n"
                                          f"- 현재 인원 : {str(myfun.getRoleCount(ctx, abbName))} 명\n"
                                          f"- 지난 순위 : {lastRank}",
                                    inline=True)
                else :
                    embed.add_field(name=f"{imoji} {fullName}",
                                    value=f" - 팀 약자 : {abbName}\n"
                                          f"- 현재 인원 : {str(myfun.getRoleCount(ctx, abbName))} 명\n"
                                          f"- 지난 순위 : {lastRank}",
                                    inline=True)
        view = DropdownView()
        await ctx.send('조회할 팀을 선택하세요.', embed=embed, view=view)

        '''sortResult = ['', '', '', '', '', '', '', '', '', '']
        embed = discord.Embed(title="FA 목록")
        logo = getLogoFromTeamInfor("FA")
        color = getColorCodeFromTeamInfor("FA")
        # DB 정보 얻기
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE TeamName=?", ("FA", ))
        teamList = cur.fetchall()
        embed.set_thumbnail(url=getLogoFromTeamInfor("FA"))
        embed.set_footer(text=f"사용자 : {myfun.getNickFromDisplayname(ctx)}", icon_url=ctx.author.display_avatar)
        # DB 정보 정렬하여 Embed로 정리
        for data in teamList:
            if data[2] == "LW":
                sortResult[0] = sortResult[0] + data[1] + "\n"
            elif data[2] == "ST":
                sortResult[1] = sortResult[1] + data[1] + "\n"
            elif data[2] == "RW":
                sortResult[2] = sortResult[2] + data[1] + "\n"
            elif data[2] == "CAM":
                sortResult[3] = sortResult[3] + data[1] + "\n"
            elif data[2] == "CM":
                sortResult[4] = sortResult[4] + data[1] + "\n"
            elif data[2] == "CDM":
                sortResult[5] = sortResult[5] + data[1] + "\n"
            elif data[2] == "LB":
                sortResult[6] = sortResult[6] + data[1] + "\n"
            elif data[2] == "CB":
                sortResult[7] = sortResult[7] + data[1] + "\n"
            elif data[2] == "RB":
                sortResult[8] = sortResult[8] + data[1] + "\n"
            elif data[2] == "GK":
                sortResult[9] = sortResult[9] + data[1] + "\n"

        for i, position in enumerate(config.positionList):
            embed.add_field(name=position, value=sortResult[i])
        """Sends a message with our dropdown containing colours"""
        # Create the view containing our dropdown
        view = DropdownView()
        # Sending a message containing our view
        await ctx.send('조회할 팀을 선택하세요.', embed=embed, view=view)'''



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


    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"An error occurred in the Team cog: {error}")

async def setup(bot):
    await bot.add_cog(Team(bot))