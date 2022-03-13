import discord
from datetime import datetime, timedelta
import sqlite3
import checkFun
from myfun import *
from discord.ext import commands
from discord.utils import get
import string
import config


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
            if checkFun.checkEnglish(ctx):                       # 닉네임 한글 검사
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
                                print('신규가입 성공')
                                await ctx.send(content=f"신규가입 성공")
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
                                await ctx.send(content=f"재가입 성공")
                                conn.commit()
                            finally :
                                conn.close()
                            # 역할 부여
                            user = ctx.author
                            role = get(ctx.guild.roles, name='테스트용')
                            await user.add_roles(role)
                    else:
                        print("닉네임 중복 검사 - 중복")
                        await ctx.send("```해당 닉네임은 이미 다른 유저가 사용 중입니다.\n"
                                       "다른 닉네임으로 수정 후 다시 시도해주세요.```")
                else:
                    print("닉네임 양식 검사 - 일치하지 않음")
                    await ctx.send("```닉네임 양식이 일치하지 않습니다.\n"
                                   "닉네임[주포지션/부포지션] or 닉네임[주포지션] 으로 수정 후 다시 시도해주세요.```")
            else:
                print("영어 아님")
                await ctx.send("```현 규정상 한글 닉네임은 스태프만 사용이 가능합니다.\n"
                               "영문으로 수정 후 다시 시도해주세요.```")
        else:
            print("이미 가입됨")
            await ctx.send("```이미 가입되었습니다.```")
        '''# 닉네임 양식 검사
        if checkFun.checkNicknameForm(ctx):
            #print("양식 검사", checkFun.checkNicknameForm(ctx))
            await ctx.send(content=f"닉네임 양식 검사 - 정상")
            # 닉네임 중복 여부 검사
            if not checkFun.checkNicknameOverlap(ctx):
                #print("중복 검사", checkFun.checkNicknameOverlap(ctx))
                await ctx.send(content=f"닉네임 중복 검사 - 정상")
                # 역할 갖고 있는 지 검사
                ownRoles = [role.name for role in ctx.author.roles]
                if not self.ROLE_NAME in ownRoles:
                    # 신규, 재가입 여부 검사
                    if not checkFun.checkRejoin(ctx):  # 신규 일경우
                        #print("재가입 여부 검사", checkFun.checkRejoin(ctx))
                        await ctx.send(content=f"재가입 여부 검사 - 신규")
                        # 신규 유저 User_Info 정보 입력
                        id = ctx.author.id
                        join_date = int(str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) +\
                                        str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second))
                        nickname = getNickFromDisplayname(ctx)
                        jupo = getJupoFromDisplayname(ctx)
                        bupo = getBupoFromDisplayname(ctx)
                        team = "무소속"
                        Exteam = "없음"
                        absent = ""
                        # DB 작업
                        try:
                            conn = sqlite3.connect("CEF.db")
                            cur = conn.cursor()
                            cur.execute("INSERT INTO User_Info VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id, join_date, nickname, jupo, bupo, team, Exteam, absent))
                            print('신규가입 성공')
                            await ctx.send(content=f"신규가입 성공")
                            conn.commit()
                        finally:
                            conn.close()
                        # 역할 부여
                        user = ctx.author
                        role = get(ctx.guild.roles, name='테스트용')
                        await user.add_roles(role)
                    else:  # 기존 유저 재가입 일경우
                        #print("재가입 여부 검사", checkFun.checkRejoin(ctx))
                        await ctx.send(content=f"재가입 여부 검사 - 재가입")
                        # 재가입 유저 User_Info 정보 입력
                        id = ctx.author.id
                        join_date = int(str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + \
                                        str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second))
                        nickname = getNickFromDisplayname(ctx)
                        jupo = getJupoFromDisplayname(ctx)
                        bupo = getBupoFromDisplayname(ctx)
                        team = "무소속"
                        Exteam = "없음"
                        absent = ""
                        # DB 작업
                        try:
                            conn = sqlite3.connect("CEF.db")
                            cur = conn.cursor()
                            cur.execute("UPDATE User_Info SET nickname=? WHERE id=?", (getNickFromDisplayname(ctx), ctx.author.id))
                            #print('재가입 성공')
                            await ctx.send(content=f"재가입 성공")
                            conn.commit()
                        finally:
                            conn.close()
                        # 역할 부여
                        user = ctx.author
                        role = get(ctx.guild.roles, name='테스트용')
                        await user.add_roles(role)
                else:
                    await ctx.send("```이미 가입되었습니다.```")
            else:  # 닉네임 중복일 경우
                await ctx.send(content=f"```{getNickFromDisplayname(ctx)} 해당 닉네임은 이미 기존 유저가 사용 중입니다.```")
        else:
            await ctx.send(content=f"```잘못된 닉네임 양식입니다.\n"
                                   f"닉네임 양식 : 닉네임[주포지션] or 닉네임[주포지션/부포지션]\n"
                                   f"예시 : Test[CB] or TEST[CB/RB]```")'''




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

    @commands.command(name='리셋', pass_context=True, aliases=['reset', 'Reset'])
    async def _reset(self, ctx):
        try :
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM User_Info")
            for row in cur.fetchall() :
                print(row[2])
        finally :
            conn.close()

    @commands.command(name='삭제', pass_context=True)
    async def _search(self, ctx):
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM User_Info WHERE id=?", (ctx.author.id,))
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



    @commands.command(name='테스', pass_context=True)
    async def _tes(self, ctx):
        print(checkFun.checkNicknameOverlap(ctx))
        if checkFun.checkNicknameOverlap(ctx):
            await ctx.send(content=f"{getNickFromDisplayname(ctx)}님은 등록되어 있습니다.")
        else:
            await ctx.send(content=f"{getNickFromDisplayname(ctx)}님은 미등록 상태입니다.")
        '''try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            param1 = (getNickFromDisplayname(ctx),)
            cur.execute("SELECT * FROM User_Info WHERE nickname=?", param1)
            print(cur.fetchall())
            print("1--------")
            cur = conn.cursor()
            cur.execute("SELECT * FROM User_Info")
            for row in cur.fetchall():
                print(row)
                if getNickFromDisplayname(ctx) == row[2]:
                    print("a")
                    break
                else:
                    print("b")
        finally:
            conn.close()'''


def setup(bot):
    bot.add_cog(Member(bot))