import discord
from discord.ext import commands
from discord.utils import get
import gspread
import sqlite3
from forAccessDB import *
import config
import asyncio
import myfun
from table2ascii import table2ascii as t2a, PresetStyle


class Career(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.season = "24-1"

    @commands.command(name='내정보', pass_context=True)
    async def _myinformation(self, ctx):
        if checkUseJoinCommand(ctx):

            role_names = [role.name for role in ctx.author.roles]
            history = getHystoryFromSeasonUserHistory(ctx)
            imoji = getImojiFromTeamInfor(getTeamNameFromUserInfo(ctx))
            logo = getLogoFromTeamInfor(getTeamNameFromUserInfo(ctx))
            embed = discord.Embed(title=getNicknameFromUserInfo(ctx),
                                  description=ctx.author.id,
                                  colour=getStringColorCodeFromTeamInfor(getTeamNameFromUserInfo(ctx)))
            embed.add_field(name="소속", value=f"{getTeamNameFromUserInfo(ctx)} {imoji}", inline=True)
            embed.add_field(name="신분", value=getRankFromUserInfo(ctx), inline=True)
            embed.add_field(name="닉네임 변경권", value=getNickChangeCouponFromUserInfo(ctx), inline=True)
            embed.add_field(name="주포지션", value=getMainPositionFromUserInfo(ctx), inline=True)
            embed.add_field(name="부포지션", value=getSubPositionFromUserInfo(ctx), inline=True)
            if "감독" in role_names:
                embed.add_field(name="계약기간", value="감독 직책으로 미표기", inline=False)
            elif "FA (무소속)" in role_names:
                embed.add_field(name="계약기간", value="FA 신분으로 미표기", inline=False)
            elif getStartDateFromContract(ctx) == '' or getEndDateFromContract(ctx) == '' or getPeriodFromContract(ctx) == '':
                embed.add_field(name="계약기간", value="계약 정보 없음", inline=False)
            else:
                text = (getStartDateFromContract(ctx) + " ~ " + getEndDateFromContract(ctx)
                        + " (총 " + str(getPeriodFromContract(ctx)) + " 일)")
                embed.add_field(name="계약기간", value=text, inline=False)
            career = getTotsFromCareerWithID(ctx.author.id)
            val = getValFromCareerValondorWithID(ctx.author.id)
            text = career + val
            if history == "":
                embed.add_field(name="히스토리", value="기록 없음", inline=False)
            else:
                embed.add_field(name="히스토리", value=history, inline=False)
            if text == "":
                embed.add_field(name="커리어", value="기록 없음", inline=False)
            else:
                embed.add_field(name="커리어", value=text, inline=False)
            embed.set_thumbnail(url=ctx.author.display_avatar.url)


            embed2_msg = await ctx.reply(embed=embed)

        else:
            await ctx.reply(config.notJoinText)


    @commands.command(name='토츠', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 하는 인원의 발롱도르 정보를 추가합니다.",
                      brief="$토츠 '시즌' '@멘션'")
    async def _awardTots(self, ctx):
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
            while i < 8:
                temp = divmod(i, 4)
                if temp[0] == 0:
                    tots = "토츠"
                    if temp[1] == 0 :
                        position = "FW"
                    elif temp[1] == 1 :
                        position = "MF"
                    elif temp[1] == 2 :
                        position = "DF"
                    elif temp[1] == 3 :
                        position = "GK"
                elif temp[0] == 1:
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
                        if i == 0:
                            t_totsFW = t_totsFW + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 1:
                            t_totsMF = t_totsMF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 2:
                            t_totsDF = t_totsDF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 3:
                            t_totsGK = t_totsGK + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 4:
                            t_nomiFW = t_nomiFW + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 5:
                            t_nomiMF = t_nomiMF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 6:
                            t_nomiDF = t_nomiDF + myfun.getNickFromDisplayname2(member_obj.display_name) + ", "
                        elif i == 7:
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
            else:
                if msg.content == "1":
                    print(totsList)

                    for i in range(len(totsList)):
                        print(i, totsList[i])
                        for mem in totsList[i]:
                            data = [mem.id, self.season, "", "", "", "", "", "", "", ""]
                            data[i+2] = True
                            try :
                                conn = connectDB()
                                cur = conn.cursor()
                                cur.execute("INSERT INTO CAREER_TOTS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                            data)
                                #cur.execute("INSERT INTO CAREER_TOTS(ID, Season, FW_Tots, MF_Tots, DF_Tots, GK_Tots, "
                                #            "FW_Nomi, MF_Nomi, DF_Nomi, GK_Nomi) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?",
                                #            (data, ))
                            finally:
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
    async def _awardValondor(self, ctx, member:discord.Member=None):
        # ID, Season
        role_names = [role.name for role in ctx.author.roles]
        print(self.season)
        if "스태프" in role_names :
            if self.season is not None:
                if member is not None:
                    msg = await ctx.send(f"```{self.season} 시즌의 수상자 : {member.display_name}```\n"
                                         f"정상 입력되었으면 1, 잘못 입력되었으면 2를 입력하세요.")
                    try :
                        msg2 = await self.bot.wait_for("message",
                                                       check=lambda
                                                           m : m.author == ctx.author and m.channel == ctx.channel,
                                                       timeout=30.0)
                    except asyncio.TimeoutError :
                        await ctx.send("시간이 초과되었습니다.")
                    else:
                        if msg2.content == "1":
                            # DB 업데이트
                            try :
                                conn = connectDB()
                                cur = conn.cursor()
                                cur.execute("INSERT INTO CAREER_VALONDOR VALUES(?, ?)", (member.id, self.season))
                                await ctx.send(f"{member.display_name} DB 업데이트 완료")
                            finally :
                                closeDB(conn)

                        elif msg2.content == "2":
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
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='리그순위입력', pass_context=True,
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
                    await ctx.send("처음부터 다시 시도해주세요.")

    @commands.command(name='시즌정보수정', pass_context=True,
                      help="권한 : 스태프\n"
                           "현재 봇에 내장된 시즌 정보를 변경합니다.",
                      brief="$시즌정보수정 '시즌'")
    async def _editSeason(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            msg = await ctx.send(f"예시와 같은 형태로 시즌 정보를 입력해주세요.\n"
                                 f"예시) 24-1, 24-2, 24-3")
            switch = True
            while True:
                try :
                    msg1 = await self.bot.wait_for("message",
                                                  check=lambda
                                                      m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=30.0)
                except asyncio.TimeoutError :
                    await ctx.send("시간이 초과되었습니다.")
                else :
                    msg2 = await ctx.send(f"기존 정보 : {self.season}"
                                          f"입력한 시즌 : {msg1.content}\n"
                                          f"입력한 시즌으로 업데이트하려면 1, 다시 입력하려면 2를 입력하세요.")
                    try:
                        msg3 = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=30.0)
                    except asyncio.TimeoutError :
                        await ctx.send("시간이 초과되었습니다.")
                    else:
                        if msg3.content == "1":
                            self.season = msg1.content
                            await ctx.send(f"{self.season}으로 업데이트되었습니다.", delete_after=10)
                            break
                        elif msg3.content == "2":
                            await ctx.send("예시와 같은 형태로 시즌 정보를 다시 입력해주세요.\n"
                                           f"예시) 24-1, 24-2, 24-3")
                        else:
                            await ctx.send("잘못 입력하였습니다.", delete_after=10)

        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='시즌정보보기', pass_context=True,
                      help="권한 : 스태프\n"
                           "현재 봇에 내장된 시즌 정보를 출력합니다.",
                      brief="$시즌수정 '시즌'")
    async def _showSeason(self, ctx) :
        await ctx.send(f"현재 봇에 저장된 시즌 정보는 {self.season}입니다.")

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"An error occurred in the career cog: {error}")

async def setup(bot):
    await bot.add_cog(Career(bot))
