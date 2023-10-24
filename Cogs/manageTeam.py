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
            switch = True
            temp = ''
            abbList = []
            # 팀 약자 정보 획득
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT Abbreviation From TEAM_INFORMATION")
            result = cur.fetchall()
            result.sort()
            # 임베드 작업
            embed = discord.Embed(title="현재 팀 목록")
            for row in result:
                if row[0] == "FA":
                    pass
                else:
                    abbList.append(row[0])
                    embed.add_field(name=f"{row[0]}", value=" ", inline=True)
            ann_msg = await ctx.send(f"```팀 정보 수정합니다.\n"
                                     f"수정할 팀의 번호를 입력해주세요.\n"
                                     f"{temp}")
            embed_msg = await ctx.send(embed=embed)
            # 팀 약자 입력
            try :
                msg = await self.bot.wait_for("message",
                                              check=lambda
                                                  m : m.author == ctx.author and m.channel == ctx.channel,
                                              timeout=30.0)
            except asyncio.TimeoutError :
                await ctx.send("시간이 초과되었습니다.\n"
                               f"다시 명령어를 입력해주세요\n"
                               f"해당 메시지는 30초 후 자동 삭제됩니다.", delete_after=15)
            else:
                abbName = msg.content.upper()
            await ann_msg.edit(content=f"```<입력 현황>\n"
                               f"팀 약자 : {abbName} -> {edit_abbName}\n"
                               f"팀 이름 : {fullName} -> {edit_fullName}\n"
                               f"색상 코드 : {colorCode} -> {edit_colorCode}\n"
                               f"이모지 : {imoji} -> {edit_imoji}```")
            embed2 = discord.Embed(title="변경할 항목 선택", description="선택할 번호를 입력하세요.")
            embed2.add_field(name="1.", value="팀약자", incline=True)
            embed2.add_field(name="2.", value="풀네임", incline=True)
            embed2.add_field(name="3.", value="색상코드", incline=True)
            embed2.add_field(name="4.", value="이모지", incline=True)
            embed2.add_field(name="5.", value="종료하기", incline=True)
            print(1)
            await embed_msg.edit(embed=embed2)
            print(2)
            # ----------------- 수정할 항목 선택 -----------------
            while True:
                print("a")
                await asyncio.sleep(1)
                await ann_msg.edit(f"<입력 현황>\n"
                                   f"팀 약자 : {abbName} -> {edit_abbName}\n"
                                   f"팀 이름 : {fullName} -> {edit_fullName}\n"
                                   f"색상 코드 : {colorCode} -> {edit_colorCode}\n"
                                   f"이모지 : {imoji} -> {edit_imoji}```")
                # 번호 선택
                try :
                    msg_num = await self.bot.wait_for("message",
                                                  check=lambda
                                                      m : m.author == ctx.author and m.channel == ctx.channel,
                                                  timeout=30.0)
                except asyncio.TimeoutError :
                    await ctx.send("시간이 초과되었습니다.\n"
                                   f"다시 명령어를 입력해주세요\n"
                                   f"해당 메시지는 30초 후 자동 삭제됩니다.")
                else:
                    # 팀 약자 수정
                    if msg_num.content.lower() == "1":
                        await ctx.send("<팀 약자 수정>\n"
                                       "수정할 이름을 입력하세요.")
                        try :
                            msg1 = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=30.0)
                        except asyncio.TimeoutError:
                            await ctx.send("시간이 초과되었습니다.\n"
                                           f"다시 명령어를 입력해주세요\n"
                                           f"해당 메시지는 30초 후 자동 삭제됩니다.")
                        else:
                            edit_abbName = msg.content.upper()
                    # 팀 풀네임 수정
                    elif msg_num.content.lower() == "2":
                        pass
                    # 색상 코드 수정
                    elif msg_num.content.lower() == "3":
                        pass
                    # 팀 이모지 코드 수정
                    elif msg_num.content.lower() == "4":
                        pass
                    # 반복문 탈출
                    elif msg_num.content.lower() == "5":
                        break



        else:
            await ctx.reply("```해당 명령어는 스태프만 사용 가능합니다.```", delete_after=30)

async def setup(bot):
    await bot.add_cog(ManageTeam(bot))