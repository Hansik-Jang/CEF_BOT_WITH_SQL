import discord
import datetime
import sqlite3
from myfun import *
from discord.ext import commands
from discord.utils import get


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='가입', pass_context=True)
    async def _join(self, ctx):
        join = False
        overlap = False
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Main')
        rows = cur.fetchall()
        for row in rows:
            print(ctx.author.id, row[2])
            if str(ctx.author.id) == row[2]:
                join = True
                print(ctx.author.id, row[2], join)
                break
            if convertNick(ctx) == row[3]:
                overlap = True
                break
        print(join, overlap)
        if overlap == False and join == False:
            if ',' in ctx.author.display_name or '.' in ctx.author.display_name :
                await ctx.send("```정확한 닉네임 양식을 지켜주세요\n"
                               "닉네임 양식 : 닉네임[주포지션/부포지션]\n"
                               "주 포지션과 부 포지션의 구분은 '/'을 사용해주세요.\n"
                               "해당 봇에서는 '.'를 인식하지 않으며, 이는 버그의 원인이 됩니다.\n"
                               "닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")
            elif "[" in ctx.author.display_name:
                if '/' in ctx.author.display_name:
                    now = datetime.datetime.now()
                    now_time = now.strftime('%Y-%m-%d %H:%M:%S')       # 가입 시간
                    # DB에 추가 --------------------------------------------------#
                    conn2 = sqlite3.connect("test.db")
                    cur2 = conn2.cursor()
                    cur2.execute('INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?, ?)', \
                                (now_time, '0000-00-00 00:00:00', str(ctx.author.id), convertNick(ctx),\
                                convertJupo(ctx), convertBupo(ctx), '무소속'))
                    conn2.commit()
                    conn2.close()
                    # -----------------------------------------------------------#
                    user = ctx.author
                    roles = [get(ctx.guild.roles, name='CEF'), get(ctx.guild.roles, name='신규')]
                    for role in roles:
                        await user.add_roles(role)
                    nickname = assembleIncludeBupo(ctx)
                    await user.edit(nick=nickname + "🐤")
                    await ctx.send("```가입을 환영합니다!```")
                    channel = get(ctx.guild.channels, name='가입-탈퇴-명단')
                    await channel.send(content=f"<신규가입> {ctx.author.mention} (가입일자 : {now_time})")
                else:
                    now = datetime.datetime.now()
                    now_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 가입 시간
                    # DB에 추가 --------------------------------------------------#
                    conn2 = sqlite3.connect("test.db")
                    cur2 = conn2.cursor()
                    cur2.execute('INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?, ?)', \
                                 (now_time, '0000-00-00 00:00:00', str(ctx.author.id), convertNick(ctx), \
                                  convertJupo(ctx), '없음', '무소속'))
                    conn2.commit()
                    conn2.close()
                    # -----------------------------------------------------------#
                    user = ctx.author
                    roles = [get(ctx.guild.roles, name='CEF'), get(ctx.guild.roles, name='신규')]
                    for role in roles:
                        await user.add_roles(role)
                    nickname = assembleExcludeBupo(ctx)
                    await user.edit(nick=nickname + "🐤")
                    await ctx.send("```가입을 환영합니다!```")
                    channel = get(ctx.guild.channels, name='가입-탈퇴-명단')
                    #await channel.send(content=f"<신규가입> {ctx.author.mention} (가입일자 : {now_time})")
            else:
                await ctx.send("```정확한 닉네임 양식을 지켜주세요\n닉네임 양식 : 닉네임[주포지션/부포지션] or 닉네임[주포지션]```")

        conn.close()

    @commands.command(name='test', pass_context=True)
    async def _test(self, ctx):
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Main')
        rows = cur.fetchall()
        for row in rows:
            print(row)

def setup(bot):
    bot.add_cog(Member(bot))