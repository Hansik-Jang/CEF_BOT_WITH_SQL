import discord
import asyncio
import time
import random
import os
import string
from discord.ext import commands
from discord.utils import get
import QueueFun

MAX_COUNT = 20
DRAFT_COUNT = 5
DELETE_AMOUNT = 2
BOT_SLEEP_TIME = 2
TEAM_A_COLOR = "파랑"
TEAM_B_COLOR = "검정"
TEAM_C_COLOR = "하양"
TEAM_D_COLOR = "빨강"

bot = commands.Bot(command_prefix='%')

f = open("key.txt", 'r')
key = f.readline()

switch = 0
entry = [""]
wait_list_member_list = []
wait_pos_count_list = [0]*10

class FormationInfo:
    def __main__(self, st_count, lw_count, rw_count, cam_count, cm_count, cdm_count, lb_count, cb_count, rb_count, gk_count):
        self.st_count = None

def WaitPosFind(pos):
    temp_num = 0
    if pos == "ST":
        temp_num += 0
    if pos == "LW":
        temp_num += 1
    if pos == "RW" :
        temp_num += 2
    if pos == "CAM":
        temp_num += 3
    if pos == "CM":
        temp_num += 4
    if pos == "CDM":
        temp_num += 5
    if pos == "LB":
        temp_num += 6
    if pos == "CB":
        temp_num += 7
    if pos == "RB":
        temp_num += 8
    if pos == "GK":
        temp_num += 9
    return temp_num

'''queue = []%
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
a_team = []
b_team = []
c_team = []
d_team = []
wait_mem = [""]
wait_temp = []
form = [""]
wait_mem_mention = []'''

@bot.event
async def on_ready():
    print('로그인 중')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("'%도움말' | 드래프트봇")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def 개빡(ctx):
    pass

@bot.command()
async def 테스트드래프트(ctx):

    '''entry.clear()
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

    global wait_st
    global wait_lw
    global wait_rw
    global wait_cam
    global wait_cm
    global wait_cdm
    global wait_lb
    global wait_cb
    global wait_rb
    global wait_gk

    a_st_queue = 0
    a_lw_queue = 0
    a_rw_queue = 0
    a_cam_queue = 0
    a_cm_queue = 0
    a_cdm_queue = 0
    a_lb_queue = 0
    a_cb_queue = 0
    a_rb_queue = 0
    a_gk_queue = 0
    b_st_queue = 0
    b_lw_queue = 0
    b_rw_queue = 0
    b_cam_queue = 0
    b_cm_queue = 0
    b_cdm_queue = 0
    b_lb_queue = 0
    b_cb_queue = 0
    b_rb_queue = 0
    b_gk_queue = 0
    global wait_mem
    global wait_mem_mention
    print(wait_mem_mention)
    for i in range(0, len(wait_mem_mention)):
        if wait_mem_mention[i].startswith("ST"):
            wait_st.append(wait_mem_mention[i])
            print(wait_st, len(wait_st))
        if wait_mem_mention[i].startswith("LW"):
            wait_lw.append(wait_mem_mention[i])
            print(wait_lw)
        if wait_mem_mention[i].startswith("RW"):
            wait_rw.append(wait_mem_mention[i])
            print(wait_rw)
        if wait_mem_mention[i].startswith("CAM"):
            wait_cam.append(wait_mem_mention[i])
            print(wait_cam)
        if wait_mem_mention[i].startswith("CM"):
            wait_cm.append(wait_mem_mention[i])
            print(wait_cm)
        if wait_mem_mention[i].startswith("CDM"):
            wait_cdm.append(wait_mem_mention[i])
            print(wait_cdm)
        if wait_mem_mention[i].startswith("LB"):
            wait_lb.append(wait_mem_mention[i])
            print(wait_lb)
        if wait_mem_mention[i].startswith("CB"):
            wait_cb.append(wait_mem_mention[i])
            print(wait_cb)
        if wait_mem_mention[i].startswith("RB"):
            wait_rb.append(wait_mem_mention[i])
            print(wait_rb)
        if wait_mem_mention[i].startswith("GK"):
            wait_gk.append(wait_mem_mention[i])
            print(wait_gk)
    wait_mem_mention.clear()
    print(wait_mem_mention)


    form = ["3-5-2", "3-4-3 플랫", "4-1-2-1-2 넓게", "4-1-2-1-2 좁게", "4-4-2 플랫", "4-2-3-1 넓게",
            "4-3-3 홀딩", "3-4-3 다이아몬드", "5-3-2", "4-1-2-1-2 좁게", "3-5-1-1"]

    await ctx.send(content=f"```cs\n"
                           f"포메이션 후보 : \n"
                           f"'3-5-2', '3-4-3 플랫', ''4-1-2-1-2 넓게', '4-1-2-1-2 좁게',\n"
                           f"'4-4-2 플랫', '4-2-3-1 넓게', '4-3-3 홀딩', '3-4-3 다이아몬드',\n"
                           f"'5-3-2', '4-1-2-1-2 좁게', '3-5-1-1'```")

    cd = await ctx.send("포메이션을 랜덤으로 뽑습니다")
    time.sleep(1)
    for i in range(0, 3):
        j = 3 - i
        await cd.edit(content=f"카운트다운 : {j}초")
        time.sleep(1)
        if j == 1:
            a_team_form = random.choice(form)
            b_team_form = random.choice(form)

    await ctx.send(content=f"```A팀 포메이션 : {a_team_form}\n```")
    if a_team_form == "4-3-3 홀딩":
        await ctx.send("```LW       ST      RW\n"
                       "    CM       CM\n"
                       "        CDM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "4-3-2-1, 4-3-3 플랫, 4-5-1 플랫, 4-5-1 공격, 4-3-3 가짜 공격수```")
        a_st_queue += 1
        a_lw_queue += 1
        a_rw_queue += 1
        a_cm_queue += 2
        a_cdm_queue += 1
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1
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
        a_st_queue += 2
        a_cam_queue += 1
        a_cdm_queue += 2
        a_lb_queue += 1
        a_cb_queue += 3
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
        await ctx.send("```LW       ST      RW\n"
                       "LM   LCM   RCM   RM\n"
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                       "3-4-2-1, 5-4-1 플랫, 5-2-2-1```")
        a_st_queue += 1
        a_lw_queue += 1
        a_rw_queue += 1
        a_cm_queue += 2
        a_lb_queue += 1
        a_cb_queue += 3
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "4-1-2-1-2 넓게":
        await ctx.send("```.    ST     ST\n"
                       "        CAM\n"
                       "LM               RM\n"
                       "        CDM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"     
                       "유사한 포메이션 : \n"
                       "4-1-3-2```")
        a_st_queue += 2
        a_cam_queue += 1
        a_lw_queue += 1
        a_rw_queue += 1
        a_cdm_queue += 1
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "4-4-2 플랫":
        await ctx.send("```.    ST     ST\n"
                       "LM   LCM   RCM   RM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"
                       "4-2-2-2, 4-4-2, 4-4-2 홀딩, 4-2-4```")
        a_st_queue += 2
        a_lw_queue += 1
        a_rw_queue += 1
        a_cm_queue += 2
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1
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
        a_st_queue += 1
        a_lw_queue += 1
        a_rw_queue += 1
        a_cam_queue += 1
        a_cdm_queue += 2
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1
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
        a_st_queue += 1
        a_lw_queue += 1
        a_rw_queue += 1
        a_cam_queue += 1
        a_cdm_queue += 1
        a_lb_queue += 1
        a_cb_queue += 3
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "5-3-2":
        await ctx.send("```.    ST     ST\n"
                       "    CM   CM   CM\n"
                       "LWB             RWB\n"  
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "안내사항 : LWB, RWB은 LB, RB를 선택하세요.\n"
                       "3-1-4-2 다이아몬드```")
        a_st_queue += 2
        a_cm_queue += 3
        a_lb_queue += 1
        a_cb_queue += 3
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "4-1-2-1-2 좁게":
        await ctx.send("```.    ST     ST\n"
                       "        CAM\n"
                       "    CM       CM\n"
                       "        CDM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "4-3-1-2```")
        a_st_queue += 2
        a_cam_queue += 1
        a_cm_queue += 2
        a_cdm_queue += 1
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1
    elif a_team_form == "3-5-1-1":  # CF는 CAM 처리
        await ctx.send("```.        ST\n"
                       "         CF\n"
                       "LM       CM      RM\n"                  
                       "     CDM   CDM\n"
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "안내사항 : CF는 CAM을 선택하세요.\n"
                       "유사한 포메이션 : 없음 \n```")
        a_st_queue += 1
        a_cam_queue += 1
        a_cm_queue += 1
        a_cdm_queue += 2
        a_lb_queue += 1
        a_cb_queue += 2
        a_rb_queue += 1
        a_gk_queue += 1

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
        b_st_queue += 1
        b_lw_queue += 1
        b_rw_queue += 1
        b_cm_queue += 2
        b_cdm_queue += 1
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1
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
        b_st_queue += 2
        b_cam_queue += 1
        b_cdm_queue += 2
        b_lb_queue += 1
        b_cb_queue += 3
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
        await ctx.send("```LW       ST      RW\n"
                       "LM   LCM   RCM   RM\n"
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "안내사항 : LM, RM은 LB, RB를 선택하세요.\n"
                       "3-4-2-1, 5-4-1 플랫, 5-2-2-1```")
        b_st_queue += 1
        b_lw_queue += 1
        b_rw_queue += 1
        b_cm_queue += 2
        b_lb_queue += 1
        b_cb_queue += 3
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "4-1-2-1-2 넓게": # LM, RM은 LW, RW으로 처리
        await ctx.send("```.    ST     ST\n"
                       "        CAM\n"
                       "LM               RM\n"
                       "        CDM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "안내사항 : LM, RM은 LW, RW를 선택하세요.\n"     
                       "유사한 포메이션 : \n"
                       "4-1-3-2```")
        b_st_queue += 2
        b_cam_queue += 1
        b_lw_queue += 1
        b_rw_queue += 1
        b_cdm_queue += 1
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "4-4-2 플랫": # LM, RM은 LW, RW으로 처리
        await ctx.send("```.    ST     ST\n"
                       "LM   LCM   RCM   RM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "4-2-2-2, 4-4-2, 4-4-2 홀딩, 4-2-4```")
        b_st_queue += 2
        b_lw_queue += 1
        b_rw_queue += 1
        b_cm_queue += 2
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1
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
        b_st_queue += 1
        b_lw_queue += 1
        b_rw_queue += 1
        b_cam_queue += 1
        b_cdm_queue += 2
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1
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
        b_st_queue += 1
        b_lw_queue += 1
        b_rw_queue += 1
        b_cam_queue += 1
        b_cdm_queue += 1
        b_lb_queue += 1
        b_cb_queue += 3
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "5-3-2": # 윙백은 풀백으로 처리
        await ctx.send("```.    ST     ST\n"
                       "        CAM\n"
                       "    CM   CM   CM\n"
                       "LWB     CDM     RWB\n"
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "3-1-4-2 다이아몬드```")
        b_st_queue += 2
        b_cm_queue += 3
        b_lb_queue += 1
        b_cb_queue += 3
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "4-1-2-1-2 좁게":
        await ctx.send("```.    ST     ST\n"
                       "        CAM\n"
                       "    CM       CM\n"
                       "        CDM\n"
                       "LB   LCB   RCB   RB\n"
                       "        GK\n"
                       "유사한 포메이션 : \n"
                       "4-3-1-2```")
        b_st_queue += 2
        b_cam_queue += 1
        b_cm_queue += 2
        b_cdm_queue += 1
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1
    elif b_team_form == "3-5-1-1":  # CF는 CAM 처리
        await ctx.send("```.        ST\n"
                       "         CF\n"
                       "LM       CM      RM\n"
                       "     CDM   CDM\n"
                       "   LCB  RCB  RCB\n"
                       "        GK\n"
                       "안내사항 : CF는 CAM을 선택하세요.\n"
                       "유사한 포메이션 : 없음 \n```")
        b_st_queue += 1
        b_cam_queue += 1
        b_cm_queue += 1
        b_cdm_queue += 2
        b_lb_queue += 1
        b_cb_queue += 2
        b_rb_queue += 1
        b_gk_queue += 1

    st_queue = a_st_queue + b_st_queue
    empty_st_queue = st_queue - len(wait_st)
    lw_queue = a_lw_queue + b_lw_queue
    empty_lw_queue = lw_queue - len(wait_lw)
    rw_queue = a_rw_queue + b_rw_queue
    empty_rw_queue = rw_queue - len(wait_rw)
    cam_queue = a_cam_queue + b_cam_queue
    empty_cam_queue = cam_queue - len(wait_cam)
    cm_queue = a_cm_queue + b_cm_queue
    empty_cm_queue = cm_queue - len(wait_cm)
    cdm_queue = a_cdm_queue + b_cdm_queue
    empty_cdm_queue = cdm_queue - len(wait_cdm)
    lb_queue = a_lb_queue + b_lb_queue
    empty_lb_queue = lb_queue - len(wait_lb)
    cb_queue = a_cb_queue + b_cb_queue
    empty_cb_queue = cb_queue - len(wait_cb)
    rb_queue = a_rb_queue + b_rb_queue
    empty_rb_queue = rb_queue - len(wait_rb)
    gk_queue = a_gk_queue + b_gk_queue
    empty_gk_queue = gk_queue - len(wait_gk)
    await ctx.send(content=f"```포지션별 인원 제한은 다음과 같습니다.\n"
                           f"포지션 : 포지션별 제한(잔여 자리)\n"
                           f"ST : {st_queue} // {empty_st_queue}\n"
                           f"LW : {lw_queue} // {empty_lw_queue}\n"
                           f"RW : {rw_queue} // {empty_rw_queue}\n"
                           f"CAM : {cam_queue} // {empty_cam_queue}\n"
                           f"CM : {cm_queue} // {empty_cm_queue}\n"
                           f"CDM : {cdm_queue} // {empty_cdm_queue}\n"
                           f"LB : {lb_queue} // {empty_lb_queue}\n"
                           f"CB : {cb_queue} // {empty_cb_queue}\n"
                           f"RB : {rb_queue} // {empty_rb_queue}\n"
                           f"GK : {gk_queue} // {empty_gk_queue}\n```")
    if a_team_form == "4-5-1 공격" or a_team_form == "4-4-2 플랫" or a_team_form == "4-1-2-1-2 넓게" or b_team_form == "4-5-1 공격" or b_team_form == "4-4-2 플랫" or b_team_form == "4-1-2-1-2 넓게":
        await ctx.send("```cs\n"
                       "'4-5-1 공격', '4-2-3-1 넓게', '4-4-2 플랫', '4-1-2-1-2 좁게' 포메이션의 경우,\n"
                       "LM, RM은 LW, RW을 누르세요```")
    if a_team_form == "5-3-2" or a_team_form == "3-5-2" or a_team_form == "3-4-3 플랫" or b_team_form == "5-3-2" or b_team_form == "3-5-2" or b_team_form == "3-4-3 플랫":
        await ctx.send("```cs\n"
                       "'3-5-2', '3-4-3', '5-3-2', '3-5-1-1' 포메이션의 경우,\n"
                       "LM, LWB, RM, RWB는 LB, RB를 누르세요```")
    if a_team_form == "3-5-1-1 공격" or b_team_form == "3-5-1-1 공격":
        await ctx.send("```cs\n"
                       "'3-5-1-1 공격' 포메이션의 CF 포지션은 CAM을 선택하세요.```")


    draft = await ctx.send("희망하는 포지션을 선택해주세요.")
    if empty_st_queue > 0:
        await draft.add_reaction("<:ST:706530008465932299>")
    if empty_lw_queue > 0:
        await draft.add_reaction("<:LW:706530007937450036>")
    if empty_rw_queue > 0:
        await draft.add_reaction("<:RW:706530008201560156>")
    if empty_cam_queue > 0:
        await draft.add_reaction("<:CAM:706530008243634176>")
    if empty_cm_queue > 0:
        await draft.add_reaction("<:CM:706530007928930386>")
    if empty_cdm_queue > 0:
        await draft.add_reaction("<:CDM:706530008289509466>")
    if empty_lb_queue > 0:
        await draft.add_reaction("<:LB:706530008369463359>")
    if empty_cb_queue > 0:
        await draft.add_reaction("<:CB:706530008113610803>")
    if empty_rb_queue > 0:
        await draft.add_reaction("<:RB:706530008100765707>")
    if empty_gk_queue > 0:
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
                if len(wait_st) >= st_queue:
                    for i in range(st_queue, len(wait_st):
                        wait_mem.append()


                if empty_st_queue>0:
                    # A팀
                    if a_st_queue > 0:                  # 만약 A팀의 ST 수가 0보다 크면,
                        for i in range(0, a_st_queue):     # A팀 ST 수만큼
                            print(st)
                            temp = random.choice(st)    # 랜덤으로 선발해
                            a_team.append(temp)         # A팀으로 배분 후
                            st.remove(temp)             # ST 리스트에서 제거
                    # B팀
                    if b_st_queue > 0:
                        for i in range(0, b_st_queue):
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
                if b_lw_queue > 0:
                    for i in range(b_lw_queue):
                        temp = random.choice(lw)
                        b_team.append(temp)
                        lw.remove(temp)
                # A팀
                if a_lw_queue > 0:
                    for i in range(a_lw_queue):
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
                if a_rw_queue > 0:
                    for i in range(a_rw_queue):
                        temp = random.choice(rw)
                        a_team.append(temp)
                        rw.remove(temp)
                # B팀
                if b_rw_queue > 0:
                    for i in range(b_rw_queue):
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
                print(b_cam_queue)
                print(cam)
                if b_cam_queue > 0:
                    for i in range(b_cam_queue):
                        temp = random.choice(cam)
                        b_team.append(temp)
                        cam.remove(temp)
                # A팀
                if a_cam_queue > 0:
                    for i in range(a_cam_queue):
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
                if a_cm_queue > 0:
                    for i in range(a_cm_queue):
                        temp = random.choice(cm)
                        a_team.append(temp)
                        cm.remove(temp)
                # B팀
                if b_cm_queue > 0:
                    for i in range(b_cm_queue):
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
                if b_cdm_queue > 0:
                    for i in range(b_cdm_queue):
                        temp = random.choice(cdm)
                        b_team.append(temp)
                        cdm.remove(temp)
                # A팀
                if a_cdm_queue > 0:
                    for i in range(a_cdm_queue):
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
                if a_lb_queue > 0:
                    for i in range(a_lb_queue):
                        temp = random.choice(lb)
                        a_team.append(temp)
                        lb.remove(temp)
                # B팀
                if b_lb_queue > 0:
                    for i in range(b_lb_queue):
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
                if b_cb_queue > 0:
                    for i in range(b_cb_queue):
                        temp = random.choice(cb)
                        b_team.append(temp)
                        cb.remove(temp)
                # A팀
                if a_cb_queue > 0:
                    for i in range(a_cb_queue):
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

                if a_rb_queue > 0:
                    for i in range(a_rb_queue):
                        temp = random.choice(rb)
                        a_team.append(temp)
                        rb.remove(temp)
                # B팀
                if b_rb_queue > 0:
                    for i in range(b_rb_queue):
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
                if b_rb_queue > 0:
                    for i in range(b_rb_queue):
                        temp = random.choice(gk)
                        b_team.append(temp)
                        gk.remove(temp)
                # A팀
                if a_gk_queue > 0:
                    for i in range(a_gk_queue):
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

            await ctx.send("\n\n대기 \n" + temp_w_team)'''




@bot.command()
async def 테초기화(ctx):
    wait_pos_count_list.clear()
    await ctx.send(ctx.author.mention + "님이 경기 대기실을 초기화하였습니다.")
    pass
    '''wait_mem.clear()
    wait_mem.append("")
    await ctx.send(ctx.author.mention + "님이 경기 대기실을 초기화하였습니다.")
    time.sleep(BOT_SLEEP_TIME)'''


@bot.command()
async def 테번호삭제(ctx, *, text):
    pass
    '''del_wait = ""
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
        await ctx.send("정확한 번호를 입력해주세요")'''





@bot.command()
async def 테참가(ctx, *, pos):
    queue_num = 0
    overlap = 0
    pos = pos.upper()
    wait_pos_count_list[WaitPosFind(pos)] += 1
    for i in range(len(wait_list_member_list)):
        if ctx.author.display_name in wait_list_member_list:
            overlap = 1
            break;
        else:
            overlap = 0
            queue_num = i
    if overlap == 0:
        wait_list_member_list.append(pos + " - " + ctx.author.display_name)
        await ctx.send(content=f"```{ctx.author.display_name}님\n"
                               f"대기 목록 {queue_num}번에 {pos} 포지션으로 참가되었습니다.\n"
                               f"{pos} 포지션은 총 {wait_pos_count_list[WaitPosFind(pos)]} 명 대기 중입니다.```")
    else:
        await ctx.send(content=f"```이미 참가되어있습니다.\n```")


@bot.command()
async def 테삭제(ctx):
    queue_num = 0
    overlap = 0
    for i in range(0, len(wait_list_member_list)):
        if wait_list_member_list[i].endswith(ctx.author.display_name):
            wait_list_member_list.remove(wait_list_member_list[i])
            temp = wait_list_member_list[i]
            pos = temp.split(" ")
            print(pos)
            wait_pos_count_list[WaitPosFind(pos)] -= 1
            await ctx.send(content=f"```{ctx.author.display_name} + 삭제되었습니다.```")
        else:
            await ctx.send(content=f"{ctx.author.display_name} 님은 대기열에 없습니다.")









'''    text = text.upper()
    try:
        for i in range(0, len(wait_mem)):
            if ctx.author.display_name in wait_mem[i]:
                check_overlap = 1
                break
            else:
                check_overlap = 0
        if check_overlap == 0:
            wait_mem.append(ctx.author.display_name + "/" + text)
            wait_mem_mention.append(text+"/" + ctx.author.mention)

            await ctx.send(content=f"{ctx.author.display_name}님\n"
                                   f"경기 대기실 목록에 {text} 포지션으로 추가되었습니다")
            await ctx.send(wait_mem_mention)
            time.sleep(BOT_SLEEP_TIME)
        else:
            await ctx.send("중복 등록이므로 불가합니다.")
            time.sleep(BOT_SLEEP_TIME)
    except:
        print("aaa")
    try:
        for i in range(0, len(wait_mem)):
            if wait_mem[i].startswith(ctx.author.display_name):
                wait_mem.remove(wait_mem[i])
                wait_mem_mention.remove(wait_mem_mention[i])
                await ctx.send(ctx.author.display_name + "삭제되었습니다")

    except:
        await ctx.send(content=f"{ctx.author.display_name} 님은 대기열에 없습니다.")
'''

@bot.command()
async def 테목록(ctx):
    temp = ""
    for i in range(0, len(wait_list_member_list)) :
        temp = temp + f"{i + 1}. " + wait_list_member_list[i] + "\n"
    if temp == "":
        await ctx.send("대기목록\n")
        await ctx.send("``` ```")
    else:
        await ctx.send("대기목록\n")
        await ctx.send("```" + temp + "```")


@bot.event
async def on_reaction_add(reaction, user):
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
        if str(reaction.emoji) == "<:LW:706530007937450036>":
            entry.append("LW/" + user.mention)
        if str(reaction.emoji) == "<:RW:706530008201560156>":
            entry.append("RW/" + user.mention)
        if str(reaction.emoji) == "<:CM:706530007928930386>":
            entry.append("CM/" + user.mention)
        if str(reaction.emoji) == "<:CAM:706530008243634176>":
            entry.append("CAM/" + user.mention)
        if str(reaction.emoji) == "<:CDM:706530008289509466>":
            entry.append("CDM/" + user.mention)
        if str(reaction.emoji) == "<:LB:706530008369463359>":
            entry.append("LB/" + user.mention)
        if str(reaction.emoji) == "<:CB:706530008113610803>":
            entry.append("CB/" + user.mention)
        if str(reaction.emoji) == "<:RB:706530008100765707>":
            entry.append("RB/" + user.mention)
        if str(reaction.emoji) == "<:GK:706530008088182786>":
            entry.append("GK/" + user.mention)


bot.run(key)
