import discord
from discord.ext import commands
import sqlite3
import os


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='이벤트테스트', pass_context=True)
    async def _test(self, ctx):

        await ctx.send("이벤트테스트")

    @commands.Cog.listener()
    async def on_ready(self):
        global DEVELOPER_SWITCH
        print('로그인 중')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')
        game = discord.Game("테스트 봇/개발 중")
        await self.bot.change_presence(status=discord.Status.online, activity=game)

        await self.bot.tree.sync(discord.Object(id=706480732477849650))
        print('싱크 완료')


async def setup(bot):
    await bot.add_cog(Event(bot))