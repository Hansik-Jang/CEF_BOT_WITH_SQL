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


@bot.event
async def on_ready():
    DiscordComponents(bot)

@bot.command()
async def testButton(ctx):
  ticket = await ctx.send(
      "_ _",
      components = [
          Button(label = "Test", style=ButtonStyle.blue, custom_id="test")
      ]
  )
  interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "test")
  embed=discord.Embed(title="Test")
  await interaction.respond(embed=embed)

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
    '''jupo = ''
    bupo = ''
    pos_li = ['st', 'lw', 'rw', 'cam', 'cm', 'cdm', 'lb', 'cb', 'rb', 'gk']
    # ------------------------- 주포지션 ----------------------------------
    jupo_msg = await ctx.channel.send("```주포지션을 입력하세요. 아래에 표기된 포지션만 입력 가능합니다.\n"
                           "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK```")
    try:
        msg = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                 timeout=10.0)

    except asyncio.TimeoutError:
        await ctx.channel.send("시간 초과")
    else:
        if msg.content.lower() == 'st':
            await msg.delete()
            await ctx.send("ST 선택")
            jupo = 'ST'
        elif msg.content.lower() == 'lw':
            await msg.delete()
            await ctx.send("LW 선택")
            jupo = 'LW'
        elif msg.content.lower() == 'rw':
            await msg.delete()
            await ctx.send("RW 선택")
            jupo = 'RW'
        elif msg.content.lower() == 'cam':
            await msg.delete()
            await ctx.send("CAM 선택")
            jupo = 'CAM'
        elif msg.content.lower() == 'CM':
            await msg.delete()
            await ctx.send("CM 선택")
            jupo = 'CM'
        elif msg.content.lower() == 'cdm':
            await msg.delete()
            await ctx.send("CDM 선택")
            jupo = 'CDM'
        elif msg.content.lower() == 'lb':
            await msg.delete()
            await ctx.send("LB 선택")
            jupo = 'LB'
        elif msg.content.lower() == 'cb':
            await msg.delete()
            await ctx.send("CB 선택")
            jupo = 'CB'
        elif msg.content.lower() == 'rb':
            await msg.delete()
            await ctx.send("RB 선택")
            jupo = 'RB'
        elif msg.content.lower() == 'gk':
            await msg.delete()
            await ctx.send("GK 선택")
            jupo = 'GK'
        else:
            await ctx.send("잘못 입력")
    await jupo_msg.delete()
    # ------------------------- 부포지션 ----------------------------------
    bupo_msg = await ctx.channel.send("```부포지션을 입력하세요. 아래에 표기된 포지션만 입력 가능합니다.\n"
                           "ST, LW, RW, CAM, CM, CDM, LB, CB, RB, GK```")
    try:
        msg = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                 timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.channel.send("시간 초과")
    else:
        if msg.content.lower() == 'st':
            await msg.delete()
            await ctx.send("ST 선택")
            bupo = 'ST'
        elif msg.content.lower() == 'lw':
            await msg.delete()
            await ctx.send("LW 선택")
            bupo = 'LW'
        elif msg.content.lower() == 'rw':
            await msg.delete()
            await ctx.send("RW 선택")
            bupo = 'RW'
        elif msg.content.lower() == 'cam':
            await msg.delete()
            await ctx.send("CAM 선택")
            bupo = 'CAM'
        elif msg.content.lower() == 'cm':
            await msg.delete()
            await ctx.send("CM 선택")
            bupo = 'CM'
        elif msg.content.lower() == 'cdm':
            await msg.delete()
            await ctx.send("CDM 선택")
            bupo = 'CDM'
        elif msg.content.lower() == 'lb':
            await msg.delete()
            await ctx.send("LB 선택")
            bupo = 'LB'
        elif msg.content.lower() == 'cb':
            await msg.delete()
            await ctx.send("CB 선택")
            bupo = 'CB'
        elif msg.content.lower() == 'rb':
            await msg.delete()
            await ctx.send("RB 선택")
            bupo = 'RB'
        elif msg.content.lower() == 'gk':
            await msg.delete()
            await ctx.send("GK 선택")
            bupo = 'GK'
        elif msg.content.lower() == 'x' or msg.content == '없음':
            await msg.delete()
            await ctx.send("없음 선택")
            bupo = '없음'
        else:
            await ctx.send("잘못 입력")
    await bupo_msg.delete()
    await ctx.send(content=f"```<입력한 정보>\n"
                           f"주포지션 : {jupo}\n"
                           f"부포지션 : {bupo}```")
    # ------------------------- 닉네임 변환 ----------------------------------
    if bupo == '':
        nickname = myfun.getNickFromDisplayname(ctx) + "[" + jupo + "]" + myfun.getImojiFromDisplayname(ctx)
    else:
        nickname = myfun.getNickFromDisplayname(ctx) + "[" + jupo + "/" + bupo + "]" + myfun.getImojiFromDisplayname(ctx)
    await ctx.send(nickname)
    user = ctx.author
    await user.edit(nick=nickname)'''


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
