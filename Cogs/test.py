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

    @commands.command(name='테스트', pass_context=True)
    async def _test1(self, ctx):
        role = get(ctx.guild.roles, name="테스트용")
        await role.edit(name="Tester")
        await ctx.send("변경 완료")
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
        try :
            msg = await self.bot.wait_for("message",
                                          check=lambda
                                              m : m.author == ctx.author and m.channel == ctx.author,
                                          timeout=30.0)
        except asyncio.TimeoutError :
            await ctx.send("시간이 초과되었습니다.\n"
                              f"다시 명령어를 입력해주세요\n"
                              f"해당 스레드는 30초 후 자동 삭제됩니다.")
        else:
            if msg.content.lower() == '1' :
                mainPosition = "LW"

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