import asyncio

import myfun
from myfun import *
import os
import discord
import time
import asyncio
from discord.ext import commands
from discord import app_commands
#import discord_ui
#import gspread
import sqlite3
#from discord_components import DiscordComponents, Button, ButtonStyle, Interaction, component
from datetime import datetime, timedelta
from typing import Literal, Optional
from discord.ext.commands import Greedy, Context # or a subclass of yours

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)
f = open("key.txt", 'r')
key = f.readline()

DEVELOPER_SWITCH = True


@bot.event
async def on_ready():

    print("봇 연결 완료")




@bot.command(name="로드", aliases=["load"])
async def load_commands(ctx, extension):
    await bot.load_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 로드했습니다!")


@bot.command(name="언로드", aliases=["unload"])
async def unload_commands(ctx, extension):
    await bot.unload_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 언로드했습니다!")


@bot.command(name="리로드", aliases=["reload"])
async def reload_commands(ctx, extension=None):
    if extension is None:  # extension이 None이면 (그냥 !리로드 라고 썼을 때)
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                await bot.unload_extension(f"Cogs.{filename[:-3]}")
                await bot.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(f":white_check_mark: Cogs.{filename[:-3]}를 다시 불러왔습니다!")
    else:
        await bot.unload_extension(f"Cogs.{extension}")
        await bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")

async def load():
    for filename in os.listdir('./Cogs') :
        if filename.endswith('.py') :
            await bot.load_extension(f"Cogs.{filename[:-3]}")
            print(f"Cogs.{filename[:-3]} 로드")

async def main():
    await load()
    await bot.start(key)
'''
@bot.command(name='스위치조회')
async def _testS(ctx):
    if DEVELOPER_SWITCH:
        await ctx.send("현재 상태 True")
    else:
        await ctx.send("현재 상태 False")'''

asyncio.run(main())