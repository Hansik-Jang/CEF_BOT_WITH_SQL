import discord
from discord.ext import commands
import gspread
import sqlite3
from forAccessDB import *
import config
import asyncio
import myfun


class Career(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='내정보', pass_context=True)
    async def _myinformation(self, ctx):
        if checkUseJoinCommand(ctx):

            role_names = [role.name for role in ctx.author.roles]
            history = getHystoryFromSeasonUserHistory(ctx)
            imoji = getImojiFromTeamInfor(getTeamNameFromUserInfo(ctx))
            logo = getLogoFromTeamInfor(getTeamNameFromUserInfo(ctx))
            embed = discord.Embed(title=getNicknameFromUserInfo(ctx),
                                  description=ctx.author.id)
            embed.add_field(name="소속", value=getTeamNameFromUserInfo(ctx), inline=True)
            embed.add_field(name="신분", value=getRankFromUserInfo(ctx), inline=True)
            embed.add_field(name="닉네임 변경권", value=getNickChangeCouponFromUserInfo(ctx), inline=True)
            embed.add_field(name="주포지션", value=getMainPositionFromUserInfo(ctx), inline=True)
            embed.add_field(name="부포지션", value=getSubPositionFromUserInfo(ctx), inline=True)
            if "감독" in role_names:
                embed.add_field(name="계약기간", value="감독 직책으로 미표기", inline=False)
            elif "FA (무소속)" in role_names:
                embed.add_field(name="계약기간", value="FA 신분으로 미표기", inline=False)
            elif (getStartDateFromContract(ctx) is not None and getEndDateFromContract(ctx) is not None
                  and getPeriodFromContract(ctx) is None):
                embed.add_field(name="계약기간", value="계약 정보 없음", inline=False)
            else:
                text = (getStartDateFromContract(ctx) + " ~ " + getEndDateFromContract(ctx)
                        + " (총 " + str(getPeriodFromContract(ctx)) + " 일)")
                embed.add_field(name="계약기간", value=text, inline=False)
            career = getTotsFromCareerWithID(ctx.author.id)
            val = getValFromCareerValondorWithID(ctx.author.id)
            text = career + val
            if text == "":
                embed.add_field(name="커리어", value="기록 없음", inline=False)
            else:
                embed.add_field(name="커리어", value=text, inline=False)
            if history == "":
                embed.add_field(name="히스토리", value="기록 없음", inline=False)
            else:
                embed.add_field(name="히스토리", value=history, inline=False)
            if logo != "":
                embed.set_thumbnail(url=logo)


            embed2_msg = await ctx.send(embed=embed)

        else:
            await ctx.reply(config.notJoinText)


    @commands.command(name='토츠', pass_context=True)
    async def _awardTots(self, ctx):
        # ID, Season, FW_Tots, FW_Nomi, MF_Tots, MF_Nomi, DF_Tots, DF_Nomi, GK_Tots, GK_Nomi
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='발롱도르', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 하는 인원의 발롱도르 정보를 추가합니다.",
                      brief="$발롱도르 '시즌' '@멘션'")
    async def _awardValondor(self, ctx, season=None):
        # ID, Season
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            if season is not None:
                print(1)
            else:
                print("z")
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='리그순위입력', pass_context=True,
                      help="권한 : 스태프\n"
                           "해당 역할의 인원들의 정보(시즌, 순위)를 DB에 추가합니다.",
                      brief="$발롱도르 '시즌' '순위' '@팀_멘션'")
    async def _awardValondor(self, ctx, season=None, rank=None, selectRole:discord.Role=None):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names:
            if season is not None:
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
                                        switch = 2
                                    else:
                                        await ctx.send("```잘못 입력하였습니다.\n"
                                                       "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK\n"
                                                       "중 하나를 입력해주세요.```", delete_after=10)
                                        await msg1.edit(content=f"{member.display_name} 님의 포지션을 다시 입력해주세요.")
                            #await ctx.send(f"{member.display_name, idNum, season, teamName, job, position, rank}")
                            # DB 정보 INSERT 하기
                            # ID, Season, Team, Job, Position, Rank
                            try:
                                conn = connectDB()
                                cur = conn.cursor()
                                cur.execute("INSERT INTO SEASON_USER_HISTORY VALUES(?, ?, ?, ?, ?, ?)",
                                            (idNum, season, teamName, job, position, rank))
                                await ctx.send(f"{member.display_name} DB 업데이트 완료")
                            finally:
                                closeDB(conn)
                    else :
                        await ctx.send("```cs\n"
                                       "#명령어 실패!!!\n"
                                       "팀역할 정보가 누락되었습니다.\n"
                                       "사용법 : $리그순위입력 '시즌' '순위' '@팀_멘션'\n"
                                       "예시 - $리그순위입력 24-1 1 @FCB```")
                else:
                    await ctx.send("```cs\n"
                                   "#명령어 실패!!!\n"
                                   "순위 정보가 누락되었습니다.\n"
                                   "사용법 : $리그순위입력 '시즌' '순위' '@팀_멘션'\n"
                                   "예시 - $리그순위입력 24-1 1 @FCB```")
            else:
                await ctx.send("```cs\n"
                               "#명령어 실패!!!\n"
                               "순위 정보가 누락되었습니다.\n"
                               "사용법 : $리그순위입력 '시즌' '순위' '@팀_멘션'\n"
                               "예시 - $리그순위입력 24-1 1 @FCB```")
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

async def setup(bot):
    await bot.add_cog(Career(bot))
