import discord
from datetime import datetime, timedelta
import sqlite3
import checkFun
import asyncio
from myfun import *
from discord.ext import commands
from discord.utils import get
import string
import config
global DEVELOPER_SWITCH

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx):
        ctxRoles = [role.name for role in ctx.author.roles]
        print(ctxRoles)
        if config.BASE_ROLE_NAME not in ctxRoles:                # 중복 가입 여부 검사
            print("중복 가입 검사 - 정상")
            print("닉네임 검사 결과 : ")
            print(checkFun.checkEnglish(ctx))
            if checkFun.checkEnglish(ctx) or '스태프' in ctxRoles:                       # 닉네임 한글 검사
                print("닉네임 한글 검사 - 정상")
                if checkFun.checkNicknameForm(ctx):              # 닉네임 양식 검사
                    print("닉네임 양식 검사 - 정상")
                    if checkFun.checkNicknameOverlap(ctx):       # 닉네임 중복 검사
                        print("닉네임 중복 검사 - 정상")
                        if checkFun.checkRejoin(ctx):            # 재가입 여부 검사
                            # 신규가입
                            # 신규 유저 User_Info 정보 입력
                            id = ctx.author.id
                            join_date = int(
                                str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + \
                                str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second))
                            nickname = getNickFromDisplayname(ctx)
                            jupo = getJupoFromDisplayname(ctx)
                            bupo = getBupoFromDisplayname(ctx)
                            team = "무소속"
                            Exteam = "없음"
                            absent = ""
                            # DB 작업
                            try :
                                conn = sqlite3.connect("CEF.db")
                                cur = conn.cursor()
                                cur.execute("INSERT INTO User_Info VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                                            (id, join_date, nickname, jupo, bupo, team, Exteam, absent))
                                cur.execute("INSERT INTO Career VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                            (id, 0, 0, 0, 0, 0, 0, 0, 0))
                                cur.execute("INSERT INTO Judge VALUES(?, ?, ?, ?)",
                                            (id, 0, 0, 0))
                                print('신규가입 성공')
                                await ctx.reply(content=f"신규가입 성공")
                                conn.commit()
                            finally :
                                conn.close()
                            # 역할 부여
                            user = ctx.author
                            role = get(ctx.guild.roles, name='테스트용')
                            await user.add_roles(role)
                        else:
                            # 재가입
                            # print("재가입 여부 검사", checkFun.checkRejoin(ctx))
                            await ctx.send(content=f"재가입 여부 검사 - 재가입")
                            # 재가입 유저 User_Info 정보 입력
                            id = ctx.author.id
                            join_date = int(
                                str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + \
                                str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second))
                            nickname = getNickFromDisplayname(ctx)
                            jupo = getJupoFromDisplayname(ctx)
                            bupo = getBupoFromDisplayname(ctx)
                            team = "무소속"
                            Exteam = "없음"
                            absent = ""
                            # DB 작업
                            try :
                                conn = sqlite3.connect("CEF.db")
                                cur = conn.cursor()
                                cur.execute("UPDATE User_Info SET nickname=? WHERE id=?",
                                            (getNickFromDisplayname(ctx), ctx.author.id))
                                # print('재가입 성공')
                                await ctx.reply(content=f"재가입 성공")
                                conn.commit()
                            finally :
                                conn.close()
                            # 역할 부여
                            user = ctx.author
                            role = get(ctx.guild.roles, name='테스트용')
                            await user.add_roles(role)
                    else:
                        print("닉네임 중복 검사 - 중복")
                        await ctx.reply("```해당 닉네임은 이미 다른 유저가 사용 중입니다.\n"
                                       "다른 닉네임으로 수정 후 다시 시도해주세요.```")
                else:
                    print("닉네임 양식 검사 - 일치하지 않음")
                    await ctx.reply("```닉네임 양식이 일치하지 않습니다.\n"
                                   "닉네임[주포지션/부포지션] or 닉네임[주포지션] 으로 수정 후 다시 시도해주세요.```")
            else:
                print("영어 아님")
                await ctx.reply("```현 규정상 한글 닉네임은 스태프만 사용이 가능합니다.\n"
                               "영문으로 수정 후 다시 시도해주세요.```")
        else:
            print("이미 가입됨")
            await ctx.reply("```이미 가입되었습니다.```")


    @commands.command(name='탈퇴', pass_context=True, aliases=['Withdrawal', 'withdrawal'])
    async def _withdrawal(self, ctx):
        # 모든 역할 제거
        roleli = []
        role_names = ["CEF", "신규", '감독', "TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D", "TEAM_E", "A Coach", "B Coach", "C Coach",
                      "D Coach", "E Coach"]
        for rolename in role_names:
            roleli.append(get(ctx.guild.roles, name=rolename))
        for role in roleli:
            await ctx.author.remove_roles(role)
        # DB 작업
        try:
            conn = sqlite3.connect("CEF.db")
            # 탈퇴 전 정보 백업
            cur = conn.cursor()
            conn.commit()
        finally:
            conn.close()

    @commands.command(name='포지션변경', pass_context=True, aliases=['reset', 'Reset'])
    async def _changeJupo(self, ctx):

        if DEVELOPER_SWITCH and ctx.author.id in config.DEVELOPER_LIST:
            jupo = ''
            bupo = ''
            checkJupo = True
            checkBupo = True
            await ctx.send(content=f"{ctx.author.mention}\n"
                                   f"```주포지션 정보를 변경합니다.\n"
                                   f"주포지션을 선택해주세요\n"
                                   "1. ST\n"
                                   "2. LW\n"
                                   "3. RW\n"
                                   "4. CAM\n"
                                   "5. CM\n"
                                   "6. CDM\n"
                                   "7. LB\n"
                                   "8. CB\n"
                                   "9. RB\n"
                                   "10. GK\n```")
            try:
                msg = await self.bot.wait_for("message", check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                             timeout=10.0)
            except asyncio.TimeoutError:
                checkJupo = False
                await ctx.channel.send("시간 초과")
            else:
                if msg.content.lower() == '1' :
                    jupo = 'ST'
                elif msg.content.lower() == '2' :
                    jupo = 'LW'
                elif msg.content.lower() == '3' :
                    jupo = 'RW'
                elif msg.content.lower() == '4' :
                    jupo = 'CAM'
                elif msg.content.lower() == '5' :
                    jupo = 'CM'
                elif msg.content.lower() == '6' :
                    jupo = 'CDM'
                elif msg.content.lower() == '7' :
                    jupo = 'LB'
                elif msg.content.lower() == '8' :
                    jupo = 'CB'
                elif msg.content.lower() == '9' :
                    jupo = 'RB'
                elif msg.content.lower() == '10' :
                    jupo = 'GK'
            if checkJupo:
                await msg.reply(content=f"```입력하신 주포지션은 '{jupo}'입니다.\n"
                                        f"부포지션을 선택해주세요.\n"
                                        "1. ST\n"
                                        "2. LW\n"
                                        "3. RW\n"
                                        "4. CAM\n"
                                        "5. CM\n"
                                        "6. CDM\n"
                                        "7. LB\n"
                                        "8. CB\n"
                                        "9. RB\n"
                                        "10. GK\n"
                                        "11. 없음```")
                try:
                    msg2 = await self.bot.wait_for("message",
                                                  check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=10.0)
                except asyncio.TimeoutError:
                    checkBupo = False
                    await ctx.channel.send("시간 초과")
                else :
                    if msg2.content.lower() == '1':
                        bupo = 'ST'
                    elif msg2.content.lower() == '2':
                        bupo = 'LW'
                    elif msg2.content.lower() == '3':
                        bupo = 'RW'
                    elif msg2.content.lower() == '4':
                        bupo = 'CAM'
                    elif msg2.content.lower() == '5':
                        bupo = 'CM'
                    elif msg2.content.lower() == '6':
                        bupo = 'CDM'
                    elif msg2.content.lower() == '7':
                        bupo = 'LB'
                    elif msg2.content.lower() == '8':
                        bupo = 'CB'
                    elif msg2.content.lower() == '9':
                        bupo = 'RB'
                    elif msg2.content.lower() == '10':
                        bupo = 'GK'
                    elif msg2.content.lower() == '11':
                        bupo = '없음'
            else:
                await ctx.send(content=f"{ctx.author.mention}\n"
                                       f"처음부터 다시 시도해주세요.")
            if checkBupo:
                if jupo == bupo:
                    await ctx.send(content=f"{ctx.author.mention}\n"
                                           f"입력한 주포지션과 부포지션이 같습니다.\n"
                                           f"처음부터 다시 시도해주세요")
                else:
                    if bupo == '없음':
                        nick = getNickFromDisplayname(ctx) + "[" + jupo + "]" + getImojiFromDisplayname(ctx)
                    else:
                        nick = getNickFromDisplayname(ctx) + "[" + jupo + "/" + bupo + "]" + getImojiFromDisplayname(ctx)
                    user = ctx.author
                    await user.edit(nick=nick)


            else :
                await ctx.send(content=f"{ctx.author.mention}\n"
                                       f"처음부터 다시 시도해주세요.")
        else:
            await ctx.send("현재 개발자모드로 개발자만 사용가능합니다.")

    @commands.command(name='데이터삭제', pass_context=True)
    async def _deleteData(self, ctx):
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM User_Info WHERE id=?", (ctx.author.id,))
            cur.execute("DELETE FROM Career WHERE id=?", (ctx.author.id,))
            cur.execute("DELETE FROM Judge WHERE id=?", (ctx.author.id,))
            conn.commit()
        finally:
            conn.close()
        user = ctx.author
        role = get(ctx.guild.roles, name='테스트용')
        await user.remove_roles(role)

    @commands.command(name='테', pass_context=True, aliases=['te'])
    async def _test(self, ctx):
        nick_ovl = True
        id_ovl = True
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM User_Info")
            #cur.execute("SELECT * FROM User_Info WHERE id=?", (ctx.author.id, ))
            data = cur.fetchall()
            print(data)
            #await ctx.send(content=f"{data}")
            print(len(data))
            print(data[0][0])
            print(data[1][0])
            print(data[0][1])

            # 전체 리스트에 있는지 체크
            for i in range(len(data)):
                if ctx.author.id == data[i][0]:     # 리스트 안에 있음 (재가입자)
                    await ctx.send("등록 되어있음")
                    break
                else:                               # 리스트 안에 없음 (신규가입)
                    await ctx.send("미등록자")
            #if data[0][1]
            #    await ctx.send("이력 없음")
            #else:
            #    await ctx.send(content=f"{cur.fetchone()}")
        finally:
            conn.close()

    @commands.command(name='제거', pass_context=True)
    async def _delete(self, ctx):
        roleli = []
        role_names = ["테스트용"]
        for rolename in role_names:
            roleli.append(get(ctx.guild.roles, name=rolename))
        for role in roleli:
            for member in role.members:
                await member.remove_roles(role)
                await ctx.send(content=f"{member.display_name} - {role} 제거")      # 메시지 닉네임 출력
                #await ctx.send(content=f"{member.mention} - {role} 제거")            메시지 멘션 출력


    @commands.command(name='테스', pass_context=True)
    async def _tes(self, ctx):
        await ctx.reply("테스트")

def setup(bot):
    bot.add_cog(Member(bot))