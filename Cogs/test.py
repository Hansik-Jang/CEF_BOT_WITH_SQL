import discord
from discord.ext import commands
from discord.utils import get
from discord import app_commands
import random
import myfun
import config
import sqlite3
import asyncio
import checkFun
import forAccessDB
from forAccessDB import *

from typing import Literal, Optional
from discord.ext import commands
from discord.ext.commands import Greedy, Context # or a subclass of yours


class Test(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()

    @app_commands.command(name="슬래시", description="슬래시 테스트 중")
    async def tree(
            self,
            interaction: discord.Interaction,
            nickname: str,
            mainPos: str,
            subPos: str) -> None:
        await interaction.respons.send_message(f"ID : {interaction.user.id}\n"
                                               f"닉네임 : {nickname}\n"
                                               f"주포지션 : {mainPos}, 부포지션 : {subPos}")

    @app_commands.command(name="테스트1", description="테스트 1번")
    async def slasytest1(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("테스트1")'''

    @commands.command(name='테스트', pass_context=True)
    async def _test1(self, ctx):
        li = []
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM SEASON_USER_HISTORY WHERE ID=?", (ctx.author.id,))
        data_list = cur.fetchall()
        data_list.sort(key=lambda x : x[1])  # Season 순으로 정렬
        data_list.append((0, "", "", "", "", 0))
        print(data_list)
        for data in data_list:
            print(data)
            text = ""
            season = str(data[1])
            abbName = str(data[2])
            job = str(data[3])
            pos = str(data[4])
            rank = str(data[5])
            host = str(getHostFromSeasonTeamCount(season))
            totalCount = str(getTotalCountFromSeasonTeamCount(season))
            print(type(season), type(abbName), type(job), type(pos), type(rank), type(host), type(totalCount))
            text = text + season + abbName + job + pos + rank + host + totalCount
            print(text)
            li.append(text)
            print(li)
        print(li)

    @commands.command(name='바꿔', pass_context=True)
    async def _test2(self, ctx, *, name):
        if config.devlopCheck(ctx):
            user = ctx.author
            await user.edit(nick=name)
            await ctx.send(content=f"{name}으로 변환 완료")
        else:
            await ctx.send("개발자 전용 명령어")

    @commands.command(name='닉변권추가', pass_context=True)
    async def _test3(self, ctx):
        result = forAccessDB.getUserInformation(ctx)
        count = result[6] + 1

        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("UPDATE USER_INFORMATION SET NickChangeCoupon=? WHERE id=?", (count, ctx.author.id))
            conn.commit()
        finally:
            conn.close()
        await ctx.send("닉변권 1회 추가")

    @commands.command(name='테스트4', pass_context=True)
    async def _test4(self, ctx):
        print(type(forAccessDB.get))
        print(type(forAccessDB.getTotalCountFromSeasonTeamCount("24-1")))

    @commands.command(name='테스트제거', pass_context=True)
    async def _test8(self, ctx):
        user = ctx.author
        test_role = get(ctx.guild.roles, name="테스트용")
        await user.remove_roles(test_role)
        await ctx.send("테스트용 역할 제거 완료")

        try :
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM USER_INFORMATION WHERE ID=?", (ctx.author.id, ))
            conn.commit()
        finally :
            conn.close()



async def setup(bot):
    await bot.add_cog(Test(bot))