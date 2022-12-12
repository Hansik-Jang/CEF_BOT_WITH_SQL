import discord
from discord.ext import commands
from discord.utils import get

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='투표', pass_context=True)
    async def _topyo(self, ctx):
        msg = await ctx.send("투표")

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')

    @commands.command(name='내전리그공지', pass_context=True)
    async def _naejeongongji(self, ctx):
        a_team_chat_id = get(ctx.guild.text_channels, id=790206738430820422)
        moderator = discord.utils.get(ctx.guild.roles, id=791693301769568277)
        await a_team_chat_id.send(content=f"{moderator.mention}\n"
                                          f"금일 21시에 내전리그 예정이니 참고바랍니다.")


def setup(bot):
    bot.add_cog(Game(bot))
