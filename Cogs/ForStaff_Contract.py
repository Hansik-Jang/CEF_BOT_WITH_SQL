import discord
from discord.ext import commands
from discord.utils import get
import checkFun
from forAccessDB import *
import config
import asyncio
import myfun
from datetime import datetime, timedelta
from table2ascii import table2ascii as t2a, PresetStyle

class 스태프전용_계약(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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


    @commands.command(name='계약입력', pass_context=True,
                      aliases=[],
                      help="권한 : 스태프\n"
                           "멘션한 인원의 계약 정보를 DB에 추가합니다.\n\n"
                           "사용시 주의사항 : \n"
                           "1. 계약정보가 기존에 입력이 되있지않아야 입력이 가능합니다.\n"
                           "2. 계약기간은 숫자만 입력해도 되지만 계약시작일은 '/'를 사용해 연도, 월, 일을 구분해줘야 합니다.\n"
                           "연도 미입력 시 자동으로 입력 날짜를 기준으로 연도를 계산하여 작동합니다.\n"
                           "사용 예시 : $계약입력 @타임제이 23/10/29 30 $계약입력 @타임제이 10/29 30",
                      brief="$계약입력 @멘션 '계약시작일' '기간'")
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


    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"스태프전용_계약 : {error}")
async def setup(bot) :
    await bot.add_cog(스태프전용_계약(bot))