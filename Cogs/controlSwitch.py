import discord
from discord.ext import commands
import sqlite3
import asyncio

##############
# 스위치별 설명
# 1. changeNick
#   - 1이면 닉변 가능
#   - 0이면 닉변 불가능
# 2. DEVELOPER_SWITCH
#   - 1이면 개발자만 사용 가능
#   - 0이면 모두 사용 가능


class ControlSwitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='컨트롤스위치테스트', pass_context=True)
    async def _controlswitchtest(self, ctx):
        await ctx.send("컨트롤스위치테스트")

    @commands.command(name='스위치변경', pass_context=True)
    async def _changeSwitch(self, ctx):
        try:
            await ctx.send("```변경할 스위치를 선택하세요.\n"
                           "1. 닉변\n"
                           "2. 개발자 전용```")
            msg = await self.bot.wait_for("message", check=lambda m : m.author == ctx.author and m.channel == ctx.channel,
                                          timeout=10.0)

        except asyncio.TimeoutError :
            await ctx.channel.send("시간 초과")
        else:
            if msg.content.lower() == '1':
                switch = 1
            elif msg.content.lower() == '2':
                switch = 2
        #
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Switch WHERE Number=:Number", {"Number" : switch})
            temp = cur.fetchall()[0]
            print(temp)
            if switch == 1:
                if temp[2] == 0:
                    cur = conn.cursor()
                    cur.execute("UPDATE Switch SET Status=?", (1,))
                    await ctx.send("```정상 작동하였습니다.\n"
                                   "닉네임 변경이 가능합니다.```")
                if temp[2] == 1:
                    cur = conn.cursor()
                    cur.execute("UPDATE Switch SET Status=?", (0,))
                    await ctx.send("```정상 작동하였습니다.\n"
                                   "닉네임 변경이 불가합니다.```")
            elif switch == 2:
                if temp[2] == 0:
                    cur = conn.cursor()
                    cur.execute("UPDATE Switch SET Status=?", (1,))
                    await ctx.send("```정상 작동하였습니다.\n"
                                   "개발자만 사용 가능하도록 변경되었습니다.```")
                if temp[2] == 1:
                    cur = conn.cursor()
                    cur.execute("UPDATE Switch SET Status=?", (0,))
                    await ctx.send("```정상 작동하였습니다.\n"
                                   "모두 사용 가능하도록 변경되었습니다.```")

        finally:
            conn.commit()
            conn.close()

    @commands.command(name='스위치현황', pass_context=True)
    async def _statusSwitch(self, ctx):
        msg = '```서버 봇 스위치 현황\n'
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Switch")
        num = 1
        for row in cur.fetchall():
            if row[2] == 0:
                msg = msg + row[1] + " - OFF\n"
            elif row[2] == 1:
                msg = msg + row[1] + " - ON\n"

        msg = msg + '```'
        await ctx.send(content=f"{msg}")


    @commands.command(name='스위치추가', pass_context=True)
    async def _switchtest(self, ctx):
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        param = 1
        cur.execute("INSERT INTO Switch VALUES(?, ?, ?)", (2, 'DELVEOPER_SWITCH', 0))
        #cur.execute("SELECT * FROM Switch WHERE Number=:Number", {"Number":1})
        #temp = cur.fetchall()[0]
        #print(temp)
        conn.commit()
        conn.close()

def setup(bot):
    bot.add_cog(ControlSwitch(bot))