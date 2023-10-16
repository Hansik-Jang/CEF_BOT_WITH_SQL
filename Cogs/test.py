import discord
from discord.ext import commands
from discord.utils import get
import random
import myfun
import config
import sqlite3
import asyncio
import checkFun
import forAccessDB


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='임시용', pass_context=True)
    async def _copypermission(self, ctx):
        result = checkFun.checkNicknameOverlap(ctx)
        await ctx.send(content=f"가입 가능 여부 : {result[0]}\n"
                               f"INFO 중복 여부 : {result[1]}\n"
                               f"EXCEP 중복 여부 : {result[2]}")


    @commands.command(name='테스트', pass_context=True)
    async def _test(self, ctx) :
        result = forAccessDB.getUserInformation(ctx)
        await ctx.send(content=f"{result}")

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
        result2 = myfun.recombinationNickname(ctx)
        await ctx.send(content=f"{result2}")

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



def setup(bot):
    bot.add_cog(Test(bot))