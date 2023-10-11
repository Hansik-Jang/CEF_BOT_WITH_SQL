import discord
from discord.ext import commands
from discord_components import DiscordComponents
import sqlite3


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

def setup(bot):
    bot.add_cog(Event(bot))