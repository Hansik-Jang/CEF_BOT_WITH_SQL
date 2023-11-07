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
from discord.ui import Select

dropdown_msg = None


class Test(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='테스트', pass_context=True,
                      help="설명서", brief="사용법")
    async def _test1(self, ctx):
        sortResult = ['', '', '', '', '', '', '', '', '', '', '']
        name = "FCB"
        embed = discord.Embed(title=name)
        # DB 정보 얻기
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE TeamName=?", (name, ))
        teamList = cur.fetchall()
        # DB 정보 정렬하여 Embed로 정리
        for i, data in enumerate(teamList):
            for position in config.positionList:
                if data[2] == position:
                    sortResult[i] = sortResult[i] + data[1] + "\n"
        for i, position in enumerate(config.positionList):
            embed.add_field(name=position, value=sortResult[i])

        await ctx.send(embed=embed)


    @commands.command(name='테스트2', pass_context=True,
                      help="설명서", brief="사용법")
    async def _test5(self, ctx) :
        print(getTeamList())
        teamList = []
        for li in getTeamList():
            print(li)
            teamList.append(li[0])
            print(teamList)

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
        pic_ext = ['.jpg', '.png', '.jpeg']
        def check(message) :
            if message.author == ctx.author and message.channel == ctx.channel :
                attachments = message.attachments
                if len(attachments) == 0 :
                    return False
                attachment = attachments[0]
                return attachment.filename.endswith(('.jpg', '.png'))
        await ctx.send("이미지 업로드")
        try :
            image_msg = await self.bot.wait_for("message", check=check, timeout=60.0)
        except asyncio.TimeoutError :
            await ctx.send("시간이 초과되었습니다.\n"
                           f"다시 명령어를 입력해주세요\n"
                           f"해당 메시지는 10초 후 자동 삭제됩니다.", delete_after=10)
        else :
            print(image_msg.attachments[0].filename)
            image = image_msg.attachments[0]
            print(image.url)
            print(type(image.url))
        embed2 = discord.Embed(title="테스트", description="   ")
        embed2.add_field(name="테스트", value="테스트")
        embed2.set_thumbnail(url=image.url)
        await ctx.send(embed=embed2)
        role = get(ctx.guild.roles, name="USA")
        print(role.name)
        await role.edit(display_icon=f"{image}")
        await ctx.send("완료")

        # Cog error handler

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"An error occurred in the Test cog: {error}")

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