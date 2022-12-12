import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import sqlite3
import myfun


class League(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='선수등록', pass_context=True)
    async def _registration(self, ctx, team, member: discord.Member, price):
        try:
            conn = sqlite3.connect("CEB.db")
            cur = conn.cursor()
            cur.execute("UPDATE League_Member SET price=? wallet=? WHERE id=?",
                        )
        finally:
            conn.commit()
            conn.close()

    @commands.command(name='등록테스트', pass_context=True)
    async def _registration2(self, ctx, team, member: discord.Member, pos, price):
        team_name_list = ["TEAM_A", "TEAM_B", "TEAM_C", "TEAM_D", "TEAM_E"]
        position_list = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]
        convertprice = int(price) * 100000000       # 억단위 변환
        addWallet = convertprice * 0.00001
        add_wallet = price * 0

        role = get(member.guild.roles, name=myfun.teamNameConvert(team))
        if team in team_name_list:
            if pos in position_list:
                try:
                    conn = sqlite3.connect("CEB.db")
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM table1 WHERE id=?", (ctx.author.id,))
                    ex_wallet = cur.fetchall()[2]

                    cur.execute("UPDATE League_Member SET price=? wallet=? WHERE id=?",
                                )
                finally:
                    conn.commit()
                    conn.close()
            else:
                await ctx.send("포지션 입력이 잘못 되었습니다.")
        else:
            await ctx.send("팀 이름 입력이 잘못 되었습니다.")

    @commands.command(name='내전리그이모지초기화', pass_context=True)
    async def _erageimojiaboutNaeJeon(self, ctx):
        for member in ctx.guild.members:
            print(member.display_name)



def setup(bot):
    bot.add_cog(League(bot))