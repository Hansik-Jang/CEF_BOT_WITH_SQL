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

    @commands.command(name='테스트', pass_context=True,
                      help="설명서", brief="사용법")
    async def _test1(self, ctx, abbName, *people: discord.Member):
        # 디스코드 상호작용
        guild = ctx.guild
        await guild.create_role(name=abbName, colour=discord.Colour.red())  # 역할 생성
        for member in people :
            role = get(ctx.guild.roles, name=abbName)
            await member.add_roles(role)
            await ctx.send(f"{member.display_name} - {abbName} 역할 추가 완료")

        # DB TEAM_INFORMATION 인서트
        try :
            fullName = abbName
            colorCode = "0xff0000"
            lastRank = 99
            url = "https://cdn.discordapp.com/attachments/853175297926889472/1168485933058895912/FCB.png?ex=6551f053&is=653f7b53&hm=44ede6da9286e3f03321077f5b86710a80530a94d345f2d4536cffedec0dd39d&"
            conn = sqlite3.connect("CEF.db")
            print("a")
            cur = conn.cursor()
            print("b")
            cur.execute("INSERT INTO TEAM_INFORMATION VALUES(?, ?, ?, ?, ?, ?);",
                        (abbName, fullName, colorCode, lastRank, "", url))
            await ctx.send("DB 추가 완료")
        except :
            print("실패")
        finally :
            conn.commit()
            conn.close()
        await ctx.reply("역할 이모지는 서버 설정에서 별도로 설정해주세요.")
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