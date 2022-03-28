import asyncio

import myfun
from myfun import *
import os
import discord
import time
from discord.ext import commands
import discord_ui
import gspread
import sqlite3
from discord_components import DiscordComponents, Button, ButtonStyle, Interaction, component
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix="$")
f = open("key.txt", 'r')
key = f.readline()





@bot.command(name='스위치조회')
async def _testS(ctx):
    if DEVELOPER_SWITCH:
        await ctx.send("현재 상태 True")
    else:
        await ctx.send("현재 상태 False")

@bot.command(name="테스트")
async def copy_info(ctx):
    nick = getNickFromDisplayname(ctx)
    jupo = getJupoFromDisplayname(ctx)
    bupo = getBupoFromDisplayname(ctx)
    if bupo == '없음':
        exclude = fitExcludeBupo(ctx)
    else:
        exclude = fitIncludeBupo(ctx)
    temp = int(
        str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(
            datetime.now().minute) + str(datetime.now().second))
    await ctx.send(f"{exclude}\n")
    await ctx.send(f"년 : {str(datetime.now().year)}\n"
                   f"월 : {str(datetime.now().month)}\n"
                   f"일 : {str(datetime.now().day)}\n"
                   f"시 : {str(datetime.now().hour)}\n"
                   f"분 : {str(datetime.now().minute)}\n"
                   f"초 : {str(datetime.now().second)}\n"
                   f"{temp}")
    print(type(datetime.now().year))


@bot.command(name="로드", aliases=["load"])
async def load_commands(ctx, extension):
    bot.load_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 로드했습니다!")


@bot.command(name="언로드", aliases=["unload"])
async def unload_commands(ctx, extension):
    bot.unload_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 언로드했습니다!")


@bot.command(name="리로드", aliases=["reload"])
async def reload_commands(ctx, extension=None):
    if extension is None:  # extension이 None이면 (그냥 !리로드 라고 썼을 때)
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(f":white_check_mark: Cogs.{filename[:-3]}를 다시 불러왔습니다!")
    else:
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")


for filename in os.listdir('Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"Cogs.{filename[:-3]} 로드")

bot.run(key)

'''
@bot.command(name="정보이동")
async def copy_info(ctx):
    cell = worksheet_list.acell('a1').value
    join = worksheet_list.range('B2:B' + cell)
    id = worksheet_list.range('D2:D' + cell)
    name = worksheet_list.range('E2:E' + cell)
    jupo = worksheet_list.range('F2:F' + cell)
    bupo = worksheet_list.range('G2:G' + cell)
    team = worksheet_list.range('H2:H' + cell)

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Main(Join_Date TEXT, ID_Num TEXT, Nickname TEXT, \
                Jupo TEXT, Bupo TEXT, Team TEXT)')

    for i in range(len(id)):
        cur.execute('insert into Main(Join_Date, ID_Num, Nickname, Jupo, Bupo, Team) values(?, ?, ?, ?, ?, ?)',
                    (join[i].value, id[i].value, name[i].value, jupo[i].value, bupo[i].value, team[i].value))
        print(i, join[i].value, id[i].value, name[i].value, jupo[i].value, bupo[i].value, team[i].value)

    conn.commit()
    print('a')
    cur.close()
    conn.close()
'''
