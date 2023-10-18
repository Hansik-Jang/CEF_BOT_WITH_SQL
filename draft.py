import discord
import time
import random
from FunForDraft import *
from discord.ext import commands
import discord
# from discord.ui import Button, View
import asyncio
import draftclass
import sqlite3
import myfun
import config

class Draft(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Draft(bot))


switch = 0
entry = []
testentry = []
captainmention = []
captainID = []
st = []
lw = []
rw = []
cm = []
cam = []
cdm = []
lb = []
cb = []
rb = []
gk = []

testst = []
testlw = []
testrw = []
testcm = []
testcam = []
testcdm = []
testlb = []
testcb = []
testrb = []
testgk = []

CAP_TIME = 10
DRAFT_TIME = 60
CURRENT_DRAFT_PLAYER_MAX = 0
CURRENT_DRAFT_COUNT = 0
SWITCH_STOP_DRAFT = True
TeamA = draftclass.TeamA()
TeamB = draftclass.TeamB()
TeamC = draftclass.TeamC()
TeamD = draftclass.TeamD()
draftclass.TeamA()
draftclass.TeamB()
draftclass.TeamC()
draftclass.TeamD()


class Draft(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
        self.buttons = ButtonsClient(bot)
        self.buttonST = Button(label='ST', custom_id='st', style=ButtonType().Danger)
        self.buttonLW = Button(label='LW', custom_id='lw', style=ButtonType().Danger)
        self.buttonRW = Button(label='RW', custom_id='rw', style=ButtonType().Danger)
        self.buttonCAM = Button(label='CAM', custom_id='cam', style=ButtonType().Success)
        self.buttonCM = Button(label='CM', custom_id='cm', style=ButtonType().Success)
        self.buttonCDM = Button(label='CDM', custom_id='cdm', style=ButtonType().Success)
        self.buttonLB = Button(label='LB', custom_id='lb', style=ButtonType().Primary)
        self.buttonCB = Button(label='CB', custom_id='cb', style=ButtonType().Primary)
        self.buttonRB = Button(label='RB', custom_id='rb', style=ButtonType().Primary)
        self.buttonGK = Button(label='GK', custom_id='gk', style=ButtonType().Secondary)
        self.button_li = [self.buttonST, self.buttonLW, self.buttonRW,
                          self.buttonCAM, self.buttonCM, self.buttonCDM,
                          self.buttonLB, self.buttonCB, self.buttonRB, self.buttonGK]

        self.DraftSwitchTwo = False
        self.DraftSwitchThree = False
        self.DraftSwitchFour = False


    def editSwitchTwo(self):
        if self.DraftSwitchTwo:
            self.DraftSwitchTwo = False
        else:
            self.DraftSwitchTwo = True

    def editSwitchThree(self):
        if self.DraftSwitchThree:
            self.DraftSwitchThree = False
        else:
            self.DraftSwitchThree = True

    def editSwitchFour(self):
        if self.DraftSwitchFour:
            self.DraftSwitchFour = False
        else:
            self.DraftSwitchFour = True

    def deleteNameFromPositonList(self, name):
        pos_li = [st, lw, rw, cam, cm, cdm, lb, cb, rb, gk]

        for pos in pos_li:
            if name in pos:
                pos.remove(name)



    @commands.command(name='개선', aliases=["개선주장"], pass_context=True)
    async def _개선(self, ctx, num) :
        global TeamA
        global TeamB
        global TeamC
        global TeamD
        global CURRENT_DRAFT_PLAYER_MAX
        global CURRENT_DRAFT_COUNT
        global SWITCH_STOP_DRAFT
        global switch

        SWITCH_STOP_DRAFT = True
        print(entry)
        switch = 0
        currectNum = True
        switchToDraft = False
        switchLoop = True
        testentry.clear()
        captainmention.clear()
        tempNumList = []

        st.clear()
        lw.clear()
        rw.clear()
        cam.clear()
        cm.clear()
        cdm.clear()
        lb.clear()
        cb.clear()
        rb.clear()
        gk.clear()

        testst.clear()
        testlw.clear()
        testrw.clear()
        testcam.clear()
        testcm.clear()
        testcdm.clear()
        testlb.clear()
        testcb.clear()
        testrb.clear()
        testgk.clear()

        TeamA.resetdata()
        TeamB.resetdata()
        TeamC.resetdata()
        TeamD.resetdata()
        CURRENT_DRAFT_PLAYER_MAX = len(testentry)

        #print(testentry)
        # await ctx.send("```<내전 내 주장 제도 임시용>\n"
        #               "해당 기능은 내전 내 주장 제도를 시범운영 함에 있어 조금이나마 빠른 진행이 되는데 도움이 되고자 만들었습니다.\n"
        #               "포지션 선택 시 자동으로 팀에 배정되는 것이 아닌 각 포지션마다 선택한 인원들을 자동으로 정리해서 글로 출력해줍니다.```")
        posli = ["<:ST:706530008465932299>", "<:LW:706530007937450036>", "<:RW:706530008201560156>",
                 "<:CM:706530007928930386>", "<:CDM:911666257219166248>", "<:LB:706530008369463359>",
                 "<:CB:706530008113610803>", "<:RB:706530008100765707>", "<:GK:706530008088182786>"]
        num = int(num)
        if num == 2 :
            self.editSwitchTwo()
            currectNum = True
        elif num == 3 :
            self.editSwitchThree()
            currectNum = True
        elif num == 4 :
            self.editSwitchFour()
            print(self.DraftSwitchFour)
            currectNum = True
        else :
            currectNum = False

        await ctx.message.delete()
        if SWITCH_STOP_DRAFT:
            if currectNum :
                while switchLoop :    # 주장의 수가 입력된 팀 개수를 충족할 때까지 반복문 실행
                    testentry.clear()
                    print(testentry)
                    cap_choice = await ctx.send("주장 지원자는 선택해주세요")
                    await cap_choice.add_reaction('⭕')
                    count = await ctx.send("카운트 다운")
                    for i in range(0, CAP_TIME) :
                        j = CAP_TIME - i
                        await count.edit(content=f"{j}초 남았습니다.")
                        time.sleep(1)
                        if j == 1 :
                            await count.edit(content=f"선택 종료")
                            if self.DraftSwitchTwo :
                                if len(captainmention) < 2 :
                                    await ctx.send("```내전 주장 지원자가 부족합니다.\n"
                                                   "다시 주장 선발이 진행됩니다.```")
                                else :
                                    switchToDraft = True
                                    print('a')
                                    switchLoop = False
                            elif self.DraftSwitchThree :
                                if len(captainmention) < 3 :
                                    await ctx.send("```내전 주장 지원자가 부족합니다.\n"
                                                   "다시 주장 선발이 진행됩니다.```")
                                else :
                                    switchToDraft = True
                                    switchLoop = False
                            elif self.DraftSwitchFour :
                                if len(captainmention) < 4 :
                                    await ctx.send("```내전 주장 지원자가 부족합니다.\n"
                                                   "다시 주장 선발이 진행됩니다.```")
                                else :
                                    switchToDraft = True
                                    switchLoop = False
            else:
                await ctx.send("```다시 입력해주세요.\n"
                               "숫자는 현재 2, 3, 4 만 가능합니다.```")

        # 주장 선발
        for i in range(len(captainmention)):
            temp = random.randint(1, 100)
            time.sleep(0.2)
            print(temp)
            tempNumList.append(temp)

        tempNumList2 = tempNumList.copy()

        print(self.DraftSwitchTwo)
        print(self.DraftSwitchThree)
        print(self.DraftSwitchFour)
        print(tempNumList)
        print(captainmention)

        for i in range(len(captainmention)):
            await ctx.send(content=f"{captainmention[i].mention} - {tempNumList[i]}")

        if self.DraftSwitchTwo :
            FirstNum = max(tempNumList)
            tempNumList.remove(FirstNum)
            SecondNum = max(tempNumList)
            tempNumList.remove(SecondNum)
            for i in range(len(captainmention)):
                if FirstNum == tempNumList2[i]:
                    TeamA.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {FirstNum}")
            for i in range(len(captainmention)):
                if SecondNum == tempNumList2[i]:
                    TeamB.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {SecondNum}")
            await ctx.send(content=f"A팀 주장 : {TeamA.getCapData().mention},\n"
                                   f"B팀 주장 : {TeamB.getCapData().mention}")
        elif self.DraftSwitchThree :
            FirstNum = max(tempNumList)
            tempNumList.remove(FirstNum)
            SecondNum = max(tempNumList)
            tempNumList.remove(SecondNum)
            ThirdNum = max(tempNumList)
            tempNumList.remove(ThirdNum)
            for i in range(len(captainmention)):
                if FirstNum == tempNumList2[i]:
                    TeamA.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {FirstNum}")
            for i in range(len(captainmention)):
                if SecondNum == tempNumList2[i]:
                    TeamB.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {SecondNum}")
            for i in range(len(captainmention)):
                if ThirdNum == tempNumList2[i]:
                    TeamC.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {ThirdNum}")
            await ctx.send(content=f"A팀 주장 : {TeamA.getCapData().mention},\n"
                                   f"B팀 주장 : {TeamB.getCapData().mention},\n"
                                   f"C팀 주장 : {TeamC.getCapData().mention}")
        elif self.DraftSwitchFour :
            FirstNum = max(tempNumList)
            tempNumList.remove(FirstNum)
            SecondNum = max(tempNumList)
            tempNumList.remove(SecondNum)
            ThirdNum = max(tempNumList)
            tempNumList.remove(ThirdNum)
            FourthNum = max(tempNumList)
            tempNumList.remove(FourthNum)
            for i in range(len(captainmention)):
                if FirstNum == tempNumList2[i]:
                    TeamA.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {FirstNum}")

            for i in range(len(captainmention)):
                if SecondNum == tempNumList2[i]:
                    TeamB.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {SecondNum}")
            for i in range(len(captainmention)):
                if ThirdNum == tempNumList2[i]:
                    TeamC.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {ThirdNum}")

            for i in range(len(captainmention)):
                if FourthNum == tempNumList2[i]:
                    TeamD.setCapData(captainmention[i])
                    await ctx.send(content=f"{captainmention[i].mention} - {FourthNum}")
            await ctx.send(content=f"A팀 주장 : {TeamA.getCapData().mention},\n"
                                   f"B팀 주장 : {TeamB.getCapData().mention},\n"
                                   f"C팀 주장 : {TeamC.getCapData().mention},\n"
                                   f"D팀 주장 : {TeamD.getCapData().mention}")

        # 드래프트 진행
        if switchToDraft:
            posli = ["<:ST:706530008465932299>", "<:LW:706530007937450036>", "<:RW:706530008201560156>",
                     "<:CM:706530007928930386>", "<:CDM:911666257219166248>", "<:LB:706530008369463359>",
                     "<:CB:706530008113610803>", "<:RB:706530008100765707>", "<:GK:706530008088182786>"]

            draft = await ctx.send("포지션을 선택해주세요")
            for pos in posli :
                await draft.add_reaction(pos)

            cd = await ctx.send("카운트 다운")
            for i in range(0, DRAFT_TIME):
                j = DRAFT_TIME - i
                await cd.edit(content=f"{j}초 남았습니다. 누른 사람 : {len(testentry)}명")
                time.sleep(1)
                if j == 1 :
                    await cd.edit(content=f"선택 종료, 누른 사람 : {len(testentry)}명")
                    # 테스트 출력 ------------------------------------------------
                    #await ctx.send("```해당 기능은 내전 내 주장 제도를 시범운영 함에 있어 조금이나마 빠른 진행이 되는데 도움이 되고자 만들었습니다.\n"
                    #               "포지션 선택 시 자동으로 팀에 배정되는 것이 아닌 각 포지션마다 선택한 인원들을 자동으로 정리해서 글로 출력해줍니다.```")
                    left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(cb) + len(rb) + len(gk)
                    await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")

            await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                   f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                   f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                   f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
            await ctx.send(content=f"A팀 주장이신 {TeamA.getCapData().mention} 님은\n"
                                   f"'%선택 @멘션' 명령어를 사용해 선발해주세요.")

    @commands.command(name='선택', aliases=["select"], pass_context=True)
    async def _선택(self, ctx, member: discord.Member):
        global CURRENT_DRAFT_COUNT
        global CURRENT_DRAFT_PLAYER_MAX
        print(testentry)
        for name in testentry:
            print(name)
        print(member.display_name)
        NAEJEON_TEAM_A_ID = get(ctx.guild.text_channels, name=config.NAEJEON_TEAM_A)
        NAEJEON_TEAM_B_ID = get(ctx.guild.text_channels, name=config.NAEJEON_TEAM_B)
        NAEJEON_TEAM_C_ID = get(ctx.guild.text_channels, name=config.NAEJEON_TEAM_C)
        NAEJEON_TEAM_D_ID = get(ctx.guild.text_channels, name=config.NAEJEON_TEAM_D)

        if self.DraftSwitchTwo:                       # 2팀일 때
            if CURRENT_DRAFT_COUNT % 2 == 0:          # A팀 차례
                if ctx.author.id == TeamA.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamA.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"B팀 주장이신 {TeamB.getCapData().mention} 님은\n"
                                               f"'%선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_A_ID.send(content=f"{member.mention} 님은 A팀 배정되었습니다.")

                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamA.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 2 == 1:        # B팀 차례
                if ctx.author.id == TeamB.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamB.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"A팀 주장이신 {TeamA.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_B_ID.send(content=f"{member.mention} 님은 B팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamB.getCapData().mention} 차례입니다.")
        elif self.DraftSwitchThree:                   # 3팀일 때
            if CURRENT_DRAFT_COUNT % 3 == 0:          # A팀 차례
                if ctx.author.id == TeamA.getCapData().id:
                    if member.display_name in testentry :
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamA.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"B팀 주장이신 {TeamB.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_A_ID.send(content=f"{member.mention} 님은 A팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamA.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 3 == 1:        # B팀 차례
                if ctx.author.id == TeamB.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamB.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"C팀 주장이신 {TeamC.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                        await NAEJEON_TEAM_B_ID.send(content=f"{member.mention} 님은 B팀 배정되었습니다.")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamB.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 3 == 2:        # C팀 차례
                if ctx.author.id == TeamC.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamC.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"A팀 주장이신 {TeamA.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_C_ID.send(content=f"{member.mention} 님은 C팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamC.getCapData().mention} 차례입니다.")

        elif self.DraftSwitchFour:                    # 4팀일 때
            if CURRENT_DRAFT_COUNT % 4 == 0:          # A팀 차례
                if ctx.author.id == TeamA.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamA.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"B팀 주장이신 {TeamB.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_A_ID.send(content=f"{member.mention} 님은 A팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamA.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 4 == 1:        # B팀 차례
                if ctx.author.id == TeamB.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamB.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"C팀 주장이신 {TeamC.getCapData().mention} 님은\n"
                                               f"'$선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_B_ID.send(content=f"{member.mention} 님은 B팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamB.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 4 == 2:        # C팀 차례
                if ctx.author.id == TeamC.getCapData().id:
                    if member.display_name in testentry :
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamC.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"D팀 주장이신 {TeamD.getCapData().mention} 님은\n"
                                               f"'%선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_C_ID.send(content=f"{member.mention} 님은 C팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamC.getCapData().mention} 차례입니다.")
            elif CURRENT_DRAFT_COUNT % 4 == 3:        # D팀 차례
                if ctx.author.id == TeamD.getCapData().id:
                    if member.display_name in testentry:
                        CURRENT_DRAFT_COUNT += 1
                        print(CURRENT_DRAFT_COUNT)
                        TeamD.setTeamData(member.mention)
                        testentry.remove(member.display_name)
                        self.deleteNameFromPositonList(member.display_name)
                        left_count = len(st) + len(lw) + len(rw) + len(cam) + len(cm) + len(cdm) + len(lb) + len(
                            cb) + len(rb) + len(gk)
                        await ctx.send(content=f"```<포지션 선택 현황>    남은 인원 : {left_count} 명\n\n"
                                               f"ST - {makeListFromList(st)}\n"
                                               f"LW - {makeListFromList(lw)}\n"
                                               f"RW - {makeListFromList(rw)}\n"
                                               f"CAM - {makeListFromList(cam)}\n"
                                               f"CM - {makeListFromList(cm)}\n"
                                               f"CDM - {makeListFromList(cdm)}\n"
                                               f"LB - {makeListFromList(lb)}\n"
                                               f"CB - {makeListFromList(cb)}\n"
                                               f"RB - {makeListFromList(rb)}\n"
                                               f"GK - {makeListFromList(gk)}\n```")
                        await ctx.send(content=f"{config.NAEJEON_TEAM_A} : {TeamA.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_B} : {TeamB.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_C} : {TeamC.getTeamData()}\n"
                                               f"{config.NAEJEON_TEAM_D} : {TeamD.getTeamData()}")
                        await ctx.send(content=f"A팀 주장이신 {TeamA.getCapData().mention} 님은\n"
                                               f"'%선택 @멘션' 명령어를 사용해 선발해주세요.")
                        await NAEJEON_TEAM_D_ID.send(content=f"{member.mention} 님은 D팀 배정되었습니다.")
                    else:
                        await ctx.send("```잘못 입력하였습니다. 다시 입력해주세요.```")
                else:
                    await ctx.send(content=f"올바르지 않은 순서입니다.\n"
                                           f"현재 {TeamD.getCapData().mention} 차례입니다.")

    @commands.Cog.listener()
    async def on_ready(self) :
        DiscordComponents(self.bot)

    @commands.command(name='버튼', pass_context=True)
    async def 버튼(self, ctx) :
        switch = True
        button = Button(label='ST', style=ButtonType().Danger)
        await ctx.send("grabbing a click...", components=[self.buttonST])

        async def check(button_ctx) :
            if int(button_ctx.author.user.id) == int(ctx.author.user.id):
                return True
            await ctx.send("I wasn't asking you!", ephemeral=True)
            return False

        while switch:
            res = await self.bot.wait_for('button_for')
            response = res.component.label
            if res.channel is not ctx.channel:
                return
            if res.channel == ctx.channel:
                if res.component.label == 'ST' or res.component.custom_id == 'st':
                    print('a')

        '''await ctx.send("버튼 테스트", components=[
            [Button(label='ST', style="3", custom_id="st"), Button(label='LW', style=4, custom_id='lw')]
        ])
        async def button_callback(interaction):
            await interaction.reponse.send("ST누름")

        int = await self.bot.wait_for("button_click")
        print(int)
        print(int.component.label)
        if int.component.label =='st':
            await int.respond("ST 누름")'''
        '''
        view = View()
        for pos in self.button_li:
            view.add_item(item=pos)
        await ctx.send("테스트", view=view)'''
        '''
        B_ST = Button(style=ButtonStyle.red, label='ST', custom_id='st')
        B_LW = Button(style=ButtonStyle.red, label='LW', custom_id='lw')
        B_RW = Button(style=ButtonStyle.red, label='RW', custom_id='rw')

        await ctx.send("테스트", component=[
                [B_ST, B_LW, B_RW]
            ]
        )

        interaction = await self.bot.wait_for("button_click")
        if interaction.id == 'st':
            await ctx.send("ST 누름")'''

    #    @commands.Cog.listener()
    #    async def on_button_click(self, interaction) :
    #        await interaction.respond(content=f"you clicked button {interaction.component.custom_id}")

    @commands.command(name='전술등록', pass_context=True)
    async def _임시주장11(self, ctx, *, text) :
        idnum = ctx.author.id
        name = myfun.getNickFromDisplayname(ctx)

        temp = text.split('"')

        formation = temp[1]
        summary = temp[3]
        detail = temp[5]

        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Nae")
        count = 1
        for row in cur.fetchall():
            if ctx.author.id == row[0]:
                count += 1

        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO Nae VALUES(?, ?, ?, ?, ?, ?)",
                        (idnum, name, count, formation, summary, detail))
            print('a')
            await ctx.send("전술 번호 최초 등록 완료")
            conn.commit()

            print('b')

        finally:
            conn.close()

    '''
    @commands.command(name='전술정보수정', pass_context=True)
    async def _임시주장2(self, ctx, *, text):
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Nae")
        count = 1
        temp = []
        for row in cur.fetchall() :
            if ctx.author.id == row[0]:
                temp.append(row[2], row[3])

        await ctx.send(content=f"{myfun.getNickFromDisplayname(ctx)} 님의 정보를 수정합니다.")
        await ctx.send("수정할 전술 번호를 선택해주세요.")
        for row in temp:
            await ctx.send(content=f"{row[0]}번 : {row[1]}")

        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("UPDASTE Nae SET ")
            conn.commit()

        except:
            print('b')

        finally:
            conn.close()'''

    @commands.command(name='전술정보전체목록', pass_context=True)
    async def _임시주장3(self, ctx):
        temp = []
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Nae")
            for row in cur.fetchall():
                temp.append(row)
                print(row)
        finally:
            conn.close()

        for index in temp:
            await ctx.send(content=f"```'{index[1]}' 님의 {index[2]}번 전술\n"
                                   f"포메이션 : {index[3]}\n"
                                   f"간략정보 : {index[4]}\n"
                                   f"상세정보 : \n"
                                   f"{index[5]}```")

    @commands.command(name='전술정보일부확인', pass_context=True)
    async def _임시주장4(self, ctx, member: discord.Member):
        temp = []
        id = member.id
        try:
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Nae WHERE id=?", (id, ))
            for row in cur.fetchall():
                temp.append(row)

            if not len(temp) == 0:
                for index in temp :
                    await ctx.send(content=f"```'{index[1]}' 님의 {index[2]}번 전술\n"
                                           f"포메이션 : {index[3]}\n"
                                           f"간략정보 : {index[4]}\n"
                                           f"상세정보 : \n"
                                           f"{index[5]}```")
            else:
                await ctx.send(content=f"```해당 유저의 등록된 전술 정보가 없습니다.```")

        except:
            pass

        finally:
            conn.close()

    @commands.command(name='전술정보드래프트', pass_context=True)
    async def _전술정보드래프트(self, ctx):
        captainID.clear()
        temp = []

        cap_choice = await ctx.send("주장 지원자는 선택해주세요")
        await cap_choice.add_reaction('⭕')
        count = await ctx.send("카운트 다운")
        #for i in range(0, CAP_TIME) :
        for i in range(0, 5) :
            j = 5 - i
            await count.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)

        #print(captainID)
        #for i in range(len(captainID)):
        #    await ctx.send(content=f"{captainmention[i]} - {captainID[i]}")

        # -------------------------------------
        # 전술 등록 여부 조회
        # -------------------------------------
        print(captainID)
        for ids in captainID:
            temp.clear()
            conn = sqlite3.connect("CEF.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Nae WHERE id=?", (ids, ))
            for row in cur.fetchall():
                temp.append(row)

            if not len(temp) == 0:
                for index in temp:
                    await ctx.send(content=f"```'{index[1]}' 님의 {index[2]}번 전술\n"
                                           f"포메이션 : {index[3]}\n"
                                           f"간략정보 : {index[4]}\n"
                                           f"```")



    @commands.command(name='임베드', pass_context=True)
    async def 임베드(self, ctx) :
        embed = discord.Embed(title=f"드래프트 현황", description=f"{ctx.author.display_name} 님의 정보창", color=0xFF007F)
        embed.add_field(name="ST", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name="LW", value="text", inline=True)
        embed.add_field(name="RW", value="text", inline=True)
        embed.add_field(name="CAM", value="text", inline=True)
        embed.add_field(name="CM", value="text", inline=True)
        embed.add_field(name="CDM", value="text", inline=True)
        embed.add_field(name="LB", value="text", inline=True)
        embed.add_field(name="CB", value="text", inline=True)
        embed.add_field(name="RB", value="text", inline=True)
        embed.add_field(name="GK", value="text", inline=True)
        embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

        await ctx.send(embed=embed)


    @commands.command(name='주장', aliases=["임시주장"], pass_context=True)
    async def 주장(self, ctx):
        global TeamA
        global TeamB
        global CURRENT_DRAFT_COUNT
        global switch
        CURRENT_DRAFT_COUNT = 2
        CURRENT_DRAFT_PLAYER = 22
        switch = 0
        entry.clear()
        st.clear()
        lw.clear()
        rw.clear()
        cam.clear()
        cm.clear()
        cdm.clear()
        lb.clear()
        cb.clear()
        rb.clear()
        gk.clear()

        await ctx.send("내전 주장 제도 임시용")
        posli = ["<:ST:706530008465932299>", "<:LW:706530007937450036>", "<:RW:706530008201560156>",
                 "<:CM:706530007928930386>", "<:CDM:911666257219166248>", "<:LB:706530008369463359>",
                 "<:CB:706530008113610803>", "<:RB:706530008100765707>", "<:GK:706530008088182786>"]

        draft = await ctx.send("포지션을 선택해주세요")
        for pos in posli:
            await draft.add_reaction(pos)

        cd = await ctx.send("카운트 다운")
        for i in range(0, DRAFT_TIME) :
            j = DRAFT_TIME - i
            await cd.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)
            if j == 1 :
                await cd.edit(content="선택 종료")
                # 테스트 출력 ------------------------------------------------
                await ctx.send("```해당 기능은 내전 내 주장 제도를 시범운영 함에 있어 조금이나마 빠른 진행이 되는데 도움이 되고자 만들었습니다.\n"
                               "포지션 선택 시 자동으로 팀에 배정되는 것이 아닌 각 포지션마다 선택한 인원들을 자동으로 정리해서 글로 출력해줍니다.```")
                await ctx.send(content=f"```<포지션 선택 현황>\n\n"
                                       f"ST - {makeListFromList(st)}\n"
                                       f"LW - {makeListFromList(lw)}\n"
                                       f"RW - {makeListFromList(rw)}\n"
                                       f"CAM - {makeListFromList(cam)}\n"
                                       f"CM - {makeListFromList(cm)}\n"
                                       f"CDM - {makeListFromList(cdm)}\n"
                                       f"LB - {makeListFromList(lb)}\n"
                                       f"CB - {makeListFromList(cb)}\n"
                                       f"RB - {makeListFromList(rb)}\n"
                                       f"GK - {makeListFromList(gk)}\n```")
                #await ctx.send("```전달사항 : 위의 현황을 복사 붙여넣기 해서 지우는 방식으로 하시면 조금이나마 빠르게 진행할 듯 합니다.```")

    @commands.command(name='개발', aliases=["주장개발"], pass_context=True)
    async def 주장개발중(self, ctx) :
        global TeamA
        global TeamB
        global CURRENT_DRAFT_COUNT
        CURRENT_DRAFT_COUNT = 2
        CURRENT_DRAFT_PLAYER = 22

        entry.clear()
        captainmention.clear()
        st.clear()
        lw.clear()
        rw.clear()
        cam.clear()
        cm.clear()
        cdm.clear()
        lb.clear()
        cb.clear()
        rb.clear()
        gk.clear()
        cap = 'cap'

        await ctx.send("```내전 주장 제도 테스트용```")
        tpli = ["<:ST:706530008465932299>", "<:LW:706530007937450036>", "<:RW:706530008201560156>",
                "<:CM:706530007928930386>", "<:CDM:911666257219166248>", "<:LB:706530008369463359>",
                "<:CB:706530008113610803>", "<:RB:706530008100765707>", "<:GK:706530008088182786>"]

        cap_choice = await ctx.send("주장 지원자는 선택해주세요")
        await cap_choice.add_reaction('⭕')
        count = await ctx.send("카운트 다운")
        for i in range(0, CAP_TIME) :
            j = CAP_TIME - i
            await count.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)
            if j == 1 :
                await count.edit(content=f"선택 종료")
                print(len(captainmention))
                print(captainmention)
                if len(captainmention) < 2 :
                    await ctx.send("내전 주장 지원자가 부족합니다.\n"
                                   "다시 드래프트를 실행해주세요.")
                else :
                    # 주장 선발
                    selected_captain1 = random.choice(captainmention)
                    captainmention.remove(selected_captain1)
                    selected_captain2 = random.choice(captainmention)
                    await ctx.send(content=f"A팀 주장 - {selected_captain1}\n"
                                           f"B팀 주장 - {selected_captain2}")
                    TeamA.setData('cap', selected_captain1)
                    # TeamB.setData('cap', selected_captain2)

                    draft = await ctx.send("포지션을 선택해주세요")
                    for s in tpli :
                        await draft.add_reaction(s)

                    cd = await ctx.send("카운트 다운")
                    for i in range(0, DRAFT_TIME) :
                        j = DRAFT_TIME - i
                        await cd.edit(content=f"{j}초 남았습니다.")
                        time.sleep(1)
                        if j == 1 :
                            await cd.edit(content="선택 종료")
                            print(len(gk))
                            # 테스트 출력 ------------------------------------------------
                            await ctx.send(entry)
                            embed = discord.Embed(title=f"드래프트 현황", color=0xFF007F)
                            embed.add_field(name="ST", value=f"{ForEmbedFromList(st)}", inline=True)
                            embed.add_field(name="LW", value=f"{ForEmbedFromList(lw)}", inline=True)
                            embed.add_field(name="RW", value=f"{ForEmbedFromList(rw)}", inline=True)
                            embed.add_field(name="CAM", value=f"{ForEmbedFromList(cam)}", inline=True)
                            embed.add_field(name="CM", value=f"{ForEmbedFromList(cm)}", inline=True)
                            embed.add_field(name="CDM", value=f"{ForEmbedFromList(cdm)}", inline=True)
                            embed.add_field(name="LB", value=f"{ForEmbedFromList(lb)}", inline=True)
                            embed.add_field(name="CB", value=f"{ForEmbedFromList(cb)}", inline=True)
                            embed.add_field(name="RB", value=f"{ForEmbedFromList(rb)}", inline=True)
                            embed.add_field(name="GK", value=f"{ForEmbedFromList(gk)}", inline=True)
                            embed.set_footer(text="Copyright ⓒ 2020-2021 타임제이(TimeJ) in C.E.F All Right Reserved.")

                            await ctx.send(embed=embed)
                            '''
                            await ctx.send(content=f"포지션 선택 현황"
                                                   f"ST - {makeListFromList(st)}\n"
                                                   f"LW - {makeListFromList(lw)}\n"
                                                   f"RW - {makeListFromList(rw)}\n"
                                                   f"CAM - {makeListFromList(cam)}\n"
                                                   f"CM - {makeListFromList(cm)}\n"
                                                   f"CDM - {makeListFromList(cdm)}\n"
                                                   f"LB - {makeListFromList(lb)}\n"
                                                   f"CB - {makeListFromList(cb)}\n"
                                                   f"RB - {makeListFromList(rb)}\n"
                                                   f"GK - {makeListFromList(gk)}\n")'''
                            # ---------------------------------------------------------
                            # await ctx.send(content=f"{TeamA.getData('cap')} 님은 팀원을 선택해주세요.\n"
                            #                       f"%선발 @멘션 으로 선택해주세요.")

                            # 버튼 만들기
                            await ctx.send(content="포지션을 선택하세요.",
                                           channel=ctx.channel.id,
                                           components=[self.button_li])


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user) :
        global switch
        if str(reaction.emoji) == '⭕' :
            if user.bot :
                return None
            if not user in captainmention:
                captainmention.append(user)
                captainID.append(user.id)
                print(user.display_name)

        for i in range(0, len(entry)) :
            if user.mention in entry[i] :
                switch = 1
                break
            else :
                switch = 0

        # 드래프트용 (임시용)
        if switch == 0 :  # 스위치가 꺼져있으면
            if user.bot == 1 :  # 봇이면 패스
                return None
            if str(reaction.emoji) == "<:ST:706530008465932299>" :
                entry.append(user.mention)
                # st.append(user.mention)
                st.append(user.display_name)
                testst.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:LW:706530007937450036>" :
                entry.append(user.mention)
                # lw.append(user.mention)
                lw.append(user.display_name)
                testlw.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:RW:706530008201560156>" :
                entry.append(user.mention)
                # rw.append(user.mention)
                rw.append(user.display_name)
                testrw.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:CAM:706530008243634176>" :
                entry.append(user.mention)
                # cam.append(user.mention)
                cam.append(user.display_name)
                testcam.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:CM:706530007928930386>" :
                entry.append(user.mention)
                # cm.append(user.mention)
                cm.append(user.display_name)
                testcm.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:CDM:911666257219166248>" :
                entry.append(user.mention)
                # cdm.append(user.mention)
                cdm.append(user.display_name)
                testcdm.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:LB:706530008369463359>" :
                entry.append(user.mention)
                # lb.append(user.mention)
                lb.append(user.display_name)
                testlb.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:CB:706530008113610803>" :
                entry.append(user.mention)
                # cb.append(user.mention)
                cb.append(user.display_name)
                testcb.append(user)
                testentry.append(user.display_name)
            if str(reaction.emoji) == "<:RB:706530008100765707>" :
                entry.append(user.mention)
                # rb.append(user.mention)
                rb.append(user.display_name)
                testrb.append(user)
                testentry.append(user)
            if str(reaction.emoji) == "<:GK:706530008088182786>" :
                entry.append(user.mention)
                # gk.append(user.mention)
                gk.append(user.display_name)
                testgk.append(user)
                testentry.append(user.display_name)


'''
        # 드래프트용 (개발용)
        if switch == 0 :  # 스위치가 꺼져있으면
            if user.bot == 1 :  # 봇이면 패스
                return None
            if str(reaction.emoji) == "<:ST:706530008465932299>" :
                entry.append(user.mention)
                st.append(user.mention)
            if str(reaction.emoji) == "<:LW:706530007937450036>" :
                entry.append(user.mention)
                lw.append(user.mention)
            if str(reaction.emoji) == "<:RW:706530008201560156>" :
                entry.append(user.mention)
                rw.append(user.mention)
            if str(reaction.emoji) == "<:CAM:706530008243634176>" :
                entry.append(user.mention)
                cam.append(user.mention)
            if str(reaction.emoji) == "<:CM:706530007928930386>" :
                entry.append(user.mention)
                cm.append(user.mention)
            if str(reaction.emoji) == "<:CDM:911666257219166248>" :
                entry.append(user.mention)
                cdm.append(user.mention)
            if str(reaction.emoji) == "<:LB:706530008369463359>" :
                entry.append(user.mention)
                lb.append(user.mention)
            if str(reaction.emoji) == "<:CB:706530008113610803>" :
                entry.append(user.mention)
                cb.append(user.mention)
            if str(reaction.emoji) == "<:RB:706530008100765707>" :
                entry.append(user.mention)
                rb.append(user.mention)
            if str(reaction.emoji) == "<:GK:706530008088182786>" :
                entry.append(user.mention)
                gk.append(user.mention)
'''



