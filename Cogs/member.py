import discord
from datetime import datetime, timedelta
import sqlite3
import checkFun
from myfun import *
from discord.ext import commands
from discord.utils import get
import string


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx):
        # 닉네임 양식 검사
        if checkFun.checkNicknameForm(ctx):
            print("양식 검사", checkFun.checkNicknameForm(ctx))
            # 닉네임 중복 여부 검사
            if not checkFun.checkNicknameOverlap(ctx):
                print("중복 검사", checkFun.checkNicknameOverlap(ctx))
                # 신규, 재가입 여부 검사
                if not checkFun.checkRejoin(ctx):
                    print("재가입 검사", checkFun.checkRejoin(ctx))
                #-------------------- User_Info 테이블 입력 --------------------
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
                    print('a')
                    conn.commit()
                finally:
                    conn.close()

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
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
        finally:
            conn.close()


    @commands.command(name='검색', pass_context=True)
    async def _search(self, ctx, *, name):
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
        finally:
            conn.close()

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