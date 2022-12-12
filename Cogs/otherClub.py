import discord
from discord.utils import get
from discord.ext import commands
import checkFun
import myfun

class OtherClub(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.li = []

    @commands.command(name='에버튼', pass_context=True)
    async def _everton(self, ctx):
        EVE_Role = get(ctx.guild.roles, name='EVE')
        if 'EVE_' in ctx.author.display_name:
            user = ctx.author
            await user.add_roles(EVE_Role)
            await ctx.reply(content=f"에버튼 소속 역할 부여 완료")
        else:
            await ctx.reply(content=f"EVE_ 양식에 맞게 닉네임 수정 후 다시 사용해주세요.")

    @commands.command(name='등번호저장', pass_context=True)
    async def _saveNum(self, ctx, name, num):
        self.li.append((ctx, name, num))
        await ctx.send(content=f"{ctx.author.mention}, 선수 이름 - {name}, 등번호 - {num} 저장 완료")

    @commands.command(name='등번호출력', pass_context=True)
    async def _showNum(self, ctx):
        for index in self.li:
            await ctx.send(content=f"{index[0].author.display_name} : {index[1]} ( {index[2]} )")


def setup(bot):
    bot.add_cog(OtherClub(bot))
