import discord
import time
import random
from FunForDraft import *
from discord.ext import commands
import draftclass

switch = 0
entry = []
captain = []
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

CAP_TIME = 3
DRAFT_TIME = 15
CURRENT_DRAFT_COUNT = 0
CURRENT_DRAFT_PLAYER = 0
TeamA = draftclass.TeamA()
TeamB = draftclass.TeamB()
TeamC = draftclass.TeamC()
TeamD = draftclass.TeamD()


class Body(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='임베드', pass_context=True)
    async def 테스트(self, ctx):
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
        CURRENT_DRAFT_COUNT = 2
        CURRENT_DRAFT_PLAYER = 22

        entry.clear()
        captain.clear()
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
                await ctx.send("```전달사항 : 위의 현황을 복사 붙여넣기 해서 지우는 방식으로 하시면 조금이나마 빠르게 진행할 듯 합니다.```")


    @commands.command(name='개발', aliases=["주장개발"], pass_context=True)
    async def 주장개발중(self, ctx):
        global TeamA
        global TeamB
        global CURRENT_DRAFT_COUNT
        CURRENT_DRAFT_COUNT = 2
        CURRENT_DRAFT_PLAYER = 22

        entry.clear()
        captain.clear()
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
        for i in range(0, CAP_TIME):
            j = CAP_TIME - i
            await count.edit(content=f"{j}초 남았습니다.")
            time.sleep(1)
            if j == 1:
                await count.edit(conent=f"선택 종료")
                print(len(captain))
                print(captain)
                if len(captain) < 2:
                    await ctx.send("내전 주장 지원자가 부족합니다.\n"
                                   "다시 드래프트를 실행해주세요.")
                else:
                    # 주장 선발
                    selected_captain1 = random.choice(captain)
                    captain.remove(selected_captain1)
                    selected_captain2 = random.choice(captain)
                    await ctx.send(content=f"A팀 주장 - {selected_captain1}\n"
                                           f"B팀 주장 - {selected_captain2}")
                    TeamA.setData('cap', selected_captain1)
                    #TeamB.setData('cap', selected_captain2)

                    draft = await ctx.send("포지션을 선택해주세요")
                    for s in tpli :
                        await draft.add_reaction(s)

                    cd = await ctx.send("카운트 다운")
                    for i in range(0, DRAFT_TIME):
                        j = DRAFT_TIME - i
                        await cd.edit(content=f"{j}초 남았습니다.")
                        time.sleep(1)
                        if j == 1:
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
                            await ctx.send(content=f"{TeamA.getData('cap')} 님은 팀원을 선택해주세요.\n"
                                                   f"%선발 @멘션 으로 선택해주세요.")

    @commands.command(name='선발', pass_context=True)
    async def 선발(self, ctx, pos, member: discord.member):
        global TeamA
        global TeamB
        global TeamC
        global TeamD
        global CURRENT_DRAFT_PLAYER

        pos = pos.lower()
        pos_li = ['st', 'lw', 'rw', 'cam', 'cm', 'cdm', 'lb', 'cb', 'rb', 'gk']
        if pos in pos_li:                           # 포지션 입력 검사사
            if CURRENT_DRAFT_COUNT == 2:                    # 2팀일 때
                if CURRENT_DRAFT_PLAYER % 2 == 0:                    # A팀 차례
                    if ctx.mention == TeamA.cap[0]:
                        pass
                else:                                                # B팀 차례
                    pass


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global switch
        print(user.display_name)
        if str(reaction.emoji) == '⭕':
            if user.bot:
                return None
            captain.append(user.mention)
            print(user.display_name)

        for i in range(0, len(entry)):
            if user.mention in entry[i]:
                switch = 1
                break
            else:
                switch = 0

        # 드래프트용
        if switch == 0:  # 스위치가 꺼져있으면
            if user.bot == 1:  # 봇이면 패스
                return None
            if str(reaction.emoji) == "<:ST:706530008465932299>":
                entry.append(user.mention)
                #st.append(user.mention)
                st.append(user.display_name)
            if str(reaction.emoji) == "<:LW:706530007937450036>":
                entry.append(user.mention)
                #lw.append(user.mention)
                lw.append(user.display_name)
            if str(reaction.emoji) == "<:RW:706530008201560156>":
                entry.append(user.mention)
                #rw.append(user.mention)
                rw.append(user.display_name)
            if str(reaction.emoji) == "<:CAM:706530008243634176>":
                entry.append(user.mention)
                #cam.append(user.mention)
                cam.append(user.display_name)
            if str(reaction.emoji) == "<:CM:706530007928930386>":
                entry.append(user.mention)
                #cm.append(user.mention)
                cm.append(user.display_name)
            if str(reaction.emoji) == "<:CDM:911666257219166248>":
                entry.append(user.mention)
                #cdm.append(user.mention)
                cdm.append(user.display_name)
            if str(reaction.emoji) == "<:LB:706530008369463359>":
                entry.append(user.mention)
                #lb.append(user.mention)
                lb.append(user.display_name)
            if str(reaction.emoji) == "<:CB:706530008113610803>":
                entry.append(user.mention)
                #cb.append(user.mention)
                cb.append(user.display_name)
            if str(reaction.emoji) == "<:RB:706530008100765707>":
                entry.append(user.mention)
                #rb.append(user.mention)
                rb.append(user.display_name)
            if str(reaction.emoji) == "<:GK:706530008088182786>":
                entry.append(user.mention)
                #gk.append(user.mention)
                gk.append(user.display_name)

def setup(bot):
    bot.add_cog(Body(bot))