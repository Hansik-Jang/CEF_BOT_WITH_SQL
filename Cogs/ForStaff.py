import discord
from discord.ext import commands

import config
import myfun
from discord.utils import get
from forAccessDB import *

class 스태프전용(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="닉변권부여", pass_context=True, aliases=['닉변권'])
    async def _giveNickChagneCoupon(self, ctx, member:discord.Member, count:int=None):
        if count is None:
            count = 1
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names:
            if 0 < count < 11:
                if checkUseJoinCommandWithID(member.id) :
                    ex_changeCoupon = getNickChangeCouponFromUserInfoWithID(member.id)
                    new_changeCoupon = ex_changeCoupon + count
                    try:
                        conn = sqlite3.connect("CEF.db")
                        cur = conn.cursor()
                        cur.execute("UPDATE USER_INFORMATION SET NickChangeCoupon=? WHERE ID=?", (new_changeCoupon, member.id))

                    finally:
                        conn.commit()
                        conn.close()
                    await ctx.send(f"{member.mention}\n"
                                   f"{myfun.getNickFromDisplayname2(member.display_name)} 닉변권 {count} 회 추가되었습니다.\n"
                                   f"{ex_changeCoupon} 회 -> {new_changeCoupon} 회")
                else :
                    await ctx.reply("해당 인원은 등록되지 않는 인원입니다.")
            else:
                await ctx.reply("1 이상, 10 이하의 숫자만 입력 가능합니다.")
        else:
            await ctx.reply("해당 명령어는 스태프만 사용 가능합니다.")

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
    async def _showNicknameException(self, ctx) :
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NICKNAME_EXCEPTION")

        rows = cur.fetchall()
        await ctx.send(content=f"{rows}")

    async def cog_command_error(self, ctx, error) :
        await ctx.send(f"스태프 전용 : {error}")
async def setup(bot) :
    await bot.add_cog(스태프전용(bot))