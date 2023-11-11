import sqlite3
import discord
from discord.ext import commands
from discord.utils import get


class AboutDB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='예외추가', pass_context=True)
    async def _insertNicknameException(self, ctx, *, text) :
        li = [text]
        try :
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO NICKNAME_EXCEPTION(Nickname) VALUES(?);", li)
            conn.commit()
            await ctx.send(content=f"{text} DB 추가 완료")

        finally :
            conn.close()

    @commands.command(name='예외목록', pass_context=True)
    async def _showNicknameException(self, ctx):
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NICKNAME_EXCEPTION")

        rows = cur.fetchall()
        await ctx.send(content=f"{rows}")


async def setup(bot):
    await bot.add_cog(AboutDB(bot))