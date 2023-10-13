import discord
from discord.ext import commands
from discord.utils import get
import random
import myfun
import config
import sqlite3
import asyncio
import checkFun


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='임시용', pass_context=True)
    async def _copypermission(self, ctx, name):
        pass

    @commands.command(name='테스트', pass_context=True)
    async def _test(self, ctx) :
        await ctx.send(content=f"디스플레이 네임 {ctx.author.display_name}")
        await ctx.send(content=f"네임 {ctx.author.name}")
        if ctx.author.display_name == ctx.author.name:
            await ctx.send("동일")
        else:
            await ctx.send("다름")

    @commands.command(name='바꿔', pass_context=True)
    async def _test2(self, ctx, *, name):
        if config.devlopCheck(ctx):
            user = ctx.author
            await user.edit(nick=name)
            await ctx.send(content=f"{name}으로 변환 완료")
        else:
            await ctx.send("개발자 전용 명령어")

    @commands.command(name='문자비교', pass_context=True)
    async def _test3(self, ctx, *, text):
        temp = text.split("/")
        text1 = temp[0].replace(" ", "")
        text2 = temp[1].replace(" ", "")
        if text1.lower() == text2.lower():
            await ctx.send(content=f"{temp[0], temp[1]} 일치")
        else:
            await ctx.send(content=f"{temp[0], temp[1]} 불일치")

    @commands.command(name='포함검사', pass_context=True)
    async def _test4(self, ctx, *, text):
        dbCheck = True
        temp = text.split("/")
        text1 = temp[0].replace(" ", "").lower()
        text2 = temp[1].replace(" ", "").lower()

        if text1 in text2:
            await ctx.send(content=f"{text1, text2} 앞에가 뒤에꺼에 포함됨")
        elif text2 in text1:
            await ctx.send(content=f"{text1, text2} 뒤에가 앞에꺼에 포함됨")
        elif text1 == text2:
            await ctx.send(content=f"{text1, text2} 일치함")
        else:
            await ctx.send(content=f"{text1, text2} 포함 안됨")


    @commands.command(name='DB검사', pass_context=True)
    async def _test6(self, ctx, *, text):
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NICKNAME_EXCEPTION")
        inName = ''
        rows = cur.fetchall()
        for row in rows:
            temp1 = row[0]
            temp2 = temp1.replace(" ", "").lower()
            text2 = text.replace(" ", "").lower()
            print(temp1, text2)
            if text2 == temp2:
                dbCheck = False
                inName = temp1
                break
            else :
                dbCheck = True

        if dbCheck:
            await ctx.send(content=f"{text} 는 DB에 존재하지 않음")
        else:
            await ctx.send(content=f"{inName}, {text} 는 DB에 존재하므로 예외 가능")

    @commands.command(name='스레드생성', pass_context=True)
    async def _test7(self, ctx):
        import time
        channel = get(ctx.guild.channels, id=ctx.channel.id)
        thread = await channel.create_thread(
            name="example",
            type=discord.ChannelType.private_thread
        )
        await thread.send(content=f"{ctx.author.mention} 테스트")
        time.sleep(20)
        await ctx.channel.purge(limit=2) # 명령어 입력 채널 텍스트 2개 삭제
        await thread.delete()

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