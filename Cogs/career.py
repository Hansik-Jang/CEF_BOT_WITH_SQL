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
        finally:
            conn.close()
        print(temp)

def setup(bot):
    bot.add_cog(Body(bot))
