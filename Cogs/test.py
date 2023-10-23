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
from datetime import datetime, timedelta
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
        from table2ascii import table2ascii as t2a, PresetStyle

        output = t2a(
            header=["닉네임", "계약 시작일", "계약기간", "계약 종료일"],
            body=[["테스트1", 20231021, 30, 20231119], ["테스트2", 20231021, 20, 20231109],
                  ["테스트3", 20231022, 14, 20231104], ["테스트4", 20231023, 30, 20231121]],
            style=PresetStyle.borderless
        )
        await ctx.send(f"```\n{output}\n```")
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
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM SEASON_USER_HISTORY WHERE ID=?", (ctx.author.id,))
        result = cur.fetchall()
        nickname = getNicknameFromUserInfoWithID(ctx.author.id)
        text = ''
        for row in result:
            season = row[1]
            print(season, type(season))
            team = row[2]
            print(team, type(team))
            job = row[3]
            print(job, type(job))
            position = row[4]
            print(position, type(position))
            rank = row[5]
            print(rank, type(rank))
            totalcount = getTotalCountFromSeasonTeamCount(season)
            print(totalcount, type(totalcount))
            text = text + season + " 시즌 | " + team + " (" + job + ") 포지션 : " + position + " | 총 " + str(totalcount) + "팀 중 " + str(rank) + "위\n"
            print(text)
        await ctx.send(f"```{text}```")
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