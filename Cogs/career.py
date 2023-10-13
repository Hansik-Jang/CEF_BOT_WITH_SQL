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
            cur.execute("SELECT * FROM USER_INFORMATION WHERE id=?", (ctx.author.id, ))
            temp = cur.fetchall()
            print(temp)
            idNum = "ID : " + str(temp[0][0])
            nickname = temp[0][1].replace("'", "")
            count = str(temp[0][6]) + " 회"
            history = "24-1 '소속팀' '직책' '순위' 中 '전체 팀 수'\n" \
                      "(예시)\n" \
                      "24-1 FCB 감독 5위 中 16팀"
            embed = discord.Embed(title=nickname, description=temp[0][0])
            embed.add_field(name="소속", value=temp[0][4], inline=True)
            embed.add_field(name="신분", value=temp[0][5], inline=True)
            embed.add_field(name="닉네임 변경권", value=count, inline=True)
            embed.add_field(name="주포지션", value=temp[0][5], inline=True)
            embed.add_field(name="부포지션", value=temp[0][5], inline=True)
            embed.add_field(name="히스토리", value=history, inline=False)


            embed2_msg = await ctx.send(embed=embed)
        finally:
            conn.close()
        print(temp)



def setup(bot):
    bot.add_cog(Body(bot))
