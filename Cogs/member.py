import discord
from datetime import datetime, timedelta
import sqlite3
import checkFun
import asyncio
from myfun import *
from discord.ext import commands
from discord.utils import get
import string
import config
import myfun

global DEVELOPER_SWITCH


class Member(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.command(name='가입', pass_context=True, aliases=['join', 'Join'])
    async def _join(self, ctx) :
        joinSwitch = True  # Switch가 True면 가입 명령어 가능 상태
        nicknameFormatSwitch = True     # True이면 가입 절차 진행
        ownRoles = [role.name for role in ctx.author.roles]
        nickname = ''

        if config.baseRoleName in config.totalCommunityRoleNameList :  # CEF, RFA, KPA, EVT, SNI 역할이 있으면
            if config.baseRoleName in ownRoles :  # CEF 역할을 갖고 있으면
                await ctx.reply(content=f"이미 가입되었습니다.")
                joinSwitch = False  # 스위치 False로 변경
            else :  # CEF 역할을 안 갖고 있으면(타 커뮤니티 유저) 모든 역할 회수 후 스위치 True
                department = ""
                user = ctx.author
                for role in ownRoles :
                    if role.name == "EVT" :
                        department = "EVT"
                    elif role.name == 'RFA' :
                        department = "RFA"
                    elif role.name == "KPA" :
                        department = "KPA"
                    elif role.name == "SNI" :
                        department = "SNI"
                    await user.remove_roles(role)
                await ctx.send(content=f"```기존 역할 '{department}'를 회수하였습니다.```", delete_after=5)
                joinSwitch = True

        if joinSwitch :  # Switch가 True이면 가입 진행
            # 닉네임 양식 체크 -> 영어, 한글 검사 -> 중복 검사
            if checkFun.checkNicknameForm(ctx):  # 닉네임 양식 검사 (별명 안에 '[', ']'가 있으면
                nicknameFormatSwitch = True
            else :  # 닉네임 양식 검사 (별명 안에 '[', ']'가 없으면
                await ctx.send(content=f"CEF 서버는 디스코드 내 별명을 기준으로 활동하게 됩니다.\n"
                                       f"디스코드 닉네임은 **'{ctx.author.name}'**, "
                                       f"서버 내 별명은 **'{myfun.getNickFromDisplayname(ctx)}'**으로 ")
                if checkFun.checkDisplayNameChange(ctx):
                    # 디스코드 닉네임과 서버 별명이 다를 경우
                    try:
                        await ctx.send(content=f"현재 서버 내 별명인 **'{myfun.getNickFromDisplayname(ctx)}'**으로 가입을 진행하시겠습니까?\n"
                                               f"10초 이내에 원하는 번호를 입력해주세요.\n"
                                               f"1. 현재 닉네임으로 진행\n"
                                               f"2. 닉네임 수정 후 다시 진행")
                        msg = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=10.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("시간 초과")
                    else :
                        if msg.content.lower() == '1':
                            nicknameFormatSwitch = True
                            nickname = myfun.getNickFromDisplayname(ctx)
                        elif msg.content.lower() == '2':
                            nicknameFormatSwitch = False
                            await ctx.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후 다시 %가입 명령어를 입력해주세요.")
                else:
                    # 디스코드 닉네임과 서버 별명이 같을 경우
                    try:
                        await ctx.send(
                            content=f"서버 내 별명을 변경하지 않은 것으로 확인됩니다.\n"
                                    f"현재 닉네임으로 가입을 진행하시겠습니까? 10초 이내에 원하는 번호를 입력해주세요.\n"
                                    f"1. 현재 닉네임으로 진행\n"
                                    f"2. 닉네임 수정 후 다시 진행")
                        msg = await self.bot.wait_for("message",
                                                      check=lambda
                                                          m : m.author == ctx.author and m.channel == ctx.channel,
                                                      timeout=10.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("시간 초과")
                    else:
                        if msg.content.lower() == '1':
                            nicknameFormatSwitch = True
                            nickname = myfun.getNickFromDisplayname(ctx)
                        elif msg.content.lower() == '2':
                            nicknameFormatSwitch = False
                            await ctx.send(content=f"{ctx.author.mention}, 서버 별명하기를 통해 닉네임 수정 후 다시 %가입 명령어를 입력해주세요.")

        if nicknameFormatSwitch:    # 닉네임 문제 해결되어 가입 절차 진행
            if checkFun.checkEnglish(myfun.getNickFromDisplayname(ctx)):    # 닉네임 내 한글이 있는지 검사
                if checkFun.checkNicknameOverlap:   # 닉네임 중복 여부 검사
                    pass
                else:
                    pass
            else :
                pass

    @commands.command(name='탈퇴', pass_context=True, aliases=['Withdrawal', 'withdrawal'])
    async def _withdrawal(self, ctx) :
        pass

    @commands.command(name='포지션변경', pass_context=True, aliases=['chanegePosition'])
    async def _changePos(self, ctx) :
        pass

    @commands.command(name='닉네임변경', pass_context=True, aliases=['changeNickname'])
    async def _changeNick(self, ctx, *, nickname) :
        pass


def setup(bot) :
    bot.add_cog(Member(bot))
