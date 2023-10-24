import discord
from discord.ext import commands
import sqlite3
import myfun
from discord.utils import get
from forAccessDB import *
import asyncio


class ManageTeam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='팀등록', pass_context=True)
    async def _registerTeam(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='팀해체', pass_context=True)
    async def _deleteTeam(self, ctx):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            pass
        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

    @commands.command(name='팀정보수정', pass_context=True)
    async def _editTeamInfor(self, ctx, inputMessage):
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            abbName = ""
            fullName = ""
            colorCode = ""
            imoji = ""
            edit_abbName = ""
            edit_fullName = ""
            edit_colorCode = ""
            edit_imoji = ""

            temp = ''
            abbList = []
            abbList2 = []
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT Abbreviation From TEAM_INFORMATION")
            result = cur.fetchall()
            result.sort()
            i = 1
            # 임베드 작업
            embed = discord.Embed(title="현재 팀 목록")
            for row in result:
                if row[0] == "FA":
                    pass
                else:
                    temp = temp + str(i) + ". " + row[0] + "\n"
                    text = str(i) + ". " + row[0]
                    abbList.append((i, row[0]))
                    abbList2.append(text)
                    i = i + 1
                    embed.add_field(name=f"{row[0]}", value=" ", inline=True)
            ann_msg = await ctx.send(f"```팀 정보 수정합니다.\n"
                                     f"팀 약자 : {abbName}\n"
                                     f"팀 이름 : {fullName}\n"
                                     f"색상 코드 : {colorCode}\n"
                                     f"이모지 : {imoji} -> {}```")
            ann_msg1 = await ctx.send(f"1. 수정할 팀의 번호를 입력해주세요.\n"
                           f"{temp}")
            await ctx.send(embed=embed)
            # 팀 약자 입력
            try :
                msg = await self.bot.wait_for("message",
                                              check=lambda
                                                  m : m.author == ctx.author and m.channel == ctx.channel,
                                              timeout=30.0)
                print(msg)
                print(msg.content)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.\n"
                                  f"다시 명령어를 입력해주세요\n"
                                  f"해당 메시지는 30초 후 자동 삭제됩니다.")
            else:
                abbName = msg.content.upper()
            # ----------------- 수정할 항목 선택 -----------------
            await ann_msg1.delete()
            await ann_msg.edit(f"")
            embed2 = discord.Embed2(title="변경할 항목 선택")
            

        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

async def setup(bot):
    await bot.add_cog(ManageTeam(bot))