import discord
from discord.ext import commands
from discord.utils import get
import checkFun
from forAccessDB import *
import config
import asyncio
import myfun
from table2ascii import table2ascii as t2a, PresetStyle


class 스태프전용_커리어(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.season = ""
        self.teamCount = ""
        self.teamSequence = []
        self.season2 = "24-1"
        self.teamCount2 = "13"
        self.teamSequence2 = ["RMA", "ESP", "FRA", "B04", "IPD", "ARG", "ITA", "BVB", "BHA", "TOT", "GER", "EVE", "LIV"]

    @commands.command(name='토츠', pass_context=True,
                      help="권한 : 스태프\n"
                           "토츠 정보를 추가합니다.",
                      brief="$토츠")
    async def _awardTots(self, ctx) :
        # ID, Season, FW_Tots, FW_Nomi, MF_Tots, MF_Nomi, DF_Tots, DF_Nomi, GK_Tots, GK_Nomi
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            tots = '토츠'
            position = "FW"
            totsFW = []
            totsMF = []
            totsDF = []
            totsGK = []
            nomiFW = []
            nomiMF = []
            nomiDF = []
            nomiGK = []
            totsList = [totsFW, totsMF, totsDF, totsGK, nomiFW, nomiMF, nomiDF, nomiGK]
            t_totsFW = ""
            t_totsMF = ""
            t_totsDF = ""
            t_totsGK = ""
            t_nomiFW = ""
            t_nomiMF = ""
            t_nomiDF = ""
            t_nomiGK = ""
            totsInsertResult = await ctx.send(content=f"```<토츠 입력 현황>\n"
                                                      f"FW - {t_totsFW}\n"
                                                      f"MF - {t_totsMF}\n"
                                                      f"DF - {t_totsDF}\n"
                                                      f"GK - {t_totsGK}\n\n"
                                                      f"<노미 입력 현황>\n"
                                                      f"FW - {t_nomiFW}\n"
                                                      f"MF - {t_nomiMF}\n"
                                                      f"DF - {t_nomiDF}\n"
                                                      f"GK - {t_nomiGK}```")
            ann_msg = await ctx.send(content=f"{tots} {position} 수상자 명단을 멘션으로 입력하세요.")
            i = 0
            while i < 8 :
                temp = divmod(i, 4)
                if temp[0] == 0 :
                    tots = "토츠"
                    if temp[1] == 0 :
                        position = "FW"
                    elif temp[1] == 1 :
                        position = "MF"
                    elif temp[1] == 2 :
                        position = "DF"
                    elif temp[1] == 3 :
                        position = "GK"
                elif temp[0] == 1 :
                    tots = "노미"
                    if temp[1] == 0 :
                        position = "FW"
                    elif temp[1] == 1 :
                        position = "MF"
                    elif temp[1] == 2 :
                        position = "DF"
                    elif temp[1] == 3 :
                        position = "GK"

                await totsInsertResult.edit(content=f"```<토츠 입력 현황>\n"
                                                    f"FW - {t_totsFW}\n"
                                                    f"MF - {t_totsMF}\n"
                                                    f"DF - {t_totsDF}\n"
                                                    f"GK - {t_totsGK}\n\n"
                                                    f"<노미 입력 현황>\n"
                                                    f"FW - {t_nomiFW}\n"
                                                    f"MF - {t_nomiMF}\n"
                                                    f"DF - {t_nomiDF}\n"
                                                    f"GK - {t_nomiGK}```")
                await ann_msg.edit(content=f"{tots} {position} 수상자 명단을 멘션으로 입력하세요.")
                try :
                    msg = await self.bot.wait_for("message",
                                                  check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=60.0)
                except asyncio.TimeoutError :
                    await ctx.send("시간이 초과되었습니다.\n"
                                   f"다시 명령어를 입력해주세요\n"
                                   f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
                    break
                else :
                    await ctx.channel.purge(limit=1)
                    member = msg.content.replace("<", "")
                    member = member.replace(">", "")
                    memberNum = member.replace("@", "")
                    tempList = memberNum.split(" ")
                    temp = []
                    for id in tempList :
                        member_obj = await self.bot.fetch_user(id)
                        totsList[i].append(member_obj)
                        if i == 0 :
                            t_totsFW = t_totsFW + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 1 :
                            t_totsMF = t_totsMF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 2 :
                            t_totsDF = t_totsDF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 3 :
                            t_totsGK = t_totsGK + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 4 :
                            t_nomiFW = t_nomiFW + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 5 :
                            t_nomiMF = t_nomiMF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 6 :
                            t_nomiDF = t_nomiDF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 7 :
                            t_nomiGK = t_nomiGK + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                    i += 1
            await totsInsertResult.delete()
            totsInsertResult2 = await ctx.send(content=f"``` <토츠 입력 최종 결과>\n"
                                                       f"FW - {t_totsFW}\n"
                                                       f"MF - {t_totsMF}\n"
                                                       f"DF - {t_totsDF}\n"
                                                       f"GK - {t_totsGK}\n\n"
                                                       f"<노미 입력 최종 결과>\n"
                                                       f"FW - {t_nomiFW}\n"
                                                       f"MF - {t_nomiMF}\n"
                                                       f"DF - {t_nomiDF}\n"
                                                       f"GK - {t_nomiGK}\n\n"
                                                       f"다음 단계로 진행하기를 희망하면 1을 입력하세요.```")
            try :
                msg = await self.bot.wait_for("message",
                                              check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                              timeout=60.0)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.\n"
                               f"다시 명령어를 입력해주세요\n"
                               f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
            else :
                if msg.content == "1" :
                    print(totsList)

                    for i in range(len(totsList)) :
                        print(i, totsList[i])
                        for mem in totsList[i] :
                            data = [mem.id, self.season, "", "", "", "", "", "", "", ""]
                            data[i + 2] = True
                            try :
                                conn = connectDB()
                                cur = conn.cursor()
                                cur.execute("INSERT INTO CAREER_TOTS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                            data)
                                # cur.execute("INSERT INTO CAREER_TOTS(ID, Season, FW_Tots, MF_Tots, DF_Tots, GK_Tots, "
                                #            "FW_Nomi, MF_Nomi, DF_Nomi, GK_Nomi) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?",
                                #            (data, ))
                            finally :
                                conn.commit()
                                conn.close()
                            await ctx.send(f"{mem.display_name} - DB 업데이트 완료", delete_after=10)
            await ctx.send("토츠 DB 업데이트 완료")
            await ctx.send(content=f"``` <{self.season} 토츠> \n"
                                   f"FW - {t_totsFW}\n"
                                   f"MF - {t_totsMF}\n"
                                   f"DF - {t_totsDF}\n"
                                   f"GK - {t_totsGK}\n\n"
                                   f"<{self.season} 노미>\n"
                                   f"FW - {t_nomiFW}\n"
                                   f"MF - {t_nomiMF}\n"
                                   f"DF - {t_nomiDF}\n"
                                   f"GK - {t_nomiGK}\n\n```")
        else :
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='발롱도르', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 하는 인원의 발롱도르 정보를 추가합니다.",
                      brief="$발롱도르 '@멘션'")
    async def _awardValondor(self, ctx, member: discord.Member = None) :
        # ID, Season
        role_names = [role.name for role in ctx.author.roles]
        print(self.season)
        if "스태프" in role_names :
            if self.season != "" :
                if member is not None :
                    msg = await ctx.send(f"```{self.season} 시즌의 수상자 : {member.display_name}```\n"
                                         f"정상 입력되었으면 1, 잘못 입력되었으면 2를 입력하세요.")
                    try :
                        msg2 = await self.bot.wait_for("message",
                                                       check=lambda
                                                           m : m.author == ctx.author and m.channel == ctx.channel,
                                                       timeout=30.0)
                    except asyncio.TimeoutError :
                        await ctx.send("시간이 초과되었습니다.")
                    else :
                        if msg2.content == "1" :
                            # DB 업데이트
                            try :
                                conn = connectDB()
                                cur = conn.cursor()
                                cur.execute("INSERT INTO CAREER_VALONDOR VALUES(?, ?)", (member.id, self.season))
                                await ctx.send(f"{member.display_name} DB 업데이트 완료")
                            finally :
                                closeDB(conn)

                        elif msg2.content == "2" :
                            await ctx.send("다시 명령어를 입력해주세요.")
                else :
                    await ctx.reply("```cs\n"
                                    "#명령어 실패!!!\n"
                                    "멤버 멘션이 누락되었습니다.\n"
                                    "사용법 : $발롱도르 '시즌' '@멘션'\n"
                                    "예시 - $발롱도르 24-1 @타임제이```")
            else :
                await ctx.reply("```cs\n"
                                "#명령어 실패!!!\n"
                                "시즌 정보가 누락되었습니다.\n"
                                "$시즌수정 명령어를 사용하여 시즌 정보를 업데이트 후 다시 시도해주세요.\n"
                                "사용법 : $발롱도르 '@멘션'\n"
                                "예시 - $발롱도르 @타임제이```")
        else :
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    '''@commands.command(name='리그순위입력', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 역할의 인원들의 정보(시즌, 순위)를 DB에 추가합니다.",
                      brief="$리그순위입력 '시즌' '순위' '@팀_멘션'")
    async def _insertLeageInfo(self, ctx, rank=None, selectRole:discord.Role=None):
        button = False
        resultList = []
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names:
            if self.season is not None:
                if rank is not None:
                    if selectRole is not None:
                        for member in selectRole.members:
                            switch = 1
                            idNum = member.id
                            teamName = selectRole.name
                            position = ''
                            for roleHasMember in [role.name for role in member.roles]:
                                if "감독" in roleHasMember:
                                    job = "감독"
                                    break
                                elif "Coach" in roleHasMember:
                                    job = "코치"
                                else:
                                    job = "선수"
                            msg1 = await ctx.send(f"{member.display_name} 님의 포지션을 입력해주세요.")
                            # 멤버별 포지션 입력 받기
                            while switch == 1:
                                try :
                                    msg = await self.bot.wait_for("message",
                                                                  check=lambda
                                                                      m : m.author == ctx.author and m.channel == ctx.channel,
                                                                  timeout=30.0)
                                except asyncio.TimeoutError :
                                    await ctx.send("시간이 초과되었습니다.")
                                else:
                                    position = msg.content.upper()
                                    if msg.content.upper() in config.positionList:
                                        resultList.append([idNum, self.season, teamName, job, position, rank])
                                        button = True
                                        switch = 2
                                    else:
                                        await ctx.send("```잘못 입력하였습니다.\n"
                                                       "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK\n"
                                                       "중 하나를 입력해주세요.```", delete_after=10)
                                        await msg1.edit(content=f"{member.display_name} 님의 포지션을 다시 입력해주세요.")
                            #await ctx.send(f"{member.display_name, idNum, season, teamName, job, position, rank}")
                    else :
                        await ctx.reply("```cs\n"
                                        "#명령어 실패!!!\n"
                                        "팀역할 정보가 누락되었습니다.\n"
                                        "사용법 : $리그순위입력 '시즌' '순위' '@팀_멘션'\n"
                                        "예시 - $리그순위입력 24-1 1 @FCB```")
                else:
                    await ctx.reply("```cs\n"
                                    "#명령어 실패!!!\n"
                                    "순위 정보가 누락되었습니다.\n"
                                    "사용법 : $리그순위입력 '시즌' '순위' '@팀_멘션'\n"
                                    "예시 - $리그순위입력 24-1 1 @FCB```")
            else:
                await ctx.reply("```cs\n"
                                "#명령어 실패!!!\n"
                                "시즌 정보가 누락되었습니다.\n"
                                "$시즌수정 명령어를 사용하여 시즌 정보를 업데이트 후 다시 시도해주세요.\n"
                                "사용법 : $리그순위입력 '순위' '@팀_멘션'\n"
                                "예시 - $리그순위입력 1 @FCB```")
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)
        print(resultList)
        if button:
            # 최종 정보 확인
            text = (f"시즌 : {self.season}\n"
                    f"순위 : {str(rank)} 위\n"
                    f"팀명 : {teamName}\n\n")
            for result in resultList:
                mem = ctx.message.guild.get_member(result[0])
                text = text + mem.display_name + " - " + str(result[4]) + "\n"
            msg = await ctx.send(f"```{text}```\n\n"
                                 f"정상 입력되었으면 1, 잘못 입력되었으면 2를 입력하세요.")
            try:
                msg3 = await self.bot.wait_for("message",
                                              check=lambda
                                                  m : m.author == ctx.author and m.channel == ctx.channel,
                                              timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
            else:
                await msg.delete()
                if msg3.content == "1":
                    # DB 정보 INSERT 하기
                    # ID, Season, Team, Job, Position, Rank
                    for result in resultList:
                        try :
                            conn = connectDB()
                            cur = conn.cursor()
                            cur.execute("INSERT INTO SEASON_USER_HISTORY VALUES(?, ?, ?, ?, ?, ?)", result)
                            mem = ctx.message.guild.get_member(result[0])
                            await ctx.send(f"{mem.display_name} DB 업데이트 완료", delete_after=10)
                        finally :
                            closeDB(conn)
                    await ctx.send(f"{selectRole.name} 팀의 시즌 순위 업데이트가 완료되었습니다.", delete_after=30)
                elif msg3.content == "2":
                    await ctx.send("처음부터 다시 시도해주세요.")'''

    @commands.command(name='리그정보입력', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 역할의 인원들의 정보(시즌, 순위)를 DB에 추가합니다.",
                      brief="$리그순위입력 '시즌' '순위' '@팀_멘션'")
    async def _insertLeagueInfo2(self, ctx) :

        teamSequence = []
        ann_msg = await ctx.send(f"```리그 순위를 입력합니다.\n"
                                 f"시즌 정보 : {self.season}\n"
                                 f"참가팀 수 : {self.teamCount}```")
        seasonInsertMessage = await ctx.send("시즌 정보를 입력해주세요.\n"
                                             "예시) 24-1, 24-2")
        try :
            msg1 = await self.bot.wait_for("message",
                                           check=lambda
                                               m : m.author == ctx.author and m.channel == ctx.channel,
                                           timeout=30.0)
        except asyncio.TimeoutError :
            await ctx.send("시간이 초과되었습니다.")
        else :
            self.season = msg1.content
            await seasonInsertMessage.delete()
            await ctx.message.channel.purge(limit=1)
            await ann_msg.edit(content=f"```리그 순위를 입력합니다.\n"
                                       f"시즌 정보 : {self.season}\n"
                                       f"참가팀 수 : {self.teamCount}```")
        seasonInsertMessage = await ctx.send(f"참가팀 수의 정보가 없습니다.\n"
                                             f"{self.season}의 참가 팀 수를 숫자로 입력해주세요.\n"
                                             f"예시) 11, 13, 15")
        try :
            msg2 = await self.bot.wait_for("message",
                                           check=lambda
                                               m : m.author == ctx.author and m.channel == ctx.channel,
                                           timeout=30.0)
        except asyncio.TimeoutError :
            await ctx.send("시간이 초과되었습니다.")
        else :
            self.teamCount = int(msg2.content)
            await seasonInsertMessage.delete()
            await ctx.message.channel.purge(limit=1)
            await ann_msg.edit(content=f"```리그 순위를 입력합니다.\n"
                                       f"시즌 정보 : {self.season}\n"
                                       f"참가팀 수 : {self.teamCount}```")
        temp_txt = ''
        insertTeamName = await ctx.send(f"1위 팀의 약자를 입력하세요.")
        for i in range(self.teamCount) :
            rank = i + 1
            await insertTeamName.edit(content=f"{str(rank)}위 팀의 약자를 입력하세요.")
            try :
                msg3 = await self.bot.wait_for("message",
                                               check=lambda
                                                   m : m.author == ctx.author and m.channel == ctx.channel,
                                               timeout=30.0)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.")
            else :
                self.teamSequence.append(msg3.content.upper())
                temp_txt = temp_txt + str(i + 1) + " - " + msg3.content.upper() + "\n"
                await ann_msg.edit(content=f"```리그 순위를 입력합니다.\n"
                                           f"시즌 정보 : {self.season}\n"
                                           f"참가팀 수 : {self.teamCount}```\n"
                                           f"```<순위별 팀 정보 입력 현황>\n"
                                           f"{temp_txt}```")
                print(self.teamSequence)

    @commands.command(name='리그순위입력', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 역할의 인원들의 정보(시즌, 순위)를 DB에 추가합니다.",
                      brief="$리그순위입력 '팀약자' '@유저멘션 '포지션' ")
    async def _insertLeagueInfo(self, ctx, team, member: discord.Member, position) :
        if position.upper() in config.positionList :
            if checkFun.checkStaff(ctx) :
                if self.season2 != "" :
                    rank = 0
                    myTeam = team.upper()
                    myPosition = position.upper()
                    myJob = getRankFromUserInfoWithID(member.id)
                    for i, team in enumerate(self.teamSequence2) :
                        if myTeam == team :
                            rank = i + 1
                            break
                    try :
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("INSERT INTO SEASON_USER_HISTORY VALUES(?, ?, ?, ?, ?, ?)",
                                    (member.id, self.season2, myTeam, myJob, myPosition, rank))
                    finally :
                        conn.commit()
                        conn.close()
                        await ctx.reply(f"```{getNicknameFromUserInfoWithID(member.id)} - 시즌 정보 업데이트 완료\n"
                                        f"입력된 정보는 $내정보 명령어를 통해 확인 가능합니다.```")
                else :
                    await ctx.reply("$리그정보입력 명령어를 먼저 사용해서 정보를 등록한 후 다시 시도해주세요.")
            else :
                await ctx.send("스태프 전용")
        else :
            await ctx.reply("포지션을 잘못 입력하였습니다.")

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"스태프전용_커리어 : {error}")
async def setup(bot) :
    await bot.add_cog(스태프전용_커리어(bot))
