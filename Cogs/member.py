import discord
import datetime
import sqlite3
import myfun
from myfun import *
from discord.ext import commands
from discord.utils import get
import string


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx):
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        nickname = getNickFromDisplayname(ctx)
        sql = 'CREATE TABLE ' + 'Info_' + eraseBlackNick(nickname)\
                                         + '(ID_Num INTEGER, Join_Date text, Out_Date text, State text, ' \
                                           'Jupo text, Bupo text, Team text, Contract text, ' \
                                           'Absence_Date str, Price INTEGER, Cur_Wallet INTEGER,' \
                                           'Pre_Wallet INTEGER, Win_Head INTEGER, Win_Coach INTEGER,' \
                                           'Win_Player INTEGER, Tots_FW INTEGER, Tots_MF INTEGER,'\
                                           'Tots_DF INTEGER, Tots_GK INTEGER, Pots INTEGER)'
        cur.execute(sql)
        print('a')
        conn.commit()
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


    @commands.command(name='테스', pass_context=True)
    async def _tes(self, ctx):
        conn = sqlite3.connect("CEF.db")
        # 탈퇴 전 정보 백업
        cur = conn.cursor()
        cur.execute('SELECT * from List WHERE ID_Num=?', (ctx.author.id, ))
        temp = cur.fetchall()
        print(temp)


def setup(bot):
    bot.add_cog(Member(bot))