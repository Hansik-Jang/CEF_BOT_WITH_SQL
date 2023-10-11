import discord
from discord.ext import commands
import gspread
import sqlite3

import myfun


class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='내정보', pass_context=True)
    async def _myinformation(self, ctx):
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM User_Info WHERE id=?", (ctx.author.id, ))
            temp = cur.fetchall()
            print(temp)
            await ctx.send(content=f"닉네임 : {temp[0][2]}\n"
                                   f"소속 : {temp[0][5]}\n"
                                   f"주포 : {temp[0][3]}, 부포 : {temp[0][4]}\n"
                                   f"닉네임 변경권 : {temp[0][7]} 개")
        finally:
            conn.close()
        print(temp)

def setup(bot):
    bot.add_cog(Body(bot))
