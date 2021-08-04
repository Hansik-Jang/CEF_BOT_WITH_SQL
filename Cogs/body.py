import discord
from discord.ext import commands

class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='바디테스트', pass_context=True)
    async def _test(self, ctx):
        name = discord.utils.get(ctx.author.guild, id="146549960312225792")
        print(name.display_name)
        await self.bot.send(f"{name.mention}")


def setup(bot):
    bot.add_cog(Body(bot))