import discord
import asyncio
import time
import random
import os
from discord.ext import commands
from discord.utils import get

MAX_COUNT = 20
DRAFT_COUNT = 5
DELETE_AMOUNT = 2
BOT_SLEEP_TIME = 2
TEAM_A_COLOR = "빨강"
TEAM_B_COLOR = "노랑"
TEAM_C_COLOR = "검정"
TEAM_D_COLOR = "하양"

dice = 0
pin = 0
switch = 0
check = 0
entry = [""]
no_entry = [""]  #멘션 x
queue = []
st = []
lw = []
rw = []
cam = []
cm = []
cdm = []
lb = []
cb = []
rb = []
gk = []
wait_st = []
wait_lw = []
wait_rw = []
wait_cam = []
wait_cm = []
wait_cdm = []
wait_lb = []
wait_cb = []
wait_rb = []
wait_gk = []
a_queue = [0,0,0,0,0,0,0,0,0,0]
b_queue = [0,0,0,0,0,0,0,0,0,0]
c_queue = [0,0,0,0,0,0,0,0,0,0]
d_queue = [0,0,0,0,0,0,0,0,0,0]
a_team = []
b_team = []
c_team = []
d_team = []
wait_mem = [""]
wait_temp = []
form = [""]
position_num = [0,0,0,0,0,0,0,0,0,0]
team_list = [""]

class Draft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 테스트2(self, ctx):
        entry.clear()
        entry.append("")
        queue.clear()
        queue.append("")
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
        a_team.clear()
        b_team.clear()

        form = ["3-5-2", "3-4-3 플랫", "4-4-2 플랫", "4-2-3-1 넓게", "4-3-3 홀딩", "3-4-3 다이아몬드"
                ]


        await ctx.send(content=f"```cs\n"
                            f"포메이션 후보 : \n"
                            f"'3-5-2', '3-4-3 플랫', '3-4-3 다이아몬드',\n"
                            f"'4-4-2 플랫', '4-2-3-1 넓게', '4-3-3 홀딩', '4-1-2-1-2 좁게',\n"
                            f"'5-3-2'```")


        cd = await ctx.send("포메이션을 랜덤으로 뽑습니다")
        time.sleep(1)
        for i in range(0, 3):
            j = 3 - i
            await cd.edit(content=f"카운트다운 : {j}초")
            time.sleep(1)
            if j == 1:
                a_team_form = random.choice(form)
                b_team_form = random.choice(form)
                team_list.append(a_team_form)
                team_list.append(b_team_form)

        await ctx.send(content=f"```A팀 포메이션 : {a_team_form}\n```")
        if a_team_form == "4-3-3 홀딩":
            await ctx.send("```LW       ST      RW\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-2-1, 4-3-3 플랫, 4-5-1 플랫, 4-5-1 공격, 4-3-3 가짜 공격수```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-5-2": #윙백은 풀백으로 처리
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "유사한 포메이션 : \n"
                        "3-4-1-2, 5-3-2, 5-2-1-2```")
            a_queue[0] = 2
            a_queue[3] = 1
            a_queue[5] = 2
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
            await ctx.send("```LW       ST      RW\n"
                        "LM   LCM   RCM   RM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "3-4-2-1, 5-4-1 플랫, 5-2-2-1```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1


        elif a_team_form == "4-4-2 플랫":
            await ctx.send("```.    ST     ST\n"
                        "LM   LCM   RCM   RM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                        "4-2-2-2, 4-4-2, 4-4-2 홀딩, 4-2-4```")
            a_queue[0] = 2
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1


        elif a_team_form == "4-2-3-1 넓게":
            await ctx.send("```.        ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                        "4-2-3-1 좁게, 4-3-3 공격, 4-4-3 수비, 4-4-1-1 공격, 4-4-1-1 미드필드```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 1
            a_queue[5] = 2
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-4-3 다이아몬드":
            await ctx.send("```LW       ST      RW\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "        CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "5-4-1 다이아몬드```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 1
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "5-3-2":
            await ctx.send("```.    ST     ST\n"
                        "    CM   CM   CM\n"
                        "LWB             RWB\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "3-1-4-2 다이아몬드```")
            a_queue[0] = 2
            a_queue[4] = 3
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1


        elif a_team_form == "4-1-2-1-2 좁게":
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-1-2```")
            a_queue[0] = 2
            a_queue[3] = 1
            a_queue[4] = 1
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 1
            a_queue[8] = 1
            a_queue[9] = 1


        # B팀 큐 생성------------------------------------------
        await ctx.send(content=f"```B팀 포메이션 : {b_team_form}\n```")
        if b_team_form == "4-3-3 홀딩":
            await ctx.send("```LW       ST      RW\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-2-1, 4-3-3 플랫, 4-5-1 플랫, 4-5-1 공격, 4-3-3 가짜 공격수```")
            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[4] = 2
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "3-5-2": #윙백은 풀백으로 처리
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "유사한 포메이션 : \n"
                        "3-4-1-2, 5-3-2, 5-2-1-2```")
            b_queue[0] = 2
            b_queue[3] = 1
            b_queue[5] = 2
            b_queue[6] = 1
            b_queue[7] = 3
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
            await ctx.send("```LW       ST      RW\n"
                        "LM   LCM   RCM   RM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "3-4-2-1, 5-4-1 플랫, 5-2-2-1```")
            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[4] = 2
            b_queue[6] = 1
            b_queue[7] = 3
            b_queue[8] = 1
            b_queue[9] = 1


        elif b_team_form == "4-4-2 플랫": # LM, RM은 LW, RW으로 처리
            await ctx.send("```.    ST     ST\n"
                        "LM   LCM   RCM   RM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-2-2-2, 4-4-2, 4-4-2 홀딩, 4-2-4```")
            b_queue[0] = 2
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[4] = 2
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "4-2-3-1 넓게":
            await ctx.send("```.        ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                        "4-2-3-1 좁게, 4-3-3 공격, 4-4-3 수비, 4-4-1-1 공격, 4-4-1-1 미드필드```")
            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[3] = 1
            b_queue[5] = 2
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "3-4-3 다이아몬드":
            await ctx.send("```LW       ST      RW\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "        CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "5-4-1 다이아몬드```")
            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[3] = 1
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 3
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "5-3-2": # 윙백은 풀백으로 처리
            await ctx.send("```.    ST     ST\n"
                        "    CM   CM   CM\n"
                        "LWB             RWB\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "3-1-4-2 다이아몬드```")
            b_queue[0] = 2
            b_queue[4] = 3
            b_queue[6] = 1
            b_queue[7] = 3
            b_queue[8] = 1
            b_queue[9] = 1

        elif b_team_form == "4-1-2-1-2 좁게":
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-1-2```")
            b_queue[0] = 2
            b_queue[3] = 1
            b_queue[4] = 1
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 1
            b_queue[8] = 1
            b_queue[9] = 1

        st_queue = a_queue[0] + b_queue[0]
        lw_queue = a_queue[1] + b_queue[1]
        rw_queue = a_queue[2] + b_queue[2]
        cam_queue = a_queue[3] + b_queue[3]
        cm_queue = a_queue[4] + b_queue[4]
        cdm_queue = a_queue[5] + b_queue[5]
        lb_queue = a_queue[6] + b_queue[6]
        cb_queue = a_queue[7] + b_queue[7]
        rb_queue = a_queue[8] + b_queue[8]
        gk_queue = a_queue[9] + b_queue[9]


        position_num[0] = st_queue
        position_num[1] = lw_queue
        position_num[2] = rw_queue
        position_num[3] = cam_queue
        position_num[4] = cm_queue
        position_num[5] = cdm_queue
        position_num[6] = lb_queue
        position_num[7] = cb_queue
        position_num[8] = rb_queue
        position_num[9] = gk_queue


        await ctx.send(content=f"```포지션별 인원 제한은 다음과 같습니다.\n"
                            f"ST : {st_queue}\n"
                            f"LW : {lw_queue}\n"
                            f"RW : {rw_queue}\n"
                            f"CAM : {cam_queue}\n"
                            f"CM : {cm_queue}\n"
                            f"CDM : {cdm_queue}\n"
                            f"LB : {lb_queue}\n"
                            f"CB : {cb_queue}\n"
                            f"RB : {rb_queue}\n"
                            f"GK : {gk_queue}\n```")
        if a_team_form == "4-5-1 공격" or a_team_form == "4-4-2 플랫" or b_team_form == "4-5-1 공격" or b_team_form == "4-4-2 플랫":
            await ctx.send("```cs\n"
                        "'4-5-1 공격', '4-2-3-1 넓게', '4-4-2 플랫', '4-1-2-1-2 좁게' 포메이션의 경우,\n"
                        "LM, RM은 LW, RW을 누르세요```")
        if a_team_form == "5-3-2" or a_team_form == "3-5-2" or a_team_form == "3-4-3 플랫" or b_team_form == "5-3-2" or b_team_form == "3-5-2" or b_team_form == "3-4-3 플랫":
            await ctx.send("```cs\n"
                        "'3-5-2', '3-4-3', '5-3-2' 포메이션의 경우,\n"
                        "LM, LWB, RM, RWB는 LB, RB를 누르세요```")

        draft = await ctx.send("희망하는 포지션을 선택해주세요.")
        if st_queue > 0:
            await draft.add_reaction("<:ST:706530008465932299>")
        if lw_queue > 0:
            await draft.add_reaction("<:LW:706530007937450036>")
        if rw_queue > 0:
            await draft.add_reaction("<:RW:706530008201560156>")
        if cam_queue > 0:
            await draft.add_reaction("<:CAM:706530008243634176>")
        if cm_queue > 0:
            await draft.add_reaction("<:CM:706530007928930386>")
        if cdm_queue > 0:
            await draft.add_reaction("<:CDM:706530008289509466>")
        if lb_queue > 0:
            await draft.add_reaction("<:LB:706530008369463359>")
        if cb_queue > 0:
            await draft.add_reaction("<:CB:706530008113610803>")
        if rb_queue > 0:
            await draft.add_reaction("<:RB:706530008100765707>")
        if gk_queue > 0:
            await draft.add_reaction("<:GK:706530008088182786>")

        cd = await ctx.send("카운트 다운")
        for i in range(0, MAX_COUNT):
            j = MAX_COUNT - i
            await cd.edit(content=f"{j}초 남았습니다. 누른 사람 : {len(entry)-1}명")
            time.sleep(1)
            if j == 1:
                await cd.edit(content=f"선택 종료, 누른 사람 : {len(entry)-1}명")
                for k in range(0, len(entry)):
                    if entry[k].startswith("ST"):
                        st.append(entry[k])
                        print("a")
                    if entry[k].startswith("LW"):
                        lw.append(entry[k])
                        print("a")
                    if entry[k].startswith("RW"):
                        rw.append(entry[k])
                        print("a")
                    if entry[k].startswith("CAM"):
                        cam.append(entry[k])
                        print(cam)
                        print("a")
                    if entry[k].startswith("CM"):
                        cm.append(entry[k])
                        print("a")
                    if entry[k].startswith("CDM"):
                        cdm.append(entry[k])
                        print("a")
                    if entry[k].startswith("LB"):
                        lb.append(entry[k])
                        print("a")
                    if entry[k].startswith("CB"):
                        cb.append(entry[k])
                        print("a")
                    if entry[k].startswith("RB"):
                        rb.append(entry[k])
                        print("a")
                    if entry[k].startswith("GK"):
                        gk.append(entry[k])
                        print("a")
                # ST 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[0] > 0:                  # 만약 A팀의 ST 수가 0보다 크면,
                        for i in range(a_queue[0]):     # A팀 ST 수만큼
                            print(st)
                            temp = random.choice(st)    # 랜덤으로 선발해
                            a_team.append(temp)         # A팀으로 배분 후
                            st.remove(temp)             # ST 리스트에서 제거
                    # B팀
                    if b_queue[0] > 0:
                        for i in range(0, b_queue[0]):
                            temp = random.choice(st)
                            b_team.append(temp)
                            st.remove(temp)
                    # 대기열 정리
                    for j in range(len(st)):
                        queue.append(st[j])
                except:
                    print(a_team)
                    print(b_team)

                # LW 선발 및 대기열 이동
                try:
                    # B팀
                    if b_queue[1] > 0:
                        for i in range(b_queue[1]):
                            temp = random.choice(lw)
                            b_team.append(temp)
                            lw.remove(temp)
                    # A팀
                    if a_queue[1] > 0:
                        for i in range(a_queue[1]):
                            temp = random.choice(lw)
                            a_team.append(temp)
                            lw.remove(temp)
                    # 대기열 정리
                    for j in range(len(lw)):
                        queue.append(lw[j])

                except:
                    print(a_team)
                    print(b_team)

                # RW 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[2] > 0:
                        for i in range(a_queue[2]):
                            temp = random.choice(rw)
                            a_team.append(temp)
                            rw.remove(temp)
                    # B팀
                    if b_queue[2] > 0:
                        for i in range(b_queue[2]):
                            temp = random.choice(rw)
                            b_team.append(temp)
                            rw.remove(temp)
                    for j in range(len(rw)):
                        queue.append(rw[j])
                except:
                    print(a_team)
                    print(b_team)

                # CAM 선발 및 대기열 이동
                try:
                    # B팀
                    print(b_queue[3])
                    print(cam)
                    if b_queue[3] > 0:
                        for i in range(b_queue[3]):
                            temp = random.choice(cam)
                            b_team.append(temp)
                            cam.remove(temp)
                    # A팀
                    if a_queue[3] > 0:
                        for i in range(a_queue[3]):
                            temp = random.choice(cam)
                            a_team.append(temp)
                            cam.remove(temp)

                    for j in range(len(cam)):
                        queue.append(cam[j])
                except:
                    print(a_team)
                    print(b_team)

                # CM 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[4] > 0:
                        for i in range(a_queue[4]):
                            temp = random.choice(cm)
                            a_team.append(temp)
                            cm.remove(temp)
                    # B팀
                    if b_queue[4] > 0:
                        for i in range(b_queue[4]):
                            temp = random.choice(cm)
                            b_team.append(temp)
                            cm.remove(temp)
                    for j in range(len(cm)):
                        queue.append(cm[j])
                except:
                    print(a_team)
                    print(b_team)

                # CDM 선발 및 대기열 이동
                try:
                    # B팀
                    if b_queue[5] > 0:
                        for i in range(b_queue[5]):
                            temp = random.choice(cdm)
                            b_team.append(temp)
                            cdm.remove(temp)
                    # A팀
                    if a_queue[5] > 0:
                        for i in range(a_queue[5]):
                            temp = random.choice(cdm)
                            a_team.append(temp)
                            cdm.remove(temp)

                    for j in range(len(cdm)):
                        queue.append(cdm[j])
                except:
                    print(a_team)
                    print(b_team)

                # LB 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[6] > 0:
                        for i in range(a_queue[6]):
                            temp = random.choice(lb)
                            a_team.append(temp)
                            lb.remove(temp)
                    # B팀
                    if b_queue[6] > 0:
                        for i in range(b_queue[6]):
                            temp = random.choice(lb)
                            b_team.append(temp)
                            lb.remove(temp)
                    for j in range(len(lb)):
                        queue.append(lb[j])
                except:
                    print(a_team)
                    print(b_team)

                # CB 선발 및 대기열 이동
                try:
                    # B팀
                    if b_queue[7] > 0:
                        for i in range(b_queue[7]):
                            temp = random.choice(cb)
                            b_team.append(temp)
                            cb.remove(temp)
                    # A팀
                    if a_queue[7] > 0:
                        for i in range(a_queue[7]):
                            temp = random.choice(cb)
                            a_team.append(temp)
                            cb.remove(temp)

                    for j in range(len(cb)):
                        queue.append(cb[j])
                except:
                    print(a_team)
                    print(b_team)

                # RB 선발 및 대기열 이동
                try:
                    # A팀

                    if a_queue[8] > 0:
                        for i in range(a_queue[8]):
                            temp = random.choice(rb)
                            a_team.append(temp)
                            rb.remove(temp)
                    # B팀
                    if b_queue[8] > 0:
                        for i in range(b_queue[8]):
                            temp = random.choice(rb)
                            b_team.append(temp)
                            rb.remove(temp)
                    for j in range(len(rb)):
                        queue.append(rb[j])
                except:
                    print(a_team)
                    print(b_team)

                # GK 선발 및 대기열 이동
                try:
                    # B팀
                    if b_queue[9] > 0:
                        for i in range(b_queue[9]):
                            temp = random.choice(gk)
                            b_team.append(temp)
                            gk.remove(temp)
                    # A팀
                    if a_queue[9] > 0:
                        for i in range(a_queue[9]):
                            temp = random.choice(gk)
                            a_team.append(temp)
                            gk.remove(temp)

                    for j in range(len(gk)):
                        queue.append(gk[j])
                except:
                    print(a_team)
                    print(b_team)

                # 내전 A팀
                temp_a_team = ""
                for j in range(0, len(a_team) + 1):
                    try:
                        temp_a_team = temp_a_team + " " + a_team[j]
                        if a_team[j].startswith("ST"):
                            if a_team[j + 1].startswith("LW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LW"):
                            if a_team[j + 1].startswith("RW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RW"):
                            if a_team[j + 1].startswith("CAM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CAM"):
                            if a_team[j + 1].startswith("CM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CM"):
                            if a_team[j + 1].startswith("CDM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CDM"):
                            if a_team[j + 1].startswith("LB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LB"):
                            if a_team[j + 1].startswith("CB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CB"):
                            if a_team[j + 1].startswith("RB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RB"):
                            if a_team[j + 1].startswith("GK"):
                                temp_a_team = temp_a_team + "\n\n"
                    except:
                        print(temp_a_team)

                await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)

                # 내전 B팀
                temp_b_team = ""
                for i in range(0, len(b_team) + 1):
                    try:
                        temp_b_team = temp_b_team + " " + b_team[i]
                        if b_team[i].startswith("ST"):
                            if b_team[i + 1].startswith("LW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LW"):
                            if b_team[i + 1].startswith("RW"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("RW"):
                            if b_team[i + 1].startswith("CAM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CAM"):
                            if b_team[i + 1].startswith("CM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CM"):
                            if b_team[i + 1].startswith("CDM"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CDM"):
                            if b_team[i + 1].startswith("LB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("LB"):
                            if b_team[i + 1].startswith("CB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("CB"):
                            if b_team[i + 1].startswith("RB"):
                                temp_b_team = temp_b_team + "\n\n"
                        if b_team[i].startswith("GK"):
                            if b_team[i + 1].startswith("RB", ""):
                                temp_b_team = temp_b_team + "\n\n"
                    except:
                        print(temp_b_team)

                await ctx.send(content=f"\n팀 B({TEAM_B_COLOR}) 명단 :  \n" + temp_b_team)

                temp_w_team = ""
                for i in range(0, len(queue)):
                    try:
                        if queue[i].startswith("ST"):
                            queue[i].replace("ST", "")
                            temp_w_team = temp_w_team + queue[i] + " ST\n"
                        if queue[i].startswith("LW"):
                            queue[i].replace("LW", "")
                            temp_w_team = temp_w_team + queue[i] + " LW\n"
                        if queue[i].startswith("RW"):
                            queue[i].replace("RW", "")
                            temp_w_team = temp_w_team + queue[i] + " RW\n"
                        if queue[i].startswith("CAM"):
                            queue[i].replace("CAM", "")
                            temp_w_team = temp_w_team + queue[i] + " CAM\n"
                        if queue[i].startswith("CM"):
                            queue[i].replace("CM", "")
                            temp_w_team = temp_w_team + queue[i] + " CM\n"
                        if queue[i].startswith("CDM"):
                            queue[i].replace("CDM", "")
                            temp_w_team = temp_w_team + queue[i] + " CDM\n"
                        if queue[i].startswith("LB"):
                            queue[i].replace("LB", "")
                            temp_w_team = temp_w_team + queue[i] + " LB\n"
                        if queue[i].startswith("CB"):
                            queue[i].replace("CB", "")
                            temp_w_team = temp_w_team + queue[i] + " CB\n"
                        if queue[i].startswith("RB"):
                            queue[i].replace("RB", "")
                            temp_w_team = temp_w_team + queue[i] + " RB\n"
                        if queue[i].startswith("GK"):
                            queue[i].replace("GK", "")
                            temp_w_team = temp_w_team + queue[i] + " GK\n"
                    except:
                        pass

                await ctx.send("\n\n대기 \n" + temp_w_team)
                overlap = 0

    #각 팀 포지션 개수, 팀 명단 삭제 안됨

    @commands.command()
    async def 테스트1(self, ctx):
        entry.clear()
        entry.append("")
        queue.clear()
        queue.append("")
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
        a_team.clear()
        b_team.clear()
        a_queue = [0,0,0,0,0,0,0,0,0,0]

        form = ["3-5-2", "3-4-3 플랫", "4-1-2-1-2 좁게", "4-4-2 플랫", "4-2-3-1 넓게",
                "4-3-3 홀딩", "3-4-3 다이아몬드", "5-3-2"]

        await ctx.send(content=f"```cs\n"
                            f"포메이션 후보 : \n"
                            f"'3-5-2', '3-4-3 플랫', '3-4-3 다이아몬드',\n"
                            f"'4-4-2 플랫', '4-2-3-1 넓게', '4-3-3 홀딩', '4-1-2-1-2 좁게',\n"
                            f"'5-3-2'```")

        cd = await ctx.send("포메이션을 랜덤으로 뽑습니다")
        time.sleep(1)
        for i in range(0, 3):
            j = 3 - i
            await cd.edit(content=f"카운트다운 : {j}초")
            time.sleep(1)
            if j == 1:
                a_team_form = random.choice(form)
                b_team_form = random.choice(form)

        await ctx.send(content=f"```포메이션 : {a_team_form}\n```")
        if a_team_form == "4-3-3 홀딩":
            await ctx.send("```LW       ST      RW\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-2-1, 4-3-3 플랫, 4-5-1 플랫, 4-5-1 공격, 4-3-3 가짜 공격수```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-5-2": #윙백은 풀백으로 처리
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "유사한 포메이션 : \n"
                        "3-4-1-2, 5-3-2, 5-2-1-2```")
            a_queue[0] = 2
            a_queue[3] = 1
            a_queue[5] = 2
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
            await ctx.send("```LW       ST      RW\n"
                        "LM   LCM   RCM   RM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "3-4-2-1, 5-4-1 플랫, 5-2-2-1```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "4-4-2 플랫":
            await ctx.send("```.    ST     ST\n"
                        "LM   LCM   RCM   RM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                        "4-2-2-2, 4-4-2, 4-4-2 홀딩, 4-2-4```")
            a_queue[0] = 2
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[4] = 2
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "4-2-3-1 넓게":
            await ctx.send("```.        ST\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "     CDM   CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                        "4-2-3-1 좁게, 4-3-3 공격, 4-4-3 수비, 4-4-1-1 공격, 4-4-1-1 미드필드```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 1
            a_queue[5] = 2
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "3-4-3 다이아몬드":
            await ctx.send("```LW       ST      RW\n"
                        "        CAM\n"
                        "LM               RM\n"
                        "        CDM\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                        "5-4-1 다이아몬드```")
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 1
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1
        elif a_team_form == "5-3-2":
            await ctx.send("```.    ST     ST\n"
                        "    CM   CM   CM\n"
                        "LWB             RWB\n"
                        "   LCB  RCB  RCB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "3-1-4-2 다이아몬드```")
            a_queue[0] = 2
            a_queue[4] = 3
            a_queue[6] = 1
            a_queue[7] = 3
            a_queue[8] = 1
            a_queue[9] = 1

        elif a_team_form == "4-1-2-1-2 좁게":
            await ctx.send("```.    ST     ST\n"
                        "        CAM\n"
                        "    CM       CM\n"
                        "        CDM\n"
                        "LB   LCB   RCB   RB\n"
                        "        GK\n"
                        "유사한 포메이션 : \n"
                        "4-3-1-2```")
            a_queue[0] = 2
            a_queue[3] = 1
            a_queue[4] = 1
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 1
            a_queue[8] = 1
            a_queue[9] = 1


        st_queue = a_queue[0]
        lw_queue = a_queue[1]
        rw_queue = a_queue[2]
        cam_queue = a_queue[3]
        cm_queue = a_queue[4]
        cdm_queue = a_queue[5]
        lb_queue = a_queue[6]
        cb_queue = a_queue[7]
        rb_queue = a_queue[8]
        gk_queue = a_queue[9]



        await ctx.send(content=f"```포지션별 인원 제한은 다음과 같습니다.\n"
                            f"ST : {st_queue}\n"
                            f"LW : {lw_queue}\n"
                            f"RW : {rw_queue}\n"
                            f"CAM : {cam_queue}\n"
                            f"CM : {cm_queue}\n"
                            f"CDM : {cdm_queue}\n"
                            f"LB : {lb_queue}\n"
                            f"CB : {cb_queue}\n"
                            f"RB : {rb_queue}\n"                     
                            f"GK : {gk_queue}\n```")
        if a_team_form == "4-5-1 공격" or a_team_form == "4-4-2 플랫" or b_team_form == "4-5-1 공격" or b_team_form == "4-4-2 플랫":
            await ctx.send("```cs\n"
                        "'4-5-1 공격', '4-2-3-1 넓게', '4-4-2 플랫', '4-1-2-1-2 좁게' 포메이션의 경우,\n"
                        "LM, RM은 LW, RW을 누르세요```")
        if a_team_form == "5-3-2" or a_team_form == "3-5-2" or a_team_form == "3-4-3 플랫" or b_team_form == "5-3-2" or b_team_form == "3-5-2" or b_team_form == "3-4-3 플랫":
            await ctx.send("```cs\n"
                        "'3-5-2', '3-4-3', '5-3-2' 포메이션의 경우,\n"
                        "LM, LWB, RM, RWB는 LB, RB를 누르세요```")

        draft = await ctx.send("희망하는 포지션을 선택해주세요.")
        if st_queue > 0:
            await draft.add_reaction("<:ST:706530008465932299>")
        if lw_queue > 0:
            await draft.add_reaction("<:LW:706530007937450036>")
        if rw_queue > 0:
            await draft.add_reaction("<:RW:706530008201560156>")
        if cam_queue > 0:
            await draft.add_reaction("<:CAM:706530008243634176>")
        if cm_queue > 0:
            await draft.add_reaction("<:CM:706530007928930386>")
        if cdm_queue > 0:
            await draft.add_reaction("<:CDM:706530008289509466>")
        if lb_queue > 0:
            await draft.add_reaction("<:LB:706530008369463359>")
        if cb_queue > 0:
            await draft.add_reaction("<:CB:706530008113610803>")
        if rb_queue > 0:
            await draft.add_reaction("<:RB:706530008100765707>")
        if gk_queue > 0:
            await draft.add_reaction("<:GK:706530008088182786>")

        cd = await ctx.send("카운트 다운")
        for i in range(0, MAX_COUNT):
            j = MAX_COUNT - i
            await cd.edit(content=f"{j}초 남았습니다. 누른 사람 : {len(entry)-1}명")
            time.sleep(1)
            if j == 1:
                await cd.edit(content=f"선택 종료, 누른 사람 : {len(entry)-1}명")
                for k in range(0, len(entry)):
                    if entry[k].startswith("ST"):
                        st.append(entry[k])
                        print("a")
                    if entry[k].startswith("LW"):
                        lw.append(entry[k])
                        print("a")
                    if entry[k].startswith("RW"):
                        rw.append(entry[k])
                        print("a")
                    if entry[k].startswith("CAM"):
                        cam.append(entry[k])
                        print(cam)
                        print("a")
                    if entry[k].startswith("CM"):
                        cm.append(entry[k])
                        print("a")
                    if entry[k].startswith("CDM"):
                        cdm.append(entry[k])
                        print("a")
                    if entry[k].startswith("LB"):
                        lb.append(entry[k])
                        print("a")
                    if entry[k].startswith("CB"):
                        cb.append(entry[k])
                        print("a")
                    if entry[k].startswith("RB"):
                        rb.append(entry[k])
                        print("a")
                    if entry[k].startswith("GK"):
                        gk.append(entry[k])
                        print("a")
                # ST 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[0] > 0:                  # 만약 A팀의 ST 수가 0보다 크면,
                        for i in range(a_queue[0]):     # A팀 ST 수만큼
                            print(st)
                            temp = random.choice(st)    # 랜덤으로 선발해
                            a_team.append(temp)         # A팀으로 배분 후
                            st.remove(temp)             # ST 리스트에서 제거

                    # 대기열 정리
                    for j in range(len(st)):
                        queue.append(st[j])
                except:
                    print(a_team)
                    print(b_team)

                # LW 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[1] > 0:
                        for i in range(a_queue[1]):
                            temp = random.choice(lw)
                            a_team.append(temp)
                            lw.remove(temp)
                    # 대기열 정리
                    for j in range(len(lw)):
                        queue.append(lw[j])

                except:
                    print(a_team)
                    print(b_team)

                # RW 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[2] > 0:
                        for i in range(a_queue[2]):
                            temp = random.choice(rw)
                            a_team.append(temp)
                            rw.remove(temp)

                    for j in range(len(rw)):
                        queue.append(rw[j])
                except:
                    print(a_team)
                    print(b_team)

                # CAM 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[3] > 0:
                        for i in range(a_queue[3]):
                            temp = random.choice(cam)
                            a_team.append(temp)
                            cam.remove(temp)

                    for j in range(len(cam)):
                        queue.append(cam[j])
                except:
                    print(a_team)
                    print(b_team)

                # CM 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[4] > 0:
                        for i in range(a_queue[4]):
                            temp = random.choice(cm)
                            a_team.append(temp)
                            cm.remove(temp)

                    for j in range(len(cm)):
                        queue.append(cm[j])
                except:
                    print(a_team)
                    print(b_team)

                # CDM 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[5] > 0:
                        for i in range(a_queue[5]):
                            temp = random.choice(cdm)
                            a_team.append(temp)
                            cdm.remove(temp)

                    for j in range(len(cdm)):
                        queue.append(cdm[j])
                except:
                    print(a_team)
                    print(b_team)

                # LB 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[6] > 0:
                        for i in range(a_queue[6]):
                            temp = random.choice(lb)
                            a_team.append(temp)
                            lb.remove(temp)
                    for j in range(len(lb)):
                        queue.append(lb[j])
                except:
                    print(a_team)
                    print(b_team)

                # CB 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[7] > 0:
                        for i in range(a_queue[7]):
                            temp = random.choice(cb)
                            a_team.append(temp)
                            cb.remove(temp)

                    for j in range(len(cb)):
                        queue.append(cb[j])
                except:
                    print(a_team)
                    print(b_team)

                # RB 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[8] > 0:
                        for i in range(a_queue[8]):
                            temp = random.choice(rb)
                            a_team.append(temp)
                            rb.remove(temp)
                    for j in range(len(rb)):
                        queue.append(rb[j])
                except:
                    print(a_team)
                    print(b_team)

                # GK 선발 및 대기열 이동
                try:
                    # A팀
                    if a_queue[9] > 0:
                        for i in range(a_queue[9]):
                            temp = random.choice(gk)
                            a_team.append(temp)
                            gk.remove(temp)

                    for j in range(len(gk)):
                        queue.append(gk[j])
                except:
                    print(a_team)
                    print(b_team)

                # 내전 A팀
                temp_a_team = ""
                for j in range(0, len(a_team) + 1):
                    try:
                        temp_a_team = temp_a_team + " " + a_team[j]
                        if a_team[j].startswith("ST"):
                            if a_team[j + 1].startswith("LW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LW"):
                            if a_team[j + 1].startswith("RW"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RW"):
                            if a_team[j + 1].startswith("CAM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CAM"):
                            if a_team[j + 1].startswith("CM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CM"):
                            if a_team[j + 1].startswith("CDM"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CDM"):
                            if a_team[j + 1].startswith("LB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("LB"):
                            if a_team[j + 1].startswith("CB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("CB"):
                            if a_team[j + 1].startswith("RB"):
                                temp_a_team = temp_a_team + "\n\n"
                        if a_team[j].startswith("RB"):
                            if a_team[j + 1].startswith("GK"):
                                temp_a_team = temp_a_team + "\n\n"
                    except:
                        print(temp_a_team)

                await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)


                temp_w_team = ""
                for i in range(0, len(queue)):
                    try:
                        if queue[i].startswith("ST"):
                            queue[i].replace("ST", "")
                            temp_w_team = temp_w_team + queue[i] + " ST\n"
                        if queue[i].startswith("LW"):
                            queue[i].replace("LW", "")
                            temp_w_team = temp_w_team + queue[i] + " LW\n"
                        if queue[i].startswith("RW"):
                            queue[i].replace("RW", "")
                            temp_w_team = temp_w_team + queue[i] + " RW\n"
                        if queue[i].startswith("CAM"):
                            queue[i].replace("CAM", "")
                            temp_w_team = temp_w_team + queue[i] + " CAM\n"
                        if queue[i].startswith("CM"):
                            queue[i].replace("CM", "")
                            temp_w_team = temp_w_team + queue[i] + " CM\n"
                        if queue[i].startswith("CDM"):
                            queue[i].replace("CDM", "")
                            temp_w_team = temp_w_team + queue[i] + " CDM\n"
                        if queue[i].startswith("LB"):
                            queue[i].replace("LB", "")
                            temp_w_team = temp_w_team + queue[i] + " LB\n"
                        if queue[i].startswith("CB"):
                            queue[i].replace("CB", "")
                            temp_w_team = temp_w_team + queue[i] + " CB\n"
                        if queue[i].startswith("RB"):
                            queue[i].replace("RB", "")
                            temp_w_team = temp_w_team + queue[i] + " RB\n"
                        if queue[i].startswith("GK"):
                            queue[i].replace("GK", "")
                            temp_w_team = temp_w_team + queue[i] + " GK\n"
                    except:
                        pass

                await ctx.send("\n\n대기 \n" + temp_w_team)





    @commands.command(pass_context=True)
    async def 대기초기화(self, ctx):
        if str(ctx.message.channel) != "대기순서":
            await ctx.send("대기순서 채널에 작성해주세요")
            time.sleep(BOT_SLEEP_TIME)
        else:
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
            wait_mem.clear()
            wait_mem.append("")
            await ctx.send(ctx.author.mention + "님이 경기 대기실을 초기화하였습니다.")
            time.sleep(BOT_SLEEP_TIME)


    @commands.command()
    async def 번호삭제(self, ctx, *, text):    #삭제 된 사람의 포지션 목록에서 삭제 필요
        role_names = [role.name for role in ctx.author.roles]
        if str(ctx.message.channel) != "대기순서":
            await ctx.send("대기순서 채널에 작성해주세요")
            time.sleep(BOT_SLEEP_TIME)
        else:
            del_wait = ""
            in_num = int(text)
            try:
                if text == 0:
                    await ctx.send("0번은 제거할 수 없습니다.")
                    time.sleep(BOT_SLEEP_TIME)
                else:
                    del_wait = wait_mem[in_num]
                    del wait_mem[in_num]
                    await ctx.send(ctx.author.display_name + " 님이 " + del_wait + "님을 대기열에서 삭제하였습니다.")
                    time.sleep(BOT_SLEEP_TIME)
            except:
                await ctx.send("정확한 번호를 입력해주세요")


    @commands.command()
    async def 대기참가(self, ctx, *, text):
        entry.clear()
        entry.append("")
        no_entry.clear()
        no_entry.append("")
        if str(ctx.message.channel) != "대기순서":
            await ctx.send("대기순서 채널에 작성해주세요")
            time.sleep(BOT_SLEEP_TIME)
            await ctx.channel.purge(limit=DELETE_AMOUNT)
        else:
            try:
                if (position_num[0] == 0 and position_num[1] == 0 and position_num[2] == 0 and position_num[3] == 0 and position_num[4] == 0 and position_num[5] == 0 and position_num[6] == 0 and position_num[7] == 0 and position_num[8] == 0 and position_num[9] == 0):
                    await ctx.send("진행중인 게임이 없어 대기가 불가능합니다!")
                    time.sleep(BOT_SLEEP_TIME)
                else:
                    for i in range(0, len(wait_mem)):
                        if ctx.author.display_name in wait_mem[i]:
                            check_overlap = 1
                            break
                        else:
                            check_overlap = 0
                    if check_overlap == 0:
                        if text == 'st' or text == 'ST':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            st.append("ST/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'lw' or text == 'LW':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            lw.append("LW/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'rw' or text == 'RW':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            rw.append("RW/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'cam' or text == 'CAM':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            cam.append("CAM/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'cm' or text == 'CM':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            cm.append("CM/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'cdm' or text == 'CDM':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            cdm.append("CDM/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'lb' or text == 'LB':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            lb.append("LB/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'cb' or text == 'CB':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            cb.append("CB/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'rb' or text == 'RB':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            rb.append("RB/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        elif text == 'gk' or text == 'GK':
                            wait_mem.append(ctx.author.display_name + "/" + text)
                            gk.append("GK/" + ctx.author.mention)
                            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                            f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
                            time.sleep(BOT_SLEEP_TIME)
                        else:
                            await ctx.send(content=f"{ctx.author.mention}님\n"
                                            f"정확한 포지션을 기입해주세요!")
                    else:
                        await ctx.send("중복 등록이므로 불가합니다.")
                        time.sleep(BOT_SLEEP_TIME)
            except:
                print("aaa")
            alert = ""
            for i in range(1, len(wait_mem)):
                alert = alert + f"{i} . " + wait_mem[i] + "\n"

            if alert == "" :
                await ctx.send("대기열이 존재하지 않습니다. 등록해주세요.")
            else:
                await ctx.send(content=f"```A팀 : {team_list[1]}, B팀 : {team_list[2]}```")
                await ctx.send("대기목록 \n")
                await ctx.send("```" + alert + "```")
    


    @commands.command()
    async def 대기삭제(self, ctx):   
        if str(ctx.message.channel) != "대기순서":
            await ctx.send("대기순서 채널에 작성해주세요")
            time.sleep(BOT_SLEEP_TIME)
            await ctx.channel.purge(limit=DELETE_AMOUNT)
        else:
            try:
                for i in range(0, len(wait_mem)):
                    if wait_mem[i].startswith(ctx.author.display_name):
                        wait_mem.remove(wait_mem[i])#대기 목록에서 삭제 O
                        for j in range(0, len(st)):
                            if "ST/" + ctx.author.mention == st[j]:
                                temp = st[j]
                                st.remove(temp)

                        for j in range(0, len(lw)):
                            if "LW/" + ctx.author.mention == lw[j]:
                                temp = lw[j]
                                lw.remove(temp)

                        for j in range(0, len(rw)):
                            if "RW/" + ctx.author.mention == rw[j]:
                                temp = rw[j]
                                rw.remove(temp)

                        for j in range(0, len(cam)):
                            if "CAM/" + ctx.author.mention == cam[j]:
                                temp = cam[j]
                                cam.remove(temp)

                        for j in range(0, len(cm)):
                            if "CM/" + ctx.author.mention == cm[j]:
                                temp = cm[j]
                                cm.remove(temp)
                        
                        for j in range(0, len(cdm)):
                            if "CDM/" + ctx.author.mention == cdm[j]:
                                temp = cdm[j]
                                cdm.remove(temp)

                        for j in range(0, len(lb)):
                            if "LB/" + ctx.author.mention == lb[j]:
                                temp = lb[j]
                                lb.remove(temp)

                        for j in range(0, len(cb)):
                            if "CB/" + ctx.author.mention == cb[j]:
                                temp = cb[j]
                                cb.remove(temp)
                        
                        for j in range(0, len(rb)):
                            if "RB/" + ctx.author.mention == rb[j]:
                                temp = rb[j]
                                rb.remove(temp)
                        
                        for j in range(0, len(gk)):
                            if "GK/" + ctx.author.mention == gk[j]:
                                temp = gk[j]
                                gk.remove(temp)
                        await ctx.send(ctx.author.display_name + "삭제되었습니다")

            except:
                await ctx.send(content=f"{ctx.author.display_name} 님은 대기열에 없습니다.")

            alert = ""
            for i in range(1, len(wait_mem)):
                alert = alert + f"{i} . " + wait_mem[i] + "\n"

            if alert == "":
                await ctx.send("대기열이 존재하지 않습니다. 등록해주세요.")
            else:
                await ctx.send("대기목록 \n")
                await ctx.send("```" + alert + "```")


    @commands.command()
    async def 대기목록(self, ctx):
        alert = ""
        try:
            for i in range(1, len(wait_mem)):
                alert = alert + f"{i} . " + wait_mem[i] + "\n"

            if alert == "":
                await ctx.send("대기열이 존재하지 않습니다. 등록해주세요.")
            else:
                await ctx.send("대기목록 \n")
                await ctx.send("```" + alert + "```")
        except:
            await ctx.send("대기열에 아무도 없습니다.")


    @commands.command()
    async def 대기분배(self, ctx, *, text):
        queue.clear()
        queue.append("")
        a_team.clear()
        b_team.clear()

        if str(ctx.message.channel) != "대기순서":
            await ctx.send("대기순서 채널에 작성해주세요")
            time.sleep(BOT_SLEEP_TIME)
        else: #text가 1,2,3,4가 아닐 때
            if (text != '2' and text != '3' and text != '4'):
                await ctx.send("올바르지 않은 숫자입니다!")
                time.sleep(BOT_SLEEP_TIME)
            else:
                in_num = int(text)
                await ctx.send("분배 명령어는 꼭 한번만 입력해주세요!")

                if in_num == 2: #2팀 분배
                    cd = await ctx.send("분배를 시작합니다")
                    time.sleep(1)
                    for i in range(0,3):
                        j = 3 - i
                        await cd.edit(content=f"카운트다운 : {j}초")
                        time.sleep(1)
                    #분배 시작
                    try:
                        # A팀
                        if a_queue[0] > 0:                  # 만약 A팀의 ST 수가 0보다 크면,
                            for i in range(a_queue[0]):     # A팀 ST 수만큼
                                print(st)
                                temp = st[i]                # 랜덤으로 선발해
                                a_team.append(temp)         # A팀으로 배분 후
                                del st[i]             # ST 리스트에서 제거
                        # B팀
                        if b_queue[0] > 0:
                            for i in range(0, b_queue[0]):
                                temp = st[i]
                                b_team.append(temp)
                                del st[i]
                        # 대기열 정리
                        for j in range(len(st)):
                            queue.append(st[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # LW 선발 및 대기열 이동
                    try:
                        # B팀
                        if b_queue[1] > 0:
                            for i in range(b_queue[1]):
                                temp = lw[i]
                                b_team.append(temp)
                                del lw[i]
                        # A팀
                        if a_queue[1] > 0:
                            for i in range(a_queue[1]):
                                temp = lw[i]
                                a_team.append(temp)
                                del lw[i]
                        # 대기열 정리
                        for j in range(len(lw)):
                            queue.append(lw[j])

                    except:
                        print(a_team)
                        print(b_team)

                    # RW 선발 및 대기열 이동
                    try:
                        # A팀
                        if a_queue[2] > 0:
                            for i in range(a_queue[2]):
                                temp = rw[i]
                                a_team.append(temp)
                                del rw[i]
                        # B팀
                        if b_queue[2] > 0:
                            for i in range(b_queue[2]):
                                temp = rw[i]
                                b_team.append(temp)
                                del rw[i]
                        for j in range(len(rw)):
                            queue.append(rw[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # CAM 선발 및 대기열 이동
                    try:
                        # B팀
                        print(b_queue[3])
                        print(cam)
                        if b_queue[3] > 0:
                            for i in range(b_queue[3]):
                                temp = cam[i]
                                b_team.append(temp)
                                del cam[i]
                        # A팀
                        if a_queue[3] > 0:
                            for i in range(a_queue[3]):
                                temp = cam[i]
                                a_team.append(temp)
                                del cam[i]

                        for j in range(len(cam)):
                            queue.append(cam[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # CM 선발 및 대기열 이동
                    try:
                        # A팀
                        if a_queue[4] > 0:
                            for i in range(a_queue[4]):
                                temp = cm[i]
                                a_team.append(temp)
                                del cm[i]
                        # B팀
                        if b_queue[4] > 0:
                            for i in range(b_queue[4]):
                                temp = cm[i]
                                b_team.append(temp)
                                del cm[i]
                        for j in range(len(cm)):
                            queue.append(cm[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # CDM 선발 및 대기열 이동
                    try:
                        # B팀
                        if b_queue[5] > 0:
                            for i in range(b_queue[5]):
                                temp = cdm[i]
                                b_team.append(temp)
                                del cdm[i]
                        # A팀
                        if a_queue[5] > 0:
                            for i in range(a_queue[5]):
                                temp = cdm[i]
                                a_team.append(temp)
                                del cdm[i]

                        for j in range(len(cdm)):
                            queue.append(cdm[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # LB 선발 및 대기열 이동
                    try:
                        # A팀
                        if a_queue[6] > 0:
                            for i in range(a_queue[6]):
                                temp = lb[i]
                                a_team.append(temp)
                                del lb[i]
                        # B팀
                        if b_queue[6] > 0:
                            for i in range(b_queue[6]):
                                temp = lb[i]
                                b_team.append(temp)
                                del lb[i]
                        for j in range(len(lb)):
                            queue.append(lb[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # CB 선발 및 대기열 이동
                    try:
                        # B팀
                        if b_queue[7] > 0:
                            for i in range(b_queue[7]):
                                temp = cb[i]
                                b_team.append(temp)
                                del cb[i]
                        # A팀
                        if a_queue[7] > 0:
                            for i in range(a_queue[7]):
                                temp = cb[i]
                                a_team.append(temp)
                                del cb[i]

                        for j in range(len(cb)):
                            queue.append(cb[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # RB 선발 및 대기열 이동
                    try:
                        # A팀

                        if a_queue[8] > 0:
                            for i in range(a_queue[8]):
                                temp = rb[i]
                                a_team.append(temp)
                                del rb[i]
                        # B팀
                        if b_queue[8] > 0:
                            for i in range(b_queue[8]):
                                temp = rb[i]
                                b_team.append(temp)
                                del rb[i]
                        for j in range(len(rb)):
                            queue.append(rb[j])
                    except:
                        print(a_team)
                        print(b_team)

                    # GK 선발 및 대기열 이동
                    try:
                        # B팀
                        if b_queue[9] > 0:
                            for i in range(b_queue[9]):
                                temp = gk[i]
                                b_team.append(temp)
                                del gk[i]
                        # A팀
                        if a_queue[9] > 0:
                            for i in range(a_queue[9]):
                                temp = gk[i]
                                a_team.append(temp)
                                del gk[i]

                        for j in range(len(gk)):
                            queue.append(gk[j])
                    except:
                        print(a_team)
                        print(b_team)

                    
                    #a팀 
                    temp_a_team = ""
                    for j in range(0, len(a_team) + 1):
                        try:
                            temp_a_team = temp_a_team + " " + a_team[j]
                            if a_team[j].startswith("ST"):
                                if a_team[j + 1].startswith("LW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LW"):
                                if a_team[j + 1].startswith("RW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RW"):
                                if a_team[j + 1].startswith("CAM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CAM"):
                                if a_team[j + 1].startswith("CM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CM"):
                                if a_team[j + 1].startswith("CDM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CDM"):
                                if a_team[j + 1].startswith("LB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LB"):
                                if a_team[j + 1].startswith("CB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CB"):
                                if a_team[j + 1].startswith("RB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RB"):
                                if a_team[j + 1].startswith("GK"):
                                    temp_a_team = temp_a_team + "\n\n"
                        except:
                            print(temp_a_team)

                    await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)

                    #B팀
                    temp_b_team = ""
                    for i in range(0, len(b_team) + 1):
                        try:
                            temp_b_team = temp_b_team + " " + b_team[i]
                            if b_team[i].startswith("ST"):
                                if b_team[i + 1].startswith("LW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LW"):
                                if b_team[i + 1].startswith("RW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RW"):
                                if b_team[i + 1].startswith("CAM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CAM"):
                                if b_team[i + 1].startswith("CM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CM"):
                                if b_team[i + 1].startswith("CDM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CDM"):
                                if b_team[i + 1].startswith("LB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LB"):
                                if b_team[i + 1].startswith("CB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CB"):
                                if b_team[i + 1].startswith("RB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("GK"):
                                if b_team[i + 1].startswith("RB", ""):
                                    temp_b_team = temp_b_team + "\n\n"
                        except:
                            print(temp_b_team)

                    await ctx.send(content=f"\n팀 B({TEAM_B_COLOR}) 명단 :  \n" + temp_b_team)
                    
                    #대기
                    temp_w_team = ""
                    for i in range(0, len(queue)):
                        try:
                            if queue[i].startswith("ST"):
                                queue[i].replace("ST", "")
                                temp_w_team = temp_w_team + queue[i] + " ST\n"
                            if queue[i].startswith("LW"):
                                queue[i].replace("LW", "")
                                temp_w_team = temp_w_team + queue[i] + " LW\n"
                            if queue[i].startswith("RW"):
                                queue[i].replace("RW", "")
                                temp_w_team = temp_w_team + queue[i] + " RW\n"
                            if queue[i].startswith("CAM"):
                                queue[i].replace("CAM", "")
                                temp_w_team = temp_w_team + queue[i] + " CAM\n"
                            if queue[i].startswith("CM"):
                                queue[i].replace("CM", "")
                                temp_w_team = temp_w_team + queue[i] + " CM\n"
                            if queue[i].startswith("CDM"):
                                queue[i].replace("CDM", "")
                                temp_w_team = temp_w_team + queue[i] + " CDM\n"
                            if queue[i].startswith("LB"):
                                queue[i].replace("LB", "")
                                temp_w_team = temp_w_team + queue[i] + " LB\n"
                            if queue[i].startswith("CB"):
                                queue[i].replace("CB", "")
                                temp_w_team = temp_w_team + queue[i] + " CB\n"
                            if queue[i].startswith("RB"):
                                queue[i].replace("RB", "")
                                temp_w_team = temp_w_team + queue[i] + " RB\n"
                            if queue[i].startswith("GK"):
                                queue[i].replace("GK", "")
                                temp_w_team = temp_w_team + queue[i] + " GK\n"
                        except:
                            pass

                    await ctx.send("\n\n대기 \n" + temp_w_team)
                    time.sleep(1)
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
                    wait_mem.clear()
                    wait_mem.append("")
                    await ctx.send("대기목록이 초기화 되었습니다.")

                
    @commands.command()
    async def 드래프트1(self, ctx):
        #if str(ctx.message.channel) != "드래프트" or "대기순서":
            #await ctx.send("드래프트 채널에 작성해주세요")
        #else:
            switch = 0
            entry.clear()
            entry.append("")
            queue.clear()
            queue.append("")
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
            a_team.clear()
            b_team.clear()

            draft = await ctx.send("포지션을 선택해주세요")
            await draft.add_reaction("<:ST:706530008465932299>")
            await draft.add_reaction("<:LW:706530007937450036>")
            await draft.add_reaction("<:RW:706530008201560156>")

            await draft.add_reaction("<:CM:706530007928930386>")
            await draft.add_reaction("<:CDM:706530008289509466>")
            await draft.add_reaction("<:LB:706530008369463359>")
            await draft.add_reaction("<:CB:706530008113610803>")
            await draft.add_reaction("<:RB:706530008100765707>")
            await draft.add_reaction("<:GK:706530008088182786>")

            cd = await ctx.send("카운트 다운")
            for i in range(0, MAX_COUNT):
                j = MAX_COUNT - i
                await cd.edit(content=f"{j}초 남았습니다.")
                time.sleep(1)
                if j == 1:
                    await cd.edit(content="선택 종료")
                    for k in range(0, len(entry)):
                        if entry[k].startswith("ST"):
                            st.append(entry[k])
                        if entry[k].startswith("LW"):
                            lw.append(entry[k])
                        if entry[k].startswith("RW"):
                            rw.append(entry[k])
                        if entry[k].startswith("CM"):
                            cm.append(entry[k])
                        if entry[k].startswith("CDM"):
                            cdm.append(entry[k])
                        if entry[k].startswith("LB"):
                            lb.append(entry[k])
                        if entry[k].startswith("CB"):
                            cb.append(entry[k])
                        if entry[k].startswith("RB"):
                            rb.append(entry[k])
                        if entry[k].startswith("GK"):
                            gk.append(entry[k])

                    # ST 선발 & 대기열 이동
                    try:
                        temp = random.choice(st)
                        a_team.append(temp)
                        st.remove(temp)
                    except:
                        print(a_team)

                    # LW 선발
                    try:
                        temp_lw = random.choice(lw)
                        a_team.append(temp_lw)
                        lw.remove(temp_lw)
                    except:
                        print(a_team)

                    # RW 선발
                    try:
                        temp_rw = random.choice(rw)
                        a_team.append(temp_rw)
                        rw.remove(temp_rw)
                    except:
                        print(a_team)

                    # CM 선발 & 대기열 이동
                    try:
                        for j in range(0, 2):
                            temp_cm = random.choice(cm)
                            a_team.append(temp_cm)
                            cm.remove(temp_cm)
                    except:
                        print(a_team)

                    # CDM 선발
                    try:
                        temp_cdm = random.choice(cdm)
                        a_team.append(temp_cdm)
                        cdm.remove(temp_cdm)
                    except:
                        print(a_team)

                    # LB 선발
                    try:
                        temp_lb = random.choice(lb)
                        a_team.append(temp_lb)
                        lb.remove(temp_lb)

                    except:
                        print(a_team)

                    # CB 선발
                    try:
                        for i in range(0, 2):
                            temp_cb = random.choice(cb)
                            a_team.append(temp_cb)
                            cb.remove(temp_cb)
                    except:
                        print(a_team)

                    # RB 선발
                    try:
                        temp_rb = random.choice(rb)
                        a_team.append(temp_rb)
                        rb.remove(temp_rb)
                    except:
                        print(a_team)

                    # GK 선발
                    try:
                        temp_gk = random.choice(gk)
                        a_team.append(temp_gk)
                        gk.remove(temp_gk)

                    except:
                        print(a_team)

                    # ST 대기열 정리
                    for j in range(0, len(st)):
                        try:
                            queue.append(st[j])
                        except:
                            print(a_team)

                    # LW 대기열 정리
                    for j in range(0, len(lw)):
                        try:
                            queue.append(lw[j])
                        except:
                            print(a_team)

                    # RW 대기열 정리
                    for j in range(0, len(rw)):
                        try:
                            queue.append(rw[j])
                        except:
                            print(a_team)

                    # CM 대기열 정리
                    for j in range(0, len(cm)):
                        try:
                            queue.append(cm[j])
                        except:
                            print(a_team)

                    # CDM 대기열 정리
                    for j in range(0, len(cdm)):
                        try:
                            queue.append(cdm[j])
                        except:
                            print(a_team)

                    # LB 대기열 정리
                    for j in range(0, len(lb)):
                        try:
                            queue.append(lb[j])
                        except:
                            print(a_team)

                    # CB 대기열 정리
                    for j in range(0, len(cb)):
                        try:
                            queue.append(cb[j])
                        except:
                            print(a_team)

                    # RB 대기열 정리
                    for j in range(0, len(rb)):
                        try:
                            queue.append(rb[j])
                        except:
                            print(a_team)

                    # GK 대기열 정리
                    for j in range(0, len(gk)):
                        try:
                            queue.append(gk[j])
                        except:
                            print(a_team)

                    # 내전 A팀
                    temp_a_team = ""
                    for j in range(0, len(a_team)+1):
                        try:
                            temp_a_team = temp_a_team + " " + a_team[j]
                            if a_team[j].startswith("ST"):
                                if a_team[j + 1].startswith("LW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LW"):
                                if a_team[j + 1].startswith("RW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RW"):
                                if a_team[j + 1].startswith("CM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CM"):
                                if a_team[j + 1].startswith("CDM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CDM"):
                                if a_team[j + 1].startswith("LB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LB"):
                                if a_team[j + 1].startswith("CB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CB"):
                                if a_team[j + 1].startswith("RB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RB"):
                                if a_team[j + 1].startswith("GK"):
                                    temp_a_team = temp_a_team + "\n\n"
                        except:
                            print(temp_a_team)

                    await ctx.send("팀 명단 : \n" + temp_a_team)

                    temp_w_team = ""
                    for i in range(0, len(queue)):
                        try:
                            if queue[i].startswith("ST"):
                                queue[i].replace("ST", "")
                                temp_w_team = temp_w_team + queue[i] + " ST\n"
                            if queue[i].startswith("LW"):
                                queue[i].replace("LW", "")
                                temp_w_team = temp_w_team + queue[i] + " LW\n"
                            if queue[i].startswith("RW"):
                                queue[i].replace("RW", "")
                                temp_w_team = temp_w_team + queue[i] + " RW\n"
                            if queue[i].startswith("CM"):
                                queue[i].replace("CM", "")
                                temp_w_team = temp_w_team + queue[i] + " CM\n"
                            if queue[i].startswith("CDM"):
                                queue[i].replace("CDM", "")
                                temp_w_team = temp_w_team + queue[i] + " CDM\n"
                            if queue[i].startswith("LB"):
                                queue[i].replace("LB", "")
                                temp_w_team = temp_w_team + queue[i] + " LB\n"
                            if queue[i].startswith("CB"):
                                queue[i].replace("CB", "")
                                temp_w_team = temp_w_team + queue[i] + " CB\n"
                            if queue[i].startswith("RB"):
                                queue[i].replace("RB", "")
                                temp_w_team = temp_w_team + queue[i] + " RB\n"
                            if queue[i].startswith("GK"):
                                queue[i].replace("GK", "")
                                temp_w_team = temp_w_team + queue[i] + " GK\n"
                        except:
                            pass

                    await ctx.send("\n\n대기 \n" + temp_w_team)

    @commands.command()
    async def 드래프트2(self, ctx):
        #if str(ctx.message.channel) != "드래프트" or "대기순서":
            #await ctx.send("드래프트 채널에 작성해주세요")
        #else:
            switch = 0
            entry.clear()
            entry.append("")
            queue.clear()
            queue.append("")
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
            a_team.clear()
            b_team.clear()
            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 0
            a_queue[4] = 2
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[3] = 0
            b_queue[4] = 2
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

            tpli = ["<:ST:706530008465932299>", "<:LW:706530007937450036>", "<:RW:706530008201560156>", "<:CM:706530007928930386>", "<:CDM:706530008289509466>", "<:LB:706530008369463359>", "<:CB:706530008113610803>", "<:RB:706530008100765707>", "<:GK:706530008088182786>"]

            draft = await ctx.send("포지션을 선택해주세요")
            for s in tpli:
                await draft.add_reaction(s)
            '''
            await draft.add_reaction("<:ST:706530008465932299>")
            await draft.add_reaction("<:LW:706530007937450036>")
            await draft.add_reaction("<:RW:706530008201560156>")
            await draft.add_reaction("<:CM:706530007928930386>")
            await draft.add_reaction("<:CDM:706530008289509466>")
            await draft.add_reaction("<:LB:706530008369463359>")
            await draft.add_reaction("<:CB:706530008113610803>")
            await draft.add_reaction("<:RB:706530008100765707>")
            await draft.add_reaction("<:GK:706530008088182786>")'''

            position_num[0] = 2
            position_num[1] = 2
            position_num[2] = 2
            position_num[3] = 0
            position_num[4] = 4
            position_num[5] = 2
            position_num[6] = 2
            position_num[7] = 4
            position_num[8] = 2
            position_num[9] = 2


            cd = await ctx.send("카운트 다운")
            for i in range(0, MAX_COUNT):
                j = MAX_COUNT - i
                await cd.edit(content=f"{j}초 남았습니다.")
                time.sleep(1)
                if j == 1:
                    await cd.edit(content="선택 종료")
                    for k in range(0, len(entry)):
                        if entry[k].startswith("ST"):
                            st.append(entry[k])
                        if entry[k].startswith("LW"):
                            lw.append(entry[k])
                        if entry[k].startswith("RW"):
                            rw.append(entry[k])
                        if entry[k].startswith("CM"):
                            cm.append(entry[k])
                        if entry[k].startswith("CDM"):
                            cdm.append(entry[k])
                        if entry[k].startswith("LB"):
                            lb.append(entry[k])
                        if entry[k].startswith("CB"):
                            cb.append(entry[k])
                        if entry[k].startswith("RB"):
                            rb.append(entry[k])
                        if entry[k].startswith("GK"):
                            gk.append(entry[k])

                    # ST 선발 & 대기열 이동
                    try:
                        temp = random.choice(st)
                        a_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        b_team.append(temp)
                        st.remove(temp)
                    except:
                        print(a_team)

                    # LW 선발
                    try:
                        temp_lw = random.choice(lw)
                        b_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        a_team.append(temp_lw)
                        lw.remove(temp_lw)
                    except:
                        print(a_team)

                    # RW 선발
                    try:
                        temp_rw = random.choice(rw)
                        a_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        b_team.append(temp_rw)
                        rw.remove(temp_rw)
                    except:
                        print(a_team)

                    # CM 선발 & 대기열 이동
                    try:
                        for j in range(0, 2):
                            temp_cm = random.choice(cm)
                            b_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            a_team.append(temp_cm)
                            cm.remove(temp_cm)
                    except:
                        print(a_team)

                    # CDM 선발
                    try:
                        temp_cdm = random.choice(cdm)
                        a_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        b_team.append(temp_cdm)
                        cdm.remove(temp_cdm)
                    except:
                        print(a_team)

                    # LB 선발
                    try:
                        temp_lb = random.choice(lb)
                        b_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        a_team.append(temp_lb)
                        lb.remove(temp_lb)

                    except:
                        print(a_team)

                    # CB 선발
                    try:
                        for i in range(0, 2):
                            temp_cb = random.choice(cb)
                            a_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            b_team.append(temp_cb)
                            cb.remove(temp_cb)
                    except:
                        print(a_team)

                    # RB 선발
                    try:
                        temp_rb = random.choice(rb)
                        b_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        a_team.append(temp_rb)
                        rb.remove(temp_rb)
                    except:
                        print(a_team)

                    # GK 선발
                    try:
                        temp_gk = random.choice(gk)
                        a_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        b_team.append(temp_gk)
                        gk.remove(temp_gk)
                    except:
                        print(a_team)

                    # ST 대기열 정리
                    for j in range(0, len(st)):
                        try:
                            queue.append(st[j])
                        except:
                            print(a_team)

                    # LW 대기열 정리
                    for j in range(0, len(lw)):
                        try:
                            queue.append(lw[j])
                        except:
                            print(a_team)

                    # RW 대기열 정리
                    for j in range(0, len(rw)):
                        try:
                            queue.append(rw[j])
                        except:
                            print(a_team)

                    # CM 대기열 정리
                    for j in range(0, len(cm)):
                        try:
                            queue.append(cm[j])
                        except:
                            print(a_team)

                    # CDM 대기열 정리
                    for j in range(0, len(cdm)):
                        try:
                            queue.append(cdm[j])
                        except:
                            print(a_team)

                    # LB 대기열 정리
                    for j in range(0, len(lb)):
                        try:
                            queue.append(lb[j])
                        except:
                            print(a_team)

                    # CB 대기열 정리
                    for j in range(0, len(cb)):
                        try:
                            queue.append(cb[j])
                        except:
                            print(a_team)

                    # RB 대기열 정리
                    for j in range(0, len(rb)):
                        try:
                            queue.append(rb[j])
                        except:
                            print(a_team)

                    # GK 대기열 정리
                    for j in range(0, len(gk)):
                        try:
                            queue.append(gk[j])
                        except:
                            print(a_team)

                    # 내전 A팀
                    temp_a_team = ""
                    for j in range(0, len(a_team)+1):
                        try:
                            temp_a_team = temp_a_team + " " + a_team[j]
                            if a_team[j].startswith("ST"):
                                if a_team[j + 1].startswith("LW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LW"):
                                if a_team[j + 1].startswith("RW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RW"):
                                if a_team[j + 1].startswith("CM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CM"):
                                if a_team[j + 1].startswith("CDM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CDM"):
                                if a_team[j + 1].startswith("LB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LB"):
                                if a_team[j + 1].startswith("CB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CB"):
                                if a_team[j + 1].startswith("RB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RB"):
                                if a_team[j + 1].startswith("GK"):
                                    temp_a_team = temp_a_team + "\n\n"
                        except:
                            print(temp_a_team)

                    await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)

                    # 내전 B팀
                    temp_b_team = ""
                    for i in range(0, len(b_team)+1):
                        try:
                            temp_b_team = temp_b_team + " " + b_team[i]
                            if b_team[i].startswith("ST"):
                                if b_team[i + 1].startswith("LW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LW"):
                                if b_team[i + 1].startswith("RW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RW"):
                                if b_team[i + 1].startswith("CM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CM"):
                                if b_team[i + 1].startswith("CDM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CDM"):
                                if b_team[i + 1].startswith("LB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LB"):
                                if b_team[i + 1].startswith("CB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CB"):
                                if b_team[i + 1].startswith("RB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("GK"):
                                if b_team[i + 1].startswith("RB", ""):
                                    temp_b_team = temp_b_team + "\n\n"
                        except:
                            print(temp_b_team)

                    await ctx.send(content=f"\n팀 B({TEAM_B_COLOR}) 명단 :  \n" + temp_b_team)

                    temp_w_team = ""
                    for i in range(0, len(queue)):
                        try:
                            if queue[i].startswith("ST"):
                                queue[i].replace("ST", "")
                                temp_w_team = temp_w_team + queue[i] + " ST\n"
                            if queue[i].startswith("LW"):
                                queue[i].replace("LW", "")
                                temp_w_team = temp_w_team + queue[i] + " LW\n"
                            if queue[i].startswith("RW"):
                                queue[i].replace("RW", "")
                                temp_w_team = temp_w_team + queue[i] + " RW\n"
                            if queue[i].startswith("CM"):
                                queue[i].replace("CM", "")
                                temp_w_team = temp_w_team + queue[i] + " CM\n"
                            if queue[i].startswith("CDM"):
                                queue[i].replace("CDM", "")
                                temp_w_team = temp_w_team + queue[i] + " CDM\n"
                            if queue[i].startswith("LB"):
                                queue[i].replace("LB", "")
                                temp_w_team = temp_w_team + queue[i] + " LB\n"
                            if queue[i].startswith("CB"):
                                queue[i].replace("CB", "")
                                temp_w_team = temp_w_team + queue[i] + " CB\n"
                            if queue[i].startswith("RB"):
                                queue[i].replace("RB", "")
                                temp_w_team = temp_w_team + queue[i] + " RB\n"
                            if queue[i].startswith("GK"):
                                queue[i].replace("GK", "")
                                temp_w_team = temp_w_team + queue[i] + " GK\n"
                        except:
                            pass

                    await ctx.send("\n\n대기 \n" + temp_w_team)

    @commands.command()
    async def 드래프트3(self, ctx):
        #if str(ctx.message.channel) != "드래프트":
            #await ctx.send("드래프트 채널에 작성해주세요")
        #else:
            switch = 0
            entry.clear()
            entry.append("")
            queue.clear()
            queue.append("")
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
            a_team.clear()
            b_team.clear()
            c_team.clear()

            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 0
            a_queue[4] = 2
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[3] = 0
            b_queue[4] = 2
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

            c_queue[0] = 1
            c_queue[1] = 1
            c_queue[2] = 1
            c_queue[3] = 0
            c_queue[4] = 2
            c_queue[5] = 1
            c_queue[6] = 1
            c_queue[7] = 2
            c_queue[8] = 1
            c_queue[9] = 1

            draft = await ctx.send("포지션을 선택해주세요")
            await draft.add_reaction("<:ST:706530008465932299>")
            await draft.add_reaction("<:LW:706530007937450036>")
            await draft.add_reaction("<:RW:706530008201560156>")
            await draft.add_reaction("<:CM:706530007928930386>")
            await draft.add_reaction("<:CDM:706530008289509466>")
            await draft.add_reaction("<:LB:706530008369463359>")
            await draft.add_reaction("<:CB:706530008113610803>")
            await draft.add_reaction("<:RB:706530008100765707>")
            await draft.add_reaction("<:GK:706530008088182786>")

            position_num[0] = 3
            position_num[1] = 3
            position_num[2] = 3
            position_num[3] = 0
            position_num[4] = 6
            position_num[5] = 3
            position_num[6] = 3
            position_num[7] = 6
            position_num[8] = 3
            position_num[9] = 3


            cd = await ctx.send("카운트 다운")
            for i in range(0, MAX_COUNT):
                j = MAX_COUNT - i
                await cd.edit(content=f"{j}초 남았습니다.")
                time.sleep(1)
                if j == 1:
                    await cd.edit(content="선택 종료")
                    for k in range(0, len(entry)):
                        if entry[k].startswith("ST"):
                            st.append(entry[k])
                        if entry[k].startswith("LW"):
                            lw.append(entry[k])
                        if entry[k].startswith("RW"):
                            rw.append(entry[k])
                        if entry[k].startswith("CM"):
                            cm.append(entry[k])
                        if entry[k].startswith("CDM"):
                            cdm.append(entry[k])
                        if entry[k].startswith("LB"):
                            lb.append(entry[k])
                        if entry[k].startswith("CB"):
                            cb.append(entry[k])
                        if entry[k].startswith("RB"):
                            rb.append(entry[k])
                        if entry[k].startswith("GK"):
                            gk.append(entry[k])

                    # ST 선발 & 대기열 이동
                    try:
                        temp = random.choice(st)
                        a_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        b_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        c_team.append(temp)
                        st.remove(temp)

                    except:
                        print(a_team)

                    # LW 선발
                    try:
                        temp_lw = random.choice(lw)
                        b_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        c_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        a_team.append(temp_lw)
                        lw.remove(temp_lw)
                    except:
                        print(a_team)

                    # RW 선발
                    try:
                        temp_rw = random.choice(rw)
                        c_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        b_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        a_team.append(temp_rw)
                        rw.remove(temp_rw)
                    except:
                        print(a_team)

                    # CM 선발 & 대기열 이동
                    try:
                        for j in range(0, 2):
                            temp_cm = random.choice(cm)
                            a_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            b_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            c_team.append(temp_cm)
                            cm.remove(temp_cm)
                    except:
                        print(a_team)

                    # CDM 선발
                    try:
                        temp_cdm = random.choice(cdm)
                        a_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        b_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        c_team.append(temp_cdm)
                        cdm.remove(temp_cdm)
                    except:
                        print(a_team)

                    # LB 선발
                    try:
                        temp_lb = random.choice(lb)
                        b_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        c_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        a_team.append(temp_lb)
                        lb.remove(temp_lb)
                    except:
                        print(a_team)

                    # CB 선발
                    try:
                        for j in range(0, 2):
                            temp_cb = random.choice(cb)
                            c_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            a_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            b_team.append(temp_cb)
                            cb.remove(temp_cb)
                    except:
                        print(a_team)

                    # RB 선발
                    try:
                        temp_rb = random.choice(rb)
                        a_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        b_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        c_team.append(temp_rb)
                        rb.remove(temp_rb)
                    except:
                        print(a_team)

                    # GK 선발
                    try:
                        temp_gk = random.choice(gk)
                        a_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        b_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        c_team.append(temp_gk)
                        gk.remove(temp_gk)
                    except:
                        print(a_team)

                    # ST 대기열 정리
                    for j in range(0, len(st)):
                        try:
                            queue.append(st[j])
                        except:
                            print(a_team)

                    # LW 대기열 정리
                    for j in range(0, len(lw)):
                        try:
                            queue.append(lw[j])
                        except:
                            print(a_team)

                    # RW 대기열 정리
                    for j in range(0, len(rw)):
                        try:
                            queue.append(rw[j])
                        except:
                            print(a_team)

                    # CM 대기열 정리
                    for j in range(0, len(cm)):
                        try:
                            queue.append(cm[j])
                        except:
                            print(a_team)

                    # CDM 대기열 정리
                    for j in range(0, len(cdm)):
                        try:
                            queue.append(cdm[j])
                        except:
                            print(a_team)

                    # LB 대기열 정리
                    for j in range(0, len(lb)):
                        try:
                            queue.append(lb[j])
                        except:
                            print(a_team)

                    # CB 대기열 정리
                    for j in range(0, len(cb)):
                        try:
                            queue.append(cb[j])
                        except:
                            print(a_team)

                    # RB 대기열 정리
                    for j in range(0, len(rb)):
                        try:
                            queue.append(rb[j])
                        except:
                            print(a_team)

                    # GK 대기열 정리
                    for j in range(0, len(gk)):
                        try:
                            queue.append(gk[j])
                        except:
                            print(a_team)

                    # 내전 A팀
                    temp_a_team = ""
                    for j in range(0, len(a_team)+1):
                        try:
                            temp_a_team = temp_a_team + " " + a_team[j]
                            if a_team[j].startswith("ST"):
                                if a_team[j + 1].startswith("LW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LW"):
                                if a_team[j + 1].startswith("RW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RW"):
                                if a_team[j + 1].startswith("CM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CM"):
                                if a_team[j + 1].startswith("CDM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CDM"):
                                if a_team[j + 1].startswith("LB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LB"):
                                if a_team[j + 1].startswith("CB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CB"):
                                if a_team[j + 1].startswith("RB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RB"):
                                if a_team[j + 1].startswith("GK"):
                                    temp_a_team = temp_a_team + "\n\n"
                        except:
                            print(temp_a_team)

                    await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)

                    # 내전 B팀
                    temp_b_team = ""
                    for i in range(0, len(b_team)+1):
                        try:
                            temp_b_team = temp_b_team + " " + b_team[i]
                            if b_team[i].startswith("ST"):
                                if b_team[i + 1].startswith("LW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LW"):
                                if b_team[i + 1].startswith("RW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RW"):
                                if b_team[i + 1].startswith("CM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CM"):
                                if b_team[i + 1].startswith("CDM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CDM"):
                                if b_team[i + 1].startswith("LB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LB"):
                                if b_team[i + 1].startswith("CB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CB"):
                                if b_team[i + 1].startswith("RB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RB"):
                                if b_team[i + 1].startswith("GK", ""):
                                    temp_b_team = temp_b_team + "\n\n"
                        except:
                            print(temp_b_team)

                    await ctx.send(content=f"팀 B({TEAM_B_COLOR}) 명단 : \n" + temp_b_team)

                    # 내전 C팀
                    temp_c_team = ""
                    for i in range(0, len(c_team)+1):
                        try:
                            temp_c_team = temp_c_team + " " + c_team[i]
                            if c_team[i].startswith("ST"):
                                if c_team[i + 1].startswith("LW"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("LW"):
                                if c_team[i + 1].startswith("RW"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("RW"):
                                if c_team[i + 1].startswith("CM"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CM"):
                                if c_team[i + 1].startswith("CDM"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CDM"):
                                if c_team[i + 1].startswith("LB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("LB"):
                                if c_team[i + 1].startswith("CB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CB"):
                                if c_team[i + 1].startswith("RB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("RB"):
                                if c_team[i + 1].startswith("GK", ""):
                                    temp_c_team = temp_c_team + "\n\n"
                        except:
                            print(temp_c_team)

                    await ctx.send(content=f"\n팀 C({TEAM_C_COLOR}) 명단 : \n" + temp_c_team)

                    temp_w_team = ""
                    for i in range(0, len(queue)):
                        try:
                            if queue[i].startswith("ST"):
                                queue[i].replace("ST", "")
                                temp_w_team = temp_w_team + queue[i] + " ST\n"
                            if queue[i].startswith("LW"):
                                queue[i].replace("LW", "")
                                temp_w_team = temp_w_team + queue[i] + " LW\n"
                            if queue[i].startswith("RW"):
                                queue[i].replace("RW", "")
                                temp_w_team = temp_w_team + queue[i] + " RW\n"
                            if queue[i].startswith("CM"):
                                queue[i].replace("CM", "")
                                temp_w_team = temp_w_team + queue[i] + " CM\n"
                            if queue[i].startswith("CDM"):
                                queue[i].replace("CDM", "")
                                temp_w_team = temp_w_team + queue[i] + " CDM\n"
                            if queue[i].startswith("LB"):
                                queue[i].replace("LB", "")
                                temp_w_team = temp_w_team + queue[i] + " LB\n"
                            if queue[i].startswith("CB"):
                                queue[i].replace("CB", "")
                                temp_w_team = temp_w_team + queue[i] + " CB\n"
                            if queue[i].startswith("RB"):
                                queue[i].replace("RB", "")
                                temp_w_team = temp_w_team + queue[i] + " RB\n"
                            if queue[i].startswith("GK"):
                                queue[i].replace("GK", "")
                                temp_w_team = temp_w_team + queue[i] + " GK\n"
                        except:
                            pass

                    await ctx.send("\n\n대기 \n" + temp_w_team)

    '''
    @commands.command()
    async def 대기실분배2(self, ctx, num1, num2):
        key = 0
        div = []
        wait_mem_name = []
        wait_mem_pos = []
        alert = ""

        for i in range(1, len(wait_mem)):
            split = wait_mem[i].split('/')
            wait_mem_name[i] = split[0]
            wait_mem_pos[i] = split[1]

            alert = alert + f"{i} . " + wait_mem[i] + "\n"

        await ctx.send("대기목록 \n")
        await ctx.send("```" + alert + "```")
        await ctx.send(content=f"닉네임 : {wait_mem_name}, 포지션 : {wait_mem_pos}")
        key = 1

        if key == 1:
            if num1 == num2:
                for j in range(0, len(wait_mem)-1):
                    pass
    '''



    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        for i in range(0, len(entry)):
            if user.mention in entry[i]:
                switch = 1
                break
            else:
                switch = 0

        # 사다리타기
        if str(reaction.emoji) == "⭕":
            entry.append("⭕/" + user.mention)

        # 드래프트용
        if switch == 0:  # 스위치가 꺼져있으면
            if user.bot == 1:  # 봇이면 패스
                return None
            if str(reaction.emoji) == "<:ST:706530008465932299>":
                entry.append("ST/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:LW:706530007937450036>":
                entry.append("LW/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:RW:706530008201560156>":
                entry.append("RW/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:CAM:706530008243634176>":
                entry.append("CAM/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:CM:706530007928930386>":
                entry.append("CM/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:CDM:706530008289509466>":
                entry.append("CDM/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:LB:706530008369463359>":
                entry.append("LB/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:CB:706530008113610803>":
                entry.append("CB/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:RB:706530008100765707>":
                entry.append("RB/" + user.mention)
                no_entry.append(user.display_name)
            if str(reaction.emoji) == "<:GK:706530008088182786>":
                entry.append("GK/" + user.mention)
                no_entry.append(user.display_name)


    @commands.command()
    async def 드래프트4(self, ctx):
        #if str(ctx.message.channel) != "드래프트":
            #await ctx.send("드래프트 채널에 작성해주세요")
        #else:
            switch = 0
            entry.clear()
            entry.append("")
            queue.clear()
            queue.append("")
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
            a_team.clear()
            b_team.clear()
            c_team.clear()
            d_team.clear()

            a_queue[0] = 1
            a_queue[1] = 1
            a_queue[2] = 1
            a_queue[3] = 0
            a_queue[4] = 2
            a_queue[5] = 1
            a_queue[6] = 1
            a_queue[7] = 2
            a_queue[8] = 1
            a_queue[9] = 1

            b_queue[0] = 1
            b_queue[1] = 1
            b_queue[2] = 1
            b_queue[3] = 0
            b_queue[4] = 2
            b_queue[5] = 1
            b_queue[6] = 1
            b_queue[7] = 2
            b_queue[8] = 1
            b_queue[9] = 1

            c_queue[0] = 1
            c_queue[1] = 1
            c_queue[2] = 1
            c_queue[3] = 0
            c_queue[4] = 2
            c_queue[5] = 1
            c_queue[6] = 1
            c_queue[7] = 2
            c_queue[8] = 1
            c_queue[9] = 1

            d_queue[0] = 1
            d_queue[1] = 1
            d_queue[2] = 1
            d_queue[3] = 0
            d_queue[4] = 2
            d_queue[5] = 1
            d_queue[6] = 1
            d_queue[7] = 2
            d_queue[8] = 1
            d_queue[9] = 1

            draft = await ctx.send("포지션을 선택해주세요")
            await draft.add_reaction("<:ST:706530008465932299>")
            await draft.add_reaction("<:LW:706530007937450036>")
            await draft.add_reaction("<:RW:706530008201560156>")
            await draft.add_reaction("<:CM:706530007928930386>")
            await draft.add_reaction("<:CDM:706530008289509466>")
            await draft.add_reaction("<:LB:706530008369463359>")
            await draft.add_reaction("<:CB:706530008113610803>")
            await draft.add_reaction("<:RB:706530008100765707>")
            await draft.add_reaction("<:GK:706530008088182786>")

            position_num[0] = 4
            position_num[1] = 4
            position_num[2] = 4
            position_num[3] = 0
            position_num[4] = 8
            position_num[5] = 4
            position_num[6] = 4
            position_num[7] = 8
            position_num[8] = 4
            position_num[9] = 4


            cd = await ctx.send("카운트 다운")
            for i in range(0, MAX_COUNT):
                j = MAX_COUNT - i
                await cd.edit(content=f"{j}초 남았습니다.")
                time.sleep(1)
                if j == 1:
                    await cd.edit(content="선택 종료")
                    for k in range(0, len(entry)):
                        if entry[k].startswith("ST"):
                            st.append(entry[k])
                        if entry[k].startswith("LW"):
                            lw.append(entry[k])
                        if entry[k].startswith("RW"):
                            rw.append(entry[k])
                        if entry[k].startswith("CM"):
                            cm.append(entry[k])
                        if entry[k].startswith("CDM"):
                            cdm.append(entry[k])
                        if entry[k].startswith("LB"):
                            lb.append(entry[k])
                        if entry[k].startswith("CB"):
                            cb.append(entry[k])
                        if entry[k].startswith("RB"):
                            rb.append(entry[k])
                        if entry[k].startswith("GK"):
                            gk.append(entry[k])

                    # ST 선발 & 대기열 이동
                    try:
                        temp = random.choice(st)
                        a_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        b_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        c_team.append(temp)
                        st.remove(temp)

                        temp = random.choice(st)
                        d_team.append(temp)
                        st.remove(temp)
                    except:
                        print(a_team)

                    # LW 선발
                    try:
                        temp_lw = random.choice(lw)
                        b_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        c_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        d_team.append(temp_lw)
                        lw.remove(temp_lw)

                        temp_lw = random.choice(lw)
                        a_team.append(temp_lw)
                        lw.remove(temp_lw)
                    except:
                        print(a_team)

                    # RW 선발
                    try:
                        temp_rw = random.choice(rw)
                        c_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        d_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        b_team.append(temp_rw)
                        rw.remove(temp_rw)

                        temp_rw = random.choice(rw)
                        a_team.append(temp_rw)
                        rw.remove(temp_rw)
                    except:
                        print(a_team)

                    # CM 선발 & 대기열 이동
                    try:
                        for j in range(0, 2):
                            temp_cm = random.choice(cm)
                            d_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            a_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            b_team.append(temp_cm)
                            cm.remove(temp_cm)

                            temp_cm = random.choice(cm)
                            c_team.append(temp_cm)
                            cm.remove(temp_cm)
                    except:
                        print(a_team)

                    # CDM 선발
                    try:
                        temp_cdm = random.choice(cdm)
                        a_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        b_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        c_team.append(temp_cdm)
                        cdm.remove(temp_cdm)

                        temp_cdm = random.choice(cdm)
                        d_team.append(temp_cdm)
                        cdm.remove(temp_cdm)
                    except:
                        print(a_team)

                    # LB 선발
                    try:
                        temp_lb = random.choice(lb)
                        b_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        c_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        a_team.append(temp_lb)
                        lb.remove(temp_lb)

                        temp_lb = random.choice(lb)
                        d_team.append(temp_lb)
                        lb.remove(temp_lb)

                    except:
                        print(a_team)

                    # CB 선발
                    try:
                        for j in range(0, 2):
                            temp_cb = random.choice(cb)
                            c_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            d_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            a_team.append(temp_cb)
                            cb.remove(temp_cb)

                            temp_cb = random.choice(cb)
                            b_team.append(temp_cb)
                            cb.remove(temp_cb)
                    except:
                        print(a_team)

                    # RB 선발
                    try:
                        temp_rb = random.choice(rb)
                        d_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        a_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        b_team.append(temp_rb)
                        rb.remove(temp_rb)

                        temp_rb = random.choice(rb)
                        c_team.append(temp_rb)
                        rb.remove(temp_rb)
                    except:
                        print(a_team)

                    # GK 선발
                    try:
                        temp_gk = random.choice(gk)
                        a_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        b_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        c_team.append(temp_gk)
                        gk.remove(temp_gk)

                        temp_gk = random.choice(gk)
                        d_team.append(temp_gk)
                        gk.remove(temp_gk)
                    except:
                        print(a_team)

                    # ST 대기열 정리
                    for j in range(0, len(st)):
                        try:
                            queue.append(st[j])
                        except:
                            print(a_team)

                    # LW 대기열 정리
                    for j in range(0, len(lw)):
                        try:
                            queue.append(lw[j])
                        except:
                            print(a_team)

                    # RW 대기열 정리
                    for j in range(0, len(rw)):
                        try:
                            queue.append(rw[j])
                        except:
                            print(a_team)

                    # CM 대기열 정리
                    for j in range(0, len(cm)):
                        try:
                            queue.append(cm[j])
                        except:
                            print(a_team)

                    # CDM 대기열 정리
                    for j in range(0, len(cdm)):
                        try:
                            queue.append(cdm[j])
                        except:
                            print(a_team)

                    # LB 대기열 정리
                    for j in range(0, len(lb)):
                        try:
                            queue.append(lb[j])
                        except:
                            print(a_team)

                    # CB 대기열 정리
                    for j in range(0, len(cb)):
                        try:
                            queue.append(cb[j])
                        except:
                            print(a_team)

                    # RB 대기열 정리
                    for j in range(0, len(rb)):
                        try:
                            queue.append(rb[j])
                        except:
                            print(a_team)

                    # GK 대기열 정리
                    for j in range(0, len(gk)):
                        try:
                            queue.append(gk[j])
                        except:
                            print(a_team)

                    # 내전 A팀
                    temp_a_team = ""
                    for j in range(0, len(a_team)+1):
                        try:
                            temp_a_team = temp_a_team + " " + a_team[j]
                            if a_team[j].startswith("ST"):
                                if a_team[j + 1].startswith("LW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LW"):
                                if a_team[j + 1].startswith("RW"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RW"):
                                if a_team[j + 1].startswith("CM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CM"):
                                if a_team[j + 1].startswith("CDM"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CDM"):
                                if a_team[j + 1].startswith("LB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("LB"):
                                if a_team[j + 1].startswith("CB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("CB"):
                                if a_team[j + 1].startswith("RB"):
                                    temp_a_team = temp_a_team + "\n\n"
                            if a_team[j].startswith("RB"):
                                if a_team[j + 1].startswith("GK"):
                                    temp_a_team = temp_a_team + "\n\n"
                        except:
                            print(temp_a_team)

                    await ctx.send(content=f"팀 A({TEAM_A_COLOR}) 명단 : \n" + temp_a_team)

                    # 내전 B팀
                    temp_b_team = ""
                    for i in range(0, len(b_team)+1):
                        try:
                            temp_b_team = temp_b_team + " " + b_team[i]
                            if b_team[i].startswith("ST"):
                                if b_team[i + 1].startswith("LW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LW"):
                                if b_team[i + 1].startswith("RW"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RW"):
                                if b_team[i + 1].startswith("CM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CM"):
                                if b_team[i + 1].startswith("CDM"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CDM"):
                                if b_team[i + 1].startswith("LB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("LB"):
                                if b_team[i + 1].startswith("CB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("CB"):
                                if b_team[i + 1].startswith("RB"):
                                    temp_b_team = temp_b_team + "\n\n"
                            if b_team[i].startswith("RB"):
                                if b_team[i + 1].startswith("GK", ""):
                                    temp_b_team = temp_b_team + "\n\n"
                        except:
                            print(temp_b_team)

                    await ctx.send(content=f"\n팀 B({TEAM_B_COLOR}) 명단 : \n" + temp_b_team)

                    # 내전 C팀
                    temp_c_team = ""
                    for i in range(0, len(c_team)+1):
                        try:
                            temp_c_team = temp_c_team + " " + c_team[i]
                            if c_team[i].startswith("ST"):
                                if c_team[i + 1].startswith("LW"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("LW"):
                                if c_team[i + 1].startswith("RW"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("RW"):
                                if c_team[i + 1].startswith("CM"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CM"):
                                if c_team[i + 1].startswith("CDM"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CDM"):
                                if c_team[i + 1].startswith("LB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("LB"):
                                if c_team[i + 1].startswith("CB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("CB"):
                                if c_team[i + 1].startswith("RB"):
                                    temp_c_team = temp_c_team + "\n\n"
                            if c_team[i].startswith("RB"):
                                if c_team[i + 1].startswith("GK", ""):
                                    temp_c_team = temp_c_team + "\n\n"
                        except:
                            print(temp_c_team)

                    await ctx.send(content=f"\n팀 C({TEAM_C_COLOR}) 명단 : \n" + temp_c_team)

                    # 내전 D팀
                    temp_d_team = ""
                    for i in range(0, len(d_team)+1):
                        try:
                            temp_d_team = temp_d_team + " " + d_team[i]
                            if d_team[i].startswith("ST"):
                                if d_team[i + 1].startswith("LW"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("LW"):
                                if d_team[i + 1].startswith("RW"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("RW"):
                                if d_team[i + 1].startswith("CM"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("CM"):
                                if d_team[i + 1].startswith("CDM"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("CDM"):
                                if d_team[i + 1].startswith("LB"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("LB"):
                                if d_team[i + 1].startswith("CB"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("CB"):
                                if d_team[i + 1].startswith("RB"):
                                    temp_d_team = temp_d_team + "\n\n"
                            if d_team[i].startswith("RB"):
                                if d_team[i + 1].startswith("GK", ""):
                                    temp_d_team = temp_d_team + "\n\n"
                        except:
                            print(temp_d_team)

                    await ctx.send(content=f"\n팀 D({TEAM_D_COLOR}) 명단 : \n" + temp_d_team)

                    temp_w_team = ""
                    for i in range(0, len(queue)):
                        try:
                            if queue[i].startswith("ST"):
                                queue[i].replace("ST", "")
                                temp_w_team = temp_w_team + queue[i] + " ST\n"
                            if queue[i].startswith("LW"):
                                queue[i].replace("LW", "")
                                temp_w_team = temp_w_team + queue[i] + " LW\n"
                            if queue[i].startswith("RW"):
                                queue[i].replace("RW", "")
                                temp_w_team = temp_w_team + queue[i] + " RW\n"
                            if queue[i].startswith("CM"):
                                queue[i].replace("CM", "")
                                temp_w_team = temp_w_team + queue[i] + " CM\n"
                            if queue[i].startswith("CDM"):
                                queue[i].replace("CDM", "")
                                temp_w_team = temp_w_team + queue[i] + " CDM\n"
                            if queue[i].startswith("LB"):
                                queue[i].replace("LB", "")
                                temp_w_team = temp_w_team + queue[i] + " LB\n"
                            if queue[i].startswith("CB"):
                                queue[i].replace("CB", "")
                                temp_w_team = temp_w_team + queue[i] + " CB\n"
                            if queue[i].startswith("RB"):
                                queue[i].replace("RB", "")
                                temp_w_team = temp_w_team + queue[i] + " RB\n"
                            if queue[i].startswith("GK"):
                                queue[i].replace("GK", "")
                                temp_w_team = temp_w_team + queue[i] + " GK\n"
                        except:
                            pass

                    await ctx.send("\n\n대기 \n" + temp_w_team)

    '''
    @bot.command()
    async def 대기실분배2(self, ctx, num1, num2):
        key = 0
        div = []
        wait_mem_name = []
        wait_mem_pos = []
        alert = ""

        for i in range(1, len(wait_mem)):
            split = wait_mem[i].split('/')
            wait_mem_name[i] = split[0]
            wait_mem_pos[i] = split[1]

            alert = alert + f"{i} . " + wait_mem[i] + "\n"

        await ctx.send("대기목록 \n")
        await ctx.send("```" + alert + "```")
        await ctx.send(content=f"닉네임 : {wait_mem_name}, 포지션 : {wait_mem_pos}")
        key = 1

        if key == 1:
            if num1 == num2:
                for j in range(0, len(wait_mem)-1):
                    pass
    '''


#bot.run(key)

def setup(bot):
    bot.add_cog(Draft(bot))