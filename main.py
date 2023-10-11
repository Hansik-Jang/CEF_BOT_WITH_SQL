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

DEVELOPER_SWITCH = True


@bot.command(name='스위치조회')
async def _testS(ctx):
    if DEVELOPER_SWITCH:
        await ctx.send("현재 상태 True")
    else:
        await ctx.send("현재 상태 False")


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
